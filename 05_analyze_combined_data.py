#%%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_combined_data():
    """Analyze the combined LinkedIn and World Bank data"""
    
    # Load the combined data
    df = pd.read_csv('combined_linkedin_wb_data.csv')
    
    print("=== Combined LinkedIn + World Bank Data Analysis ===")
    print(f"Total records: {len(df)}")
    print(f"Date: World Bank data from {df['wb_year'].iloc[0]}")
    print(f"Germany population: {df['wb_total_population'].iloc[0]:,}")
    
    # 1. LinkedIn penetration by language
    print("\n=== LinkedIn Penetration by Language (All Demographics) ===")
    all_ages_all_genders = df[(df['age_range'] == 'All ages') & (df['gender'] == 'All genders')]
    
    language_analysis = all_ages_all_genders[['language', 'audience_count', 'linkedin_penetration_rate']].copy()
    language_analysis = language_analysis.sort_values('audience_count', ascending=False)
    
    for _, row in language_analysis.iterrows():
        print(f"{row['language']:8}: {row['audience_count']:>9,} LinkedIn users ({row['linkedin_penetration_rate']:>5.2f}% of population)")
    
    # 2. Gender distribution analysis
    print("\n=== Gender Distribution Analysis ===")
    print("LinkedIn vs Population gender distribution:")
    
    # Calculate total LinkedIn users by gender
    male_linkedin = df[(df['age_range'] == 'All ages') & (df['gender'] == 'male')]['audience_count'].sum()
    female_linkedin = df[(df['age_range'] == 'All ages') & (df['gender'] == 'female')]['audience_count'].sum()
    total_linkedin = male_linkedin + female_linkedin
    
    # World Bank gender distribution
    wb_male_pct = df['wb_male_percentage'].iloc[0]
    wb_female_pct = df['wb_female_percentage'].iloc[0]
    
    print(f"Population - Male: {wb_male_pct:.1f}%, Female: {wb_female_pct:.1f}%")
    print(f"LinkedIn   - Male: {male_linkedin/total_linkedin*100:.1f}%, Female: {female_linkedin/total_linkedin*100:.1f}%")
    print(f"LinkedIn representation: Male {male_linkedin:,}, Female {female_linkedin:,}")
    
    # 3. Age group analysis
    print("\n=== Age Group Analysis (English + German users only) ===")
    native_speakers = df[df['language'].isin(['English', 'German']) & (df['gender'] == 'All genders')]
    
    age_analysis = native_speakers.groupby('age_range').agg({
        'audience_count': 'sum',
        'wb_population_estimate': 'first',
        'linkedin_penetration_rate': 'mean'
    }).round(2)
    
    # Reorder age groups logically
    age_order = ['18-24', '25-34', '35-54', '55+', 'All ages']
    age_analysis = age_analysis.reindex(age_order)
    
    for age_range, row in age_analysis.iterrows():
        if age_range != 'All ages':  # Skip 'All ages' as it's the sum
            print(f"{age_range:>6}: {row['audience_count']:>9,} LinkedIn users, "
                  f"penetration: {row['linkedin_penetration_rate']:>5.2f}%")
    
    # 4. Language-specific insights
    print("\n=== Language-Specific Insights ===")
    
    # Focus on non-German/English languages to understand expat communities
    foreign_languages = df[~df['language'].isin(['German', 'English']) & 
                          (df['age_range'] == 'All ages') & 
                          (df['gender'] == 'All genders')]
    
    print("Foreign language LinkedIn communities in Germany:")
    for _, row in foreign_languages.sort_values('audience_count', ascending=False).iterrows():
        # Estimate what percentage of total foreign population this might represent
        print(f"{row['language']:8}: {row['audience_count']:>6,} users ({row['linkedin_penetration_rate']:.2f}% of total population)")
    
    # 5. Professional networking insights
    print("\n=== Professional Networking Insights ===")
    
    # Working-age population analysis (25-54)
    working_age = df[df['age_range'].isin(['25-34', '35-54']) & 
                    (df['gender'] == 'All genders') &
                    df['language'].isin(['English', 'German'])]
    
    working_age_summary = working_age.groupby('language').agg({
        'audience_count': 'sum',
        'wb_population_estimate': 'sum',
        'linkedin_penetration_rate': 'mean'
    }).round(2)
    
    print("LinkedIn penetration in working-age population (25-54):")
    for language, row in working_age_summary.iterrows():
        print(f"{language}: {row['linkedin_penetration_rate']:.1f}% penetration")
    
    # 6. International community analysis
    print("\n=== International Community Analysis ===")
    
    # Compare different languages across age groups for gender-neutral data
    international_df = df[(df['gender'] == 'All genders') & 
                         (~df['language'].isin(['German'])) &
                         (df['age_range'] != 'All ages')]
    
    intl_pivot = international_df.pivot_table(
        index='language', 
        columns='age_range', 
        values='audience_count',
        fill_value=0
    )
    
    # Reorder columns
    age_cols = ['18-24', '25-34', '35-54', '55+']
    intl_pivot = intl_pivot.reindex(columns=age_cols)
    
    print("International LinkedIn users by age group:")
    print(intl_pivot.to_string())
    
    # Calculate total international LinkedIn community
    total_international = df[~df['language'].isin(['German']) & 
                           (df['age_range'] == 'All ages') & 
                           (df['gender'] == 'All genders')]['audience_count'].sum()
    
    total_german = df[(df['language'] == 'German') & 
                     (df['age_range'] == 'All ages') & 
                     (df['gender'] == 'All genders')]['audience_count'].iloc[0]
    
    print(f"\nTotal international LinkedIn community: {total_international:,}")
    print(f"Total German LinkedIn community: {total_german:,}")
    print(f"International share: {total_international/(total_international+total_german)*100:.1f}%")
    
    return df
#%%
def create_visualizations(df):
    """Create visualizations of the data"""
    
    # Set up the plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('LinkedIn Demographics in Germany vs World Bank Data', fontsize=16)
    
    # 1. Language penetration (All ages, All genders)
    all_demo = df[(df['age_range'] == 'All ages') & (df['gender'] == 'All genders')]
    
    axes[0,0].bar(all_demo['language'], all_demo['linkedin_penetration_rate'])
    axes[0,0].set_title('LinkedIn Penetration Rate by Language')
    axes[0,0].set_ylabel('Penetration Rate (%)')
    axes[0,0].set_yscale('log')
    axes[0,0].tick_params(axis='x', rotation=45)
    
    # 2. Gender balance by age group (stacked percentage bars)
    gender_age_data = df[(df['gender'] != 'All genders') & 
                        (df['age_range'] != 'All ages')]
    
    # Group by age and language, then calculate gender percentages
    gender_age_pivot = gender_age_data.groupby(['age_range', 'language', 'gender'])['audience_count'].sum().unstack('gender', fill_value=0)
    
    # Calculate percentages for each age/language group
    gender_age_pct = gender_age_pivot.div(gender_age_pivot.sum(axis=1), axis=0) * 100
    
    # Reorganize index to group by age first, then language
    age_order = ['18-24', '25-34', '35-54', '55+']
    new_index = []
    for age in age_order:
        for lang in sorted(gender_age_pct.index.get_level_values(1).unique()):
            if (age, lang) in gender_age_pct.index:
                new_index.append((age, lang))
    
    gender_age_pct = gender_age_pct.reindex(new_index)
    gender_age_pct.index = [f"{age}\n{lang}" for age, lang in gender_age_pct.index]
    
    gender_age_pct.plot(kind='bar', ax=axes[0,1], stacked=True, 
                       color=['lightblue', 'lightcoral'], width=0.8)
    axes[0,1].set_title('LinkedIn Gender Balance by Age Group and Language')
    axes[0,1].set_ylabel('Percentage (%)')
    axes[0,1].set_ylim(0, 100)
    axes[0,1].tick_params(axis='x', rotation=45)
    axes[0,1].legend(title='Gender')
    
    # Add vertical lines to separate age groups
    age_breaks = []
    current_age = None
    for i, (age, lang) in enumerate(new_index):
        if current_age and age != current_age:
            age_breaks.append(i - 0.5)
        current_age = age
    
    for break_pos in age_breaks:
        axes[0,1].axvline(x=break_pos, color='gray', linestyle='-', alpha=0.3, linewidth=1)
    
    # 3. Gender balance by language (stacked percentage bars)
    gender_lang_data = df[(df['age_range'] == 'All ages') & 
                         (df['gender'] != 'All genders')]
    
    gender_lang_pivot = gender_lang_data.pivot_table(index='language', columns='gender', values='audience_count')
    
    # Calculate percentages for each language
    gender_lang_pct = gender_lang_pivot.div(gender_lang_pivot.sum(axis=1), axis=0) * 100
    
    gender_lang_pct.plot(kind='bar', ax=axes[1,0], stacked=True,
                        color=['lightblue', 'lightcoral'])
    axes[1,0].set_title('LinkedIn Gender Balance by Language')
    axes[1,0].set_ylabel('Percentage (%)')
    axes[1,0].set_ylim(0, 100)
    axes[1,0].tick_params(axis='x', rotation=45)
    axes[1,0].legend(title='Gender')
    
    # 4. World Bank Gender Balance by Language
    # Show World Bank population gender distribution (same for all languages in Germany)
    wb_male_pct = df['wb_male_percentage'].iloc[0]
    wb_female_pct = df['wb_female_percentage'].iloc[0]
    
    # Get unique languages from the data
    languages = df['language'].unique()
    
    # Create World Bank gender data for each language (same values since it's national data)
    wb_gender_data = pd.DataFrame({
        'male': [wb_male_pct] * len(languages),
        'female': [wb_female_pct] * len(languages)
    }, index=languages)
    
    wb_gender_data.plot(kind='bar', ax=axes[1,1], stacked=True,
                       color=['lightblue', 'lightcoral'])
    axes[1,1].set_title('World Bank Population Gender Balance by Language')
    axes[1,1].set_ylabel('Percentage (%)')
    axes[1,1].set_ylim(0, 100)
    axes[1,1].tick_params(axis='x', rotation=45)
    axes[1,1].legend(title='Gender')
    
    # Add reference line at 50%
    axes[1,1].axhline(y=50, color='gray', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('linkedin_demographics_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Visualization saved as 'linkedin_demographics_analysis.png'")

if __name__ == "__main__":
    df = analyze_combined_data()
    
    # Uncomment to create visualizations (requires matplotlib)
    create_visualizations(df)
#%%