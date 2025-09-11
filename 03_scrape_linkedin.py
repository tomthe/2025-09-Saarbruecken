#%%
# The following syntax allows you to install packages directly from a Jupyter notebook cell.
# If you're running this code outside of a Jupyter notebook, you should install the packages using pip directly
%pip install requests
#%%
import requests
import json
import urllib.parse
import csv
import pickle
import os
from datetime import datetime
import itertools

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




# Result:

#%%
import urllib.parse
import csv
import pickle
import os
from datetime import datetime
import itertools

# Mapping dictionaries for different targeting criteria
LOCATION_MAP = {
    "Germany": {
        "urn": "urn:urn%3Ali%3Ageo%3A101282230",
        "name": "Germany", 
        "ancestor": "urn%3Ali%3Ageo%3A100506914"
    },
    "Italy": {
        "urn": "urn:urn%3Ali%3Ageo%3A103350119",
        "name": "Italy",
        "ancestor": "urn%3Ali%3Ageo%3A100506914"
    },
    "Denmark": {
        "urn": "urn:urn%3Ali%3Ageo%3A104514075", 
        "name": "Denmark",
        "ancestor": "urn%3Ali%3Ageo%3A100506914"
    }
}

AGE_RANGE_MAP = {
    "18-24": {
        "urn": "urn:urn%3Ali%3AageRange%3A%2818%2C24%29",
        "name": "18%20to%2024"
    },
    "25-34": {
        "urn": "urn:urn%3Ali%3AageRange%3A%2825%2C34%29", 
        "name": "25%20to%2034"
    },
    "35-54": {
        "urn": "urn:urn%3Ali%3AageRange%3A%2835%2C54%29",
        "name": "35%20to%2054"
    },
    "55+": {
        "urn": "urn:urn%3Ali%3AageRange%3A%2855%2C2147483647%29",
        "name": "55%2B"
    }
}
GENDER_MAP = {
    "male": {
        "urn": "urn:urn%3Ali%3Agender%3AMALE",
        "name": "Male"
    },
    "female": {
        "urn": "urn:urn%3Ali%3Agender%3AFEMALE", 
        "name": "Female"
    }
}

LANGUAGE_MAP = {
    "Italian": {
        "urn": "urn:urn%3Ali%3Alocale%3Ait_IT",
        "name": "Italian"
    },
    "French": {
        "urn": "urn:urn%3Ali%3Alocale%3Afr_FR",
        "name": "French"
    },
    "Spanish": {
        "urn": "urn:urn%3Ali%3Alocale%3Aes_ES",
        "name": "Spanish"
    },
    "English": {
        "urn": "urn:urn%3Ali%3Alocale%3Aen_US",
        "name": "English"
    }
}

def build_targeting_criteria(location=None, age_range=None, gender=None, language=None):
    """
    Build LinkedIn targeting criteria string based on input parameters.
    
    Args:
        location (str): Location name (e.g., "Germany", "Italy", "Denmark")
        age_range (str): Age range (e.g., "18-24", "25-34", "35-54", "55+") 
        gender (str): Gender ("male" or "female")
        language (str): Language (e.g., "French", "Spanish", "Italian", "English")
    
    Returns:
        str: URL-encoded targeting criteria string
    """
    criteria_parts = []
    
    # Location targeting (required)
    if location and location in LOCATION_MAP:
        loc_data = LOCATION_MAP[location]
        location_part = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List(({loc_data['urn']},name:{loc_data['name']},facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List({loc_data['ancestor']}))))))"
        criteria_parts.append(location_part)
    
    # Age range targeting (optional)
    if age_range and age_range in AGE_RANGE_MAP:
        age_data = AGE_RANGE_MAP[age_range]
        age_part = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AageRanges,name:Member%20Age),segments:List(({age_data['urn']},name:{age_data['name']},facetUrn:urn%3Ali%3AadTargetingFacet%3AageRanges)))))"
        criteria_parts.append(age_part)
    
    # Gender targeting (optional)
    if gender and gender in GENDER_MAP:
        gender_data = GENDER_MAP[gender]
        gender_part = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List(({gender_data['urn']},name:{gender_data['name']},facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders)))))"
        criteria_parts.append(gender_part)
    
    # Language targeting (optional)
    if language and language in LANGUAGE_MAP:
        lang_data = LANGUAGE_MAP[language]
        language_part = f"(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Profile%20language),segments:List(({lang_data['urn']},name:{lang_data['name']},facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales)))))"
        criteria_parts.append(language_part)
    
    # Combine all criteria parts
    criteria_string = ",".join(criteria_parts)
    
    # Build the full targeting criteria
    full_criteria = f"q=targetingCriteria&cmTargetingCriteria=(include:(and:List({criteria_string})),exclude:(or:List()))&withValidation=true"
    
    return full_criteria

def get_audience_count(cookies, headers, location=None, age_range=None, gender=None, language=None):
    """
    Get LinkedIn audience count for specific targeting criteria.
    
    Returns:
        dict: Response data with audience count or error information
    """
    try:
        data = build_targeting_criteria(location, age_range, gender, language)
        
        response = requests.post(
            'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        
        if response.status_code == 200:
            response_data = response.json()
            if 'elements' in response_data and len(response_data['elements']) > 0:
                return {
                    'success': True,
                    'count': response_data['elements'][0]['count'],
                    'allow_activation': response_data['elements'][0].get('allowCampaignActivation', False)
                }
        
        return {
            'success': False,
            'error': f"HTTP {response.status_code}",
            'response': response.text[:200]  # First 200 chars for debugging
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def collect_all_combinations_with_cache(cookies, headers, cache_file='linkedin_cache.pkl', output_file='linkedin_audience_data.csv'):
    """
    Collect audience counts for all combinations of targeting criteria with caching.
    
    Args:
        cookies (dict): LinkedIn session cookies
        headers (dict): Request headers
        cache_file (str): Path to cache file
        output_file (str): Path to output CSV file
    """
    
    # Load existing cache
    cache = {}
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'rb') as f:
                cache = pickle.load(f)
            print(f"Loaded cache with {len(cache)} entries")
        except:
            print("Could not load cache file, starting fresh")
    
    # Define all possible values
    locations = list(LOCATION_MAP.keys())
    age_ranges = [None] + list(AGE_RANGE_MAP.keys())  # None means no age restriction
    genders = [None, "male", "female"]  # None means no gender restriction
    languages = list(LANGUAGE_MAP.keys())
    
    # Generate all combinations
    all_combinations = list(itertools.product(locations, age_ranges, genders, languages))
    
    results = []
    new_requests = 0
    
    print(f"Processing {len(all_combinations)} combinations...")
    
    for i, (location, age_range, gender, language) in enumerate(all_combinations):
        # Create cache key
        cache_key = (location, age_range, gender, language)
        
        # Check cache first
        if cache_key in cache:
            result = cache[cache_key]
        else:
            # Make API request
            result = get_audience_count(cookies, headers, location, age_range, gender, language)
            cache[cache_key] = result
            new_requests += 1
            
            # Save cache every 10 new requests
            if new_requests % 10 == 0:
                with open(cache_file, 'wb') as f:
                    pickle.dump(cache, f)
                print(f"Progress: {i+1}/{len(all_combinations)} - Cache updated ({new_requests} new requests)")
        
        # Add to results
        row = {
            'location': location,
            'age_range': age_range or 'All',
            'gender': gender or 'All', 
            'language': language,
            'audience_count': result.get('count', 0) if result.get('success') else 0,
            'success': result.get('success', False),
            'error': result.get('error', ''),
            'timestamp': datetime.now().isoformat()
        }
        results.append(row)
    
    # Save final cache
    with open(cache_file, 'wb') as f:
        pickle.dump(cache, f)
    
    # Save results to CSV
    if results:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        
        print(f"Results saved to {output_file}")
        print(f"Total combinations: {len(results)}")
        print(f"New API requests made: {new_requests}")
        print(f"Successful requests: {sum(1 for r in results if r['success'])}")
    
    return results

# Example usage and test
def test_targeting_function():
    """Test the targeting criteria function with some examples"""
    
    # Test case 1: Germany, 35-54, French
    criteria1 = build_targeting_criteria("Germany", "35-54", None, "French")
    print("Test 1 - Germany, 35-54, French:")
    print(criteria1[:100] + "...")
    
    # Test case 2: Germany, female, French  
    criteria2 = build_targeting_criteria("Germany", None, "female", "French")
    print("\nTest 2 - Germany, female, French:")
    print(criteria2[:100] + "...")
    
    # Test case 3: Germany, Spanish (no age/gender)
    criteria3 = build_targeting_criteria("Germany", None, None, "Spanish")
    print("\nTest 3 - Germany, Spanish:")
    print(criteria3[:100] + "...")

# %%
# Test the functions
test_targeting_function()

# %%
# To collect all combinations and save to CSV_
results = collect_all_combinations_with_cache(cookies, headers)

# %%
# To test a single request:
result = get_audience_count(cookies, headers, "Germany", "35-54", "female", "French")
print(f"Audience count: {result}")
