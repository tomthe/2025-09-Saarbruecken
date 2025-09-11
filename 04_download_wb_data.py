import requests
import pandas as pd
import json
import time
from datetime import datetime

# World Bank API base URL
WB_API_BASE = "https://api.worldbank.org/v2"

def get_wb_indicators():
    """Get list of available World Bank indicators"""
    url = f"{WB_API_BASE}/indicator?format=json&per_page=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            return data[1]  # The actual data is in the second element
    return []

def search_demographic_indicators():
    """Search for demographic-related indicators"""
    print("Searching for demographic indicators...")
    indicators = get_wb_indicators()
    
    demographic_keywords = ['population', 'age', 'gender', 'male', 'female', 'demographic']
    relevant_indicators = []
    
    for indicator in indicators:
        name = indicator.get('name', '').lower()
        source_note = indicator.get('sourceNote', '').lower()
        
        if any(keyword in name or keyword in source_note for keyword in demographic_keywords):
            relevant_indicators.append({
                'id': indicator['id'],
                'name': indicator['name'],
                'sourceNote': indicator.get('sourceNote', '')[:200] + '...' if len(indicator.get('sourceNote', '')) > 200 else indicator.get('sourceNote', '')
            })
    
    return relevant_indicators

def get_wb_data(country_code, indicator_code, start_year=2015, end_year=2023):
    """Download data for a specific country and indicator"""
    url = f"{WB_API_BASE}/country/{country_code}/indicator/{indicator_code}"
    params = {
        'date': f"{start_year}:{end_year}",
        'format': 'json',
        'per_page': 1000
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 1 and data[1]:  # Check if we have actual data
                return data[1]
        return []
    except Exception as e:
        print(f"Error fetching data for {indicator_code}: {e}")
        return []

def download_demographic_data():
    """Download demographic data for Germany"""
    
    # Key demographic indicators for Germany
    indicators = {
        'SP.POP.TOTL': 'Total Population',
        'SP.POP.TOTL.MA.ZS': 'Population, male (% of total population)',
        'SP.POP.TOTL.FE.ZS': 'Population, female (% of total population)',
        'SP.POP.0014.TO.ZS': 'Population ages 0-14 (% of total population)',
        'SP.POP.1564.TO.ZS': 'Population ages 15-64 (% of total population)', 
        'SP.POP.65UP.TO.ZS': 'Population ages 65 and above (% of total population)',
        'SP.POP.0014.MA.ZS': 'Population ages 0-14, male (% of male population)',
        'SP.POP.1564.MA.ZS': 'Population ages 15-64, male (% of male population)',
        'SP.POP.65UP.MA.ZS': 'Population ages 65 and above, male (% of male population)',
        'SP.POP.0014.FE.ZS': 'Population ages 0-14, female (% of female population)',
        'SP.POP.1564.FE.ZS': 'Population ages 15-64, female (% of female population)',
        'SP.POP.65UP.FE.ZS': 'Population ages 65 and above, female (% of female population)',
        'SM.POP.NETM': 'Net migration',
        'SM.POP.TOTL.ZS': 'International migrant stock (% of population)'
    }
    
    country_code = 'DEU'  # Germany
    all_data = []
    
    print(f"Downloading demographic data for Germany...")
    
    for indicator_code, indicator_name in indicators.items():
        print(f"Fetching: {indicator_name}")
        data = get_wb_data(country_code, indicator_code)
        
        for record in data:
            if record['value'] is not None:
                all_data.append({
                    'country': record['country']['value'],
                    'country_code': record['countryiso3code'],
                    'indicator_code': indicator_code,
                    'indicator_name': indicator_name,
                    'year': record['date'],
                    'value': record['value']
                })
        
        # Be respectful to the API
        time.sleep(0.1)
    
    return pd.DataFrame(all_data)

def process_demographic_data(df):
    """Process and calculate additional demographic metrics"""
    if df.empty:
        return df
    
    # Get the latest year's data
    latest_year = df['year'].max()
    latest_data = df[df['year'] == latest_year].copy()
    
    # Create a summary table with key metrics
    summary = {}
    
    for _, row in latest_data.iterrows():
        summary[row['indicator_code']] = row['value']
    
    # Calculate absolute numbers from percentages
    total_pop = summary.get('SP.POP.TOTL', 0)
    
    # Calculate age group populations
    age_0_14_pct = summary.get('SP.POP.0014.TO.ZS', 0) / 100
    age_15_64_pct = summary.get('SP.POP.1564.TO.ZS', 0) / 100
    age_65_plus_pct = summary.get('SP.POP.65UP.TO.ZS', 0) / 100
    
    # Calculate gender split
    male_pct = summary.get('SP.POP.TOTL.MA.ZS', 0) / 100
    female_pct = summary.get('SP.POP.TOTL.FE.ZS', 0) / 100
    
    # Create processed data
    processed_data = []
    
    # Map LinkedIn age ranges to World Bank age groups
    linkedin_age_mapping = {
        '18-24': 'age_15_64',  # Best approximation
        '25-34': 'age_15_64',
        '35-54': 'age_15_64', 
        '55+': 'age_65_plus'   # Approximate
    }
    
    wb_age_populations = {
        'age_0_14': total_pop * age_0_14_pct,
        'age_15_64': total_pop * age_15_64_pct,
        'age_65_plus': total_pop * age_65_plus_pct
    }
    
    # Create rows for each LinkedIn demographic combination
    for age_range in ['All ages', '18-24', '25-34', '35-54', '55+']:
        for gender in ['All genders', 'male', 'female']:
            
            # Calculate population estimate
            if age_range == 'All ages':
                age_pop = total_pop
            else:
                wb_age_group = linkedin_age_mapping.get(age_range, 'age_15_64')
                age_pop = wb_age_populations[wb_age_group]
                
                # Rough approximation for specific LinkedIn age ranges within 15-64
                if age_range in ['18-24', '25-34', '35-54'] and wb_age_group == 'age_15_64':
                    # Assume roughly equal distribution within working age
                    age_pop = age_pop / 3  # Divide by 3 age groups
            
            if gender == 'All genders':
                pop_estimate = age_pop
            elif gender == 'male':
                pop_estimate = age_pop * male_pct
            else:  # female
                pop_estimate = age_pop * female_pct
            
            processed_data.append({
                'location': 'Germany',
                'age_range': age_range,
                'gender': gender,
                'wb_population_estimate': int(pop_estimate),
                'wb_year': latest_year,
                'wb_total_population': int(total_pop),
                'wb_male_percentage': male_pct * 100,
                'wb_female_percentage': female_pct * 100
            })
    
    return pd.DataFrame(processed_data)

def join_with_linkedin_data(wb_df, linkedin_file='linkedin_audience_data.csv'):
    """Join World Bank data with LinkedIn audience data"""
    
    # Load LinkedIn data
    try:
        linkedin_df = pd.read_csv(linkedin_file)
        print(f"Loaded LinkedIn data: {len(linkedin_df)} rows")
    except FileNotFoundError:
        print(f"LinkedIn data file {linkedin_file} not found!")
        return None
    
    # Join the data
    combined_df = linkedin_df.merge(
        wb_df, 
        on=['location', 'age_range', 'gender'], 
        how='left'
    )
    
    # Calculate penetration rates
    combined_df['linkedin_penetration_rate'] = (
        combined_df['audience_count'] / combined_df['wb_population_estimate'] * 100
    ).round(2)
    
    # Add some analysis columns
    combined_df['audience_per_million_population'] = (
        combined_df['audience_count'] / (combined_df['wb_total_population'] / 1_000_000)
    ).round(0)
    
    return combined_df

def main():
    """Main function to download and process all data"""
    
    print("=== World Bank Demographic Data Download ===")
    
    # Download demographic data
    wb_raw_data = download_demographic_data()
    
    if wb_raw_data.empty:
        print("Failed to download World Bank data")
        return
    
    print(f"Downloaded {len(wb_raw_data)} records from World Bank")
    
    # Save raw data
    wb_raw_data.to_csv('wb_demographic_raw.csv', index=False)
    print("Saved raw World Bank data to wb_demographic_raw.csv")
    
    # Process the data
    wb_processed = process_demographic_data(wb_raw_data)
    
    if wb_processed.empty:
        print("Failed to process World Bank data")
        return
    
    print(f"Processed data into {len(wb_processed)} demographic segments")
    
    # Save processed data
    wb_processed.to_csv('wb_demographic_processed.csv', index=False)
    print("Saved processed World Bank data to wb_demographic_processed.csv")
    
    # Join with LinkedIn data
    combined_data = join_with_linkedin_data(wb_processed)
    
    if combined_data is not None:
        # Save combined data
        combined_data.to_csv('combined_linkedin_wb_data.csv', index=False)
        print(f"Saved combined data to combined_linkedin_wb_data.csv ({len(combined_data)} rows)")
        
        # Print some summary statistics
        print("\n=== Summary Statistics ===")
        print(f"Total LinkedIn users in dataset: {combined_data['audience_count'].sum():,}")
        print(f"Estimated Germany population: {combined_data['wb_total_population'].iloc[0]:,}")
        
        # Show penetration rates by language
        print("\n=== LinkedIn Penetration by Language (All ages, All genders) ===")
        summary = combined_data[
            (combined_data['age_range'] == 'All ages') & 
            (combined_data['gender'] == 'All genders')
        ][['language', 'audience_count', 'linkedin_penetration_rate']].sort_values('audience_count', ascending=False)
        
        for _, row in summary.iterrows():
            print(f"{row['language']}: {row['audience_count']:,} users ({row['linkedin_penetration_rate']:.2f}% penetration)")
    
    print("\n=== Available demographic indicators ===")
    print("Searching for additional demographic indicators...")
    demographic_indicators = search_demographic_indicators()
    
    print(f"\nFound {len(demographic_indicators)} demographic-related indicators:")
    for i, indicator in enumerate(demographic_indicators[:10]):  # Show first 10
        print(f"{i+1}. {indicator['id']}: {indicator['name']}")
    
    if len(demographic_indicators) > 10:
        print(f"... and {len(demographic_indicators) - 10} more")

if __name__ == "__main__":
    main()
