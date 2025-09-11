#%%
# The following syntax allows you to install packages directly from a Jupyter notebook cell.
# If you're running this code outside of a Jupyter notebook, you should install the packages using
%pip install requests
#%%
import requests
import json

#%%
cookies = {
    ... please replace this with your own cookies ...
}

headers = {
    ... please replace this with your own headers ...
}


#%%
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List((urn:urn%3Ali%3AageRange%3A%2835%2C54%29,name:35%20to%2054,facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Ait_IT,name:Italian,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
response = requests.post(
    'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
    cookies=cookies,
    headers=headers,
    data=data,
)
# %%
print(response.status_code) # 200
response_data = response.json() # {'elements': [{'count': 3200, 'allowCampaignActivation': True, 'includesDynamicFacets': False}], 'paging': {'count': 10, 'start': 0, 'links': []}}

# Extract the audience count
audience_count = response_data['elements'][0]['count']
print(f"Audience count: {audience_count}")
# %%

# new targeting criteria: French language instead of Italian
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List((urn:urn%3Ali%3AageRange%3A%2835%2C54%29,name:35%20to%2054,facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# new targeting criteria: age range 18-24 instead of 35-54
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List((urn:urn%3Ali%3AageRange%3A%2825%2C34%29,name:25%20to%2034,facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# new targeting criteria: age range 18-24 instead of 35-54
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List((urn:urn%3Ali%3AageRange%3A%2818%2C24%29,name:18%20to%2024,facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# 55+ age range:
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List((urn:urn%3Ali%3AageRange%3A%2855%2C2147483647%29,name:55%2B,facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# no age restriction, only location and language
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# gender = female
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AFEMALE,name:Female,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# gender = male
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AMALE,name:Male,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AMALE,name:Male,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Afr_FR,name:French,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%
# language = Spanish
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List((urn:urn%3Ali%3Alocale%3Aes_ES,name:Spanish,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales))))))),exclude:(or:List()))&withValidation=true'
#%%

# After gathering all the example requests from above, "back in the day",
# I would have tried to figure out how to generate these requests.
# Nowadays, let's ask AI to help us with that:

#Prompt:

# We collected several example requests with different targeting criteria in this file.
# Please write a Python function that takes as input the location (e.g. "Germany"),
# age range (e.g. "18-24", "25-34", "35-54", "55+"),
# gender (e.g. "male", "female"), and language (e.g. "French", "Spanish"),
# and returns the corresponding targeting criteria string.
# Please use the same format as in the example requests above. Think hard about
# how these requests are constructed, and make sure to cover all possible input values.

# Then also write code that uses this function to get the audience count for all combinations
# and saves the results in a CSV file.

# It would be great if requests could be cached, so that we don't have to repeat requests for the same criteria.
#file:03_scrape_linkedin.py

import csv
import hashlib
import os
from urllib.parse import quote

#%%
# Mapping dictionaries for targeting criteria
LOCATION_MAPPING = {
    "Germany": "urn:urn%3Ali%3Ageo%3A101282230"
}

AGE_RANGE_MAPPING = {
    "18-24": "urn:urn%3Ali%3AageRange%3A%2818%2C24%29",
    "25-34": "urn:urn%3Ali%3AageRange%3A%2825%2C34%29", 
    "35-54": "urn:urn%3Ali%3AageRange%3A%2835%2C54%29",
    "55+": "urn:urn%3Ali%3AageRange%3A%2855%2C2147483647%29"
}

GENDER_MAPPING = {
    "male": "urn:urn%3Ali%3Agender%3AMALE",
    "female": "urn:urn%3Ali%3Agender%3AFEMALE"
}

LANGUAGE_MAPPING = {
    "Italian": "urn:urn%3Ali%3Alocale%3Ait_IT",
    "French": "urn:urn%3Ali%3Alocale%3Afr_FR", 
    "Spanish": "urn:urn%3Ali%3Alocale%3Aes_ES",
    "English": "urn:urn%3Ali%3Alocale%3Aen_US",
    "German": "urn:urn%3Ali%3Alocale%3Ade_DE"
}

def generate_targeting_criteria(location=None, age_range=None, gender=None, language=None):
    """
    Generate LinkedIn targeting criteria string based on input parameters.
    
    Args:
        location (str): Location name (e.g., "Germany")
        age_range (str): Age range (e.g., "18-24", "25-34", "35-54", "55+")
        gender (str): Gender ("male", "female")
        language (str): Language (e.g., "French", "Spanish", "Italian", "English", "German")
    
    Returns:
        str: URL-encoded targeting criteria string
    """
    criteria_parts = []
    
    # Add location criteria (required)
    if location and location in LOCATION_MAPPING:
        location_urn = LOCATION_MAPPING[location]
        location_criteria = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List(({location_urn},name:{location},facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914))))))"
        criteria_parts.append(location_criteria)
    
    # Add age range criteria
    if age_range and age_range in AGE_RANGE_MAPPING:
        age_urn = AGE_RANGE_MAPPING[age_range]
        age_display = age_range.replace("+", "%2B")
        age_criteria = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List(({age_urn},name:{age_display},facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges)))))"
        criteria_parts.append(age_criteria)
    
    # Add gender criteria
    if gender and gender in GENDER_MAPPING:
        gender_urn = GENDER_MAPPING[gender]
        gender_display = gender.capitalize()
        gender_criteria = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List(({gender_urn},name:{gender_display},facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders)))))"
        criteria_parts.append(gender_criteria)
    
    # Add language criteria
    if language and language in LANGUAGE_MAPPING:
        language_urn = LANGUAGE_MAPPING[language]
        language_criteria = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List(({language_urn},name:{language},facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales)))))"
        criteria_parts.append(language_criteria)
    
    # Join all criteria parts
    if criteria_parts:
        criteria_string = ",".join(criteria_parts)
        full_criteria = f"q=targetingCriteria&cmTargetingCriteria=(include:(and:List({criteria_string})),exclude:(or:List()))&withValidation=true"
        return full_criteria
    else:
        return None

# Cache functionality
CACHE_FILE = "linkedin_audience_cache.json"

def get_cache():
    """Load cache from file"""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache):
    """Save cache to file"""
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def get_cache_key(location, age_range, gender, language):
    """Generate a unique cache key for the parameters"""
    key_data = f"{location}_{age_range}_{gender}_{language}"
    return hashlib.md5(key_data.encode()).hexdigest()

def get_audience_count(location=None, age_range=None, gender=None, language=None, use_cache=True):
    """
    Get audience count for given targeting criteria with caching support.
    """
    # Check cache first
    cache_key = get_cache_key(location, age_range, gender, language)
    cache = get_cache() if use_cache else {}
    
    if use_cache and cache_key in cache:
        print(f"Cache hit for {location}, {age_range}, {gender}, {language}")
        return cache[cache_key]
    
    # Generate targeting criteria
    data = generate_targeting_criteria(location, age_range, gender, language)
    if not data:
        return None
    
    try:
        # Make the request
        response = requests.post(
            'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        
        if response.status_code == 200:
            response_data = response.json()
            audience_count = response_data['elements'][0]['count']
            
            # Cache the result
            if use_cache:
                cache[cache_key] = audience_count
                save_cache(cache)
            
            return audience_count
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error making request: {e}")
        return None

def generate_all_combinations_csv(filename="linkedin_audience_data.csv"):
    """
    Generate audience counts for all combinations and save to CSV.
    """
    # Define all possible values
    locations = ["Germany"]
    age_ranges = [None, "18-24", "25-34", "35-54", "55+"]
    genders = [None, "male", "female"]
    languages = ["French", "Spanish", "Italian", "English", "German"]
    
    results = []
    total_combinations = len(locations) * len(age_ranges) * len(genders) * len(languages)
    current = 0
    
    print(f"Processing {total_combinations} combinations...")
    
    for location in locations:
        for age_range in age_ranges:
            for gender in genders:
                for language in languages:
                    current += 1
                    print(f"Processing {current}/{total_combinations}: {location}, {age_range}, {gender}, {language}")
                    
                    count = get_audience_count(location, age_range, gender, language)
                    
                    results.append({
                        'location': location,
                        'age_range': age_range or 'All ages',
                        'gender': gender or 'All genders',
                        'language': language,
                        'audience_count': count
                    })
                    
                    # Small delay to be respectful to the API
                    import time
                    time.sleep(0.5)
    
    # Save to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['location', 'age_range', 'gender', 'language', 'audience_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"Results saved to {filename}")
    return results

# Example usage and testing
if __name__ == "__main__":
    # Test the function with a few examples
    print("Testing targeting criteria generation:")
    
    # Test 1: Location + Age + Language (like your examples)
    criteria1 = generate_targeting_criteria("Germany", "35-54", None, "Italian")
    print("Test 1 - Germany, 35-54, Italian:")
    print(criteria1[:100] + "...")
    
    # Test 2: Location + Gender + Language
    criteria2 = generate_targeting_criteria("Germany", None, "female", "French") 
    print("\nTest 2 - Germany, female, French:")
    print(criteria2[:100] + "...")
    
    # Test 3: All parameters
    criteria3 = generate_targeting_criteria("Germany", "25-34", "male", "Spanish")
    print("\nTest 3 - Germany, 25-34, male, Spanish:")
    print(criteria3[:100] + "...")
    
    # Test a single request to verify it works
    print("\nTesting single audience count request:")
    count = get_audience_count("Germany", "35-54", None, "Italian")
    print(f"Audience count for Germany, 35-54, Italian: {count}")
    
    # Uncomment the line below to generate the full CSV (warning: this will make many API requests!)
    results = generate_all_combinations_csv()
    
    print("\nTo generate the full CSV with all combinations, uncomment the last line and run the script.")
    print("Note: This will make many API requests and may take several minutes to complete.")

#%%
