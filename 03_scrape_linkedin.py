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
    'bcookie': '"v=2&d06e9ab1-c3e1-4868-8b12-3d23f7bcb447"',
    'li_gc': 'MTswOzE3NTc0MjIwMjY7MjswMjHWQzHrLECT1t7ZlxcdU+AU4xuUIhllV4i724HdcwELyg==',
    'bscookie': '"v=1&20250909124710ebeeffed-5459-4ae8-8fa4-ae671088a6f6AQHQ6AefMiXzOVPs1yIIzATD8xFxlNDj"',
    'li_alerts': 'e30=',
    'li_rm': 'AQGJVYdDBWIzCAAAAZkuhHnbNIdMox_jews8Thqb_AzFkr88ARsh0vmvHrMVtWKmFJbwodBHTt3BtvKGjsBQr0yMH4YzCvD3gf9tspHR9xtzX2eYOWUGuzLu',
    'li_at': 'AQEDAS3W8qAFt6BVAAABmS6FVTYAAAGZUpHZNk0Aob2aJWWHvU7D34xMmlOBzVjFe78ohjruK5xRjD7lEoY_lzcMXJ6PL5ZRThYV3rmQp2DaNLutDfo9jM-BFm1gDVtUQA9_I6DHhjyYOqP4YgKacpI0',
    'liap': 'true',
    'JSESSIONID': '"ajax:7096641885251446497"',
    'timezone': 'Europe/Berlin',
    'li_theme': 'light',
    'li_theme_set': 'app',
    'dfpfpt': '733a4eafecb446dcaab9a503417f47f2',
    'lidc': '"b=TB36:s=T:r=T:a=V:p=T:g=22254:u=662:x=1:i=1757422941:t=1757509341:v=2:sig=AQHHNjtoLoyfDA1Ht1yNQjWuncwRyTdk"',
    'PLAY_LANG': 'en',
    'lang': 'v=2&lang=en-US',
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVshdOy7P1490jg04nCmvXBEfjwO%252fLyXNStYvTSwCtrlwaOkaZjWUivxh%252fgUJ%252bco0Ah1vTdSmdQRp1WspX6R8OaRU%252bM0AVAR6W%252bnhC818RjyijixC1x4OqaL9BUkIyqI0h5uBDRkynEdvpl1DcRAwpn5B%252fjE%252bcxdGjea91LjEPTC4uprURw3rYzOJJCxftE8pHYZjNkRU%252fCShajOjxFt%252bKXQ7VKjo%252bMIS7FPWq1JxK2tCtqZLjggYZ0n%252frKHWVPxeerhacmTgjJn1ZD8sl9TTa%252fCnQs%252f3SQ1AGEEvH9DusKtklps2bpU%252fE4h1ZKxnF54m9c%253d',
    '__cf_bm': 'OeCpRxKt4vMxSHGa11AVJBYta2RBniCzSI9eNXBAnf8-1757504999-1.0.1.1-spIvlnNaeNwhUqk4yaQ9fz7zezYhXkuWWPzXFw2QTl6MWvvZsWC6F0l04oiC46zxiqkY07DW.kyDNnqAmw7PV3IKT9ksUpKS3OhFwMuhAro',
    'li_mc': 'MTs0MjsxNzU3NTA1NDU2OzI7MDIxH685ItSNUWU9w9ROVGBsvUuz+YrKzZSPBQb/ERakk/8=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en,de;q=0.9,de-DE;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'csrf-token': 'ajax:7096641885251446497',
    'origin': 'https://www.linkedin.com',
    'priority': 'u=1, i',
    'referer': 'https://www.linkedin.com/campaignmanager/accounts/503555724/campaigns/new/details?businessId=personal&campaignGroupId=768047403&initialObjectiveType=WEBSITE_VISIT',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
    'x-http-method-override': 'GET',
    'x-li-er-key': 'urn:li:sponsoredAccount:503555724',
    'x-li-lang': 'en_US',
    'x-li-page-instance': 'urn:li:page:d_campaign_details;0L/XjNrMTFiKzve0wIw5nw==',
    'x-li-track': '{"clientVersion":"2.33.1798","mpVersion":"2.33.1798","osName":"web","timezoneOffset":2,"timezone":"Europe/Berlin","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":1.875,"displayWidth":3200.625,"displayHeight":2000.625}',
    'x-restli-protocol-version': '2.0.0',
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
# To collect all combinations and save to CSV, uncomment and run:
results = collect_all_combinations_with_cache(cookies, headers)

# %%
# To test a single request:
result = get_audience_count(cookies, headers, "Germany", "35-54", "female", "French")
print(f"Audience count: {result}")

# %%
