#%%
# The following syntax allows you to install packages directly from a Jupyter notebook cell.
# If you're running this code outside of a Jupyter notebook, you should install the packages using
%pip install requests
#%%
import requests
import json

#%%
cookies = {
    # replace with your cookies from curlconverter....
}

headers = {
    # replace with your headers from curlconverter....
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
# We need a good prompt!

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

# %%
