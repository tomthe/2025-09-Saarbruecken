#%%
import requests

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
    # 'cookie': 'bcookie="v=2&d06e9ab1-c3e1-4868-8b12-3d23f7bcb447"; li_gc=MTswOzE3NTc0MjIwMjY7MjswMjHWQzHrLECT1t7ZlxcdU+AU4xuUIhllV4i724HdcwELyg==; bscookie="v=1&20250909124710ebeeffed-5459-4ae8-8fa4-ae671088a6f6AQHQ6AefMiXzOVPs1yIIzATD8xFxlNDj"; li_alerts=e30=; li_rm=AQGJVYdDBWIzCAAAAZkuhHnbNIdMox_jews8Thqb_AzFkr88ARsh0vmvHrMVtWKmFJbwodBHTt3BtvKGjsBQr0yMH4YzCvD3gf9tspHR9xtzX2eYOWUGuzLu; li_at=AQEDAS3W8qAFt6BVAAABmS6FVTYAAAGZUpHZNk0Aob2aJWWHvU7D34xMmlOBzVjFe78ohjruK5xRjD7lEoY_lzcMXJ6PL5ZRThYV3rmQp2DaNLutDfo9jM-BFm1gDVtUQA9_I6DHhjyYOqP4YgKacpI0; liap=true; JSESSIONID="ajax:7096641885251446497"; timezone=Europe/Berlin; li_theme=light; li_theme_set=app; dfpfpt=733a4eafecb446dcaab9a503417f47f2; lidc="b=TB36:s=T:r=T:a=V:p=T:g=22254:u=662:x=1:i=1757422941:t=1757509341:v=2:sig=AQHHNjtoLoyfDA1Ht1yNQjWuncwRyTdk"; PLAY_LANG=en; lang=v=2&lang=en-US; fptctx2=taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVshdOy7P1490jg04nCmvXBEfjwO%252fLyXNStYvTSwCtrlwaOkaZjWUivxh%252fgUJ%252bco0Ah1vTdSmdQRp1WspX6R8OaRU%252bM0AVAR6W%252bnhC818RjyijixC1x4OqaL9BUkIyqI0h5uBDRkynEdvpl1DcRAwpn5B%252fjE%252bcxdGjea91LjEPTC4uprURw3rYzOJJCxftE8pHYZjNkRU%252fCShajOjxFt%252bKXQ7VKjo%252bMIS7FPWq1JxK2tCtqZLjggYZ0n%252frKHWVPxeerhacmTgjJn1ZD8sl9TTa%252fCnQs%252f3SQ1AGEEvH9DusKtklps2bpU%252fE4h1ZKxnF54m9c%253d; __cf_bm=OeCpRxKt4vMxSHGa11AVJBYta2RBniCzSI9eNXBAnf8-1757504999-1.0.1.1-spIvlnNaeNwhUqk4yaQ9fz7zezYhXkuWWPzXFw2QTl6MWvvZsWC6F0l04oiC46zxiqkY07DW.kyDNnqAmw7PV3IKT9ksUpKS3OhFwMuhAro; li_mc=MTs0MjsxNzU3NTA1NDU2OzI7MDIxH685ItSNUWU9w9ROVGBsvUuz+YrKzZSPBQb/ERakk/8=',
}

data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,ancestorUrns:List()))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A103350119,name:Italy,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))))),exclude:(or:List()))&withValidation=true'
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,ancestorUrns:List()))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A104514075,name:Denmark,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))))),exclude:(or:List()))&withValidation=true'
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,ancestorUrns:List()))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))))),exclude:(or:List()))&withValidation=true'
#Female:
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,ancestorUrns:List()))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AFEMALE,name:Female,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))))),exclude:(or:List()))&withValidation=true'
#Male:
data = 'q=targetingCriteria&cmTargetingCriteria=(include:(and:List((or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,name:Interface%20Locales),segments:List((urn:urn%3Ali%3Alocale%3Aen_US,name:English,facetUrn:urn%3Ali%3AadTargetingFacet%3AinterfaceLocales,ancestorUrns:List()))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Agenders,name:Member%20Gender),segments:List((urn:urn%3Ali%3Agender%3AMALE,name:Male,facetUrn:urn%3Ali%3AadTargetingFacet%3Agenders))))),(or:List((facet:(urn:urn%3Ali%3AadTargetingFacet%3Alocations,name:Locations),segments:List((urn:urn%3Ali%3Ageo%3A101282230,name:Germany,facetUrn:urn%3Ali%3AadTargetingFacet%3Alocations,ancestorUrns:List(urn%3Ali%3Ageo%3A100506914)))))))),exclude:(or:List()))&withValidation=true'
#female:
#%%



response = requests.post(
    'https://www.linkedin.com/campaign-manager-api/campaignManagerAudienceCounts',
    cookies=cookies,
    headers=headers,
    data=data,
)

# %%
print(response.status_code) # 200
response_data = response.json() # {'elements': [{'count': 3200, 'allow
# %%
response_data
# %%
