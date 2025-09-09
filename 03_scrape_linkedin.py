#%%
# The following syntax allows you to install packages directly from a Jupyter notebook cell.
# If you're running this code outside of a Jupyter notebook, you should install the packages using
%pip install requests
#%%
import requests
import json

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
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVshdOy7P1490jg04nCmvXBEfjwO%252fLyXNStYvTSwCtrlwaOkaZjWUivxh%252fgUJ%252bco0Ah1vTdSmdQRp1WspX6R8OaRU%252bM0AVAR6W%252bnhC818RjyijSHIB5QeMGsYSzCG3Y5jXTPauXRFXyzle%252f2NP3jakfaMzDAYaS7RmsIY6wPaD%252b0KbRhNr2JGbaqdwrKcZZdy2i1O3Ws%252bYANgbZ3hdyH%252blfapq0yArf6kmuKGU2tPd1jOelsHMeik95tYP7zsT22fAftGZ8MqE7dkmtpHAuVcl3XHDkVxce%252b7gH1LnXW06ZAH1UY9%252bRo15ZDmWOqpj3Y1F4%253d',
    'PLAY_LANG': 'en',
    'lang': 'v=2&lang=en-US',
    'lidc': '"b=TB36:s=T:r=T:a=V:p=T:g=22254:u=662:x=1:i=1757422941:t=1757509341:v=2:sig=AQHHNjtoLoyfDA1Ht1yNQjWuncwRyTdk"',
    'li_mc': 'MTs0MjsxNzU3NDI0NjQ3OzI7MDIxcIF6XwUPKBg11xraD4iMnRpYw8jC7nmci5diV31SQDE=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en,de;q=0.9,de-DE;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'csrf-token': 'ajax:7096641885251446497',
    'origin': 'https://www.linkedin.com',
    'priority': 'u=1, i',
    'referer': 'https://www.linkedin.com/campaignmanager/accounts/503555724/campaigns/new/details?businessId=personal&campaignGroupId=768164513&initialObjectiveType=WEBSITE_VISIT',
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
    'x-li-page-instance': 'urn:li:page:d_campaign_details;XAJGPtdeRAeg6ed4+QaSqw==',
    'x-li-track': '{"clientVersion":"2.33.1754","mpVersion":"2.33.1754","osName":"web","timezoneOffset":2,"timezone":"Europe/Berlin","deviceFormFactor":"DESKTOP","mpName":"campaign-manager-web","displayDensity":1.5,"displayWidth":2560.5,"displayHeight":1600.5}',
    'x-restli-protocol-version': '2.0.0',
    # 'cookie': 'bcookie="v=2&d06e9ab1-c3e1-4868-8b12-3d23f7bcb447"; li_gc=MTswOzE3NTc0MjIwMjY7MjswMjHWQzHrLECT1t7ZlxcdU+AU4xuUIhllV4i724HdcwELyg==; bscookie="v=1&20250909124710ebeeffed-5459-4ae8-8fa4-ae671088a6f6AQHQ6AefMiXzOVPs1yIIzATD8xFxlNDj"; li_alerts=e30=; li_rm=AQGJVYdDBWIzCAAAAZkuhHnbNIdMox_jews8Thqb_AzFkr88ARsh0vmvHrMVtWKmFJbwodBHTt3BtvKGjsBQr0yMH4YzCvD3gf9tspHR9xtzX2eYOWUGuzLu; li_at=AQEDAS3W8qAFt6BVAAABmS6FVTYAAAGZUpHZNk0Aob2aJWWHvU7D34xMmlOBzVjFe78ohjruK5xRjD7lEoY_lzcMXJ6PL5ZRThYV3rmQp2DaNLutDfo9jM-BFm1gDVtUQA9_I6DHhjyYOqP4YgKacpI0; liap=true; JSESSIONID="ajax:7096641885251446497"; timezone=Europe/Berlin; li_theme=light; li_theme_set=app; dfpfpt=733a4eafecb446dcaab9a503417f47f2; fptctx2=taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVshdOy7P1490jg04nCmvXBEfjwO%252fLyXNStYvTSwCtrlwaOkaZjWUivxh%252fgUJ%252bco0Ah1vTdSmdQRp1WspX6R8OaRU%252bM0AVAR6W%252bnhC818RjyijSHIB5QeMGsYSzCG3Y5jXTPauXRFXyzle%252f2NP3jakfaMzDAYaS7RmsIY6wPaD%252b0KbRhNr2JGbaqdwrKcZZdy2i1O3Ws%252bYANgbZ3hdyH%252blfapq0yArf6kmuKGU2tPd1jOelsHMeik95tYP7zsT22fAftGZ8MqE7dkmtpHAuVcl3XHDkVxce%252b7gH1LnXW06ZAH1UY9%252bRo15ZDmWOqpj3Y1F4%253d; PLAY_LANG=en; lang=v=2&lang=en-US; lidc="b=TB36:s=T:r=T:a=V:p=T:g=22254:u=662:x=1:i=1757422941:t=1757509341:v=2:sig=AQHHNjtoLoyfDA1Ht1yNQjWuncwRyTdk"; li_mc=MTs0MjsxNzU3NDI0NjQ3OzI7MDIxcIF6XwUPKBg11xraD4iMnRpYw8jC7nmci5diV31SQDE=',
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
