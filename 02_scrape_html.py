#%%
%pip install requests beautifulsoup4
#%%
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    """Extract all headlines from a webpage"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [tag.get_text(strip=True) for tag in soup.find_all(['h1','h2','h3','h4','h5','h6']) if tag.get_text(strip=True)]
    return headlines

# Usage
url = 'https://example.com'
headlines = scrape_headlines(url)

# Display results
print(f"Found {len(headlines)} headlines from {url}:")
for i, headline in enumerate(headlines, 1):
    print(f"{i}. {headline}")