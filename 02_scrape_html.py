#%%
%pip install requests beautifulsoup4
#%%
import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin, urlparse
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def scrape_headlines_from_url(url):
    """
    Scrape headlines from a given URL
    
    Args:
        url (str): The URL to scrape headlines from
        
    Returns:
        list: List of dictionaries containing headline data
    """
    headlines = []
    
    try:
        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Common headline selectors (h1, h2, h3, h4, h5, h6)
        headline_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        
        for tag in headline_tags:
            elements = soup.find_all(tag)
            for element in elements:
                headline_text = element.get_text(strip=True)
                if headline_text:  # Only add non-empty headlines
                    headlines.append({
                        'url': url,
                        'tag': tag,
                        'headline': headline_text,
                        'timestamp': datetime.now().isoformat()
                    })
        
        logger.info(f"Found {len(headlines)} headlines from {url}")
        
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
    except Exception as e:
        logger.error(f"Error parsing content from {url}: {e}")
    
    return headlines

def save_headlines_to_csv(headlines, filename='headlines.csv'):
    """
    Save headlines to a CSV file
    
    Args:
        headlines (list): List of headline dictionaries
        filename (str): Output CSV filename
    """
    if not headlines:
        logger.warning("No headlines to save")
        return
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['url', 'tag', 'headline', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for headline in headlines:
                writer.writerow(headline)
        
        logger.info(f"Saved {len(headlines)} headlines to {filename}")
        
    except Exception as e:
        logger.error(f"Error saving to CSV: {e}")

def scrape_example_com():
    """
    Main function to scrape headlines from example.com
    """
    url = "https://example.com"
    
    logger.info(f"Starting to scrape headlines from {url}")
    
    # Scrape headlines
    headlines = scrape_headlines_from_url(url)
    
    if headlines:
        # Save to CSV
        output_filename = 'example_com_headlines.csv'
        save_headlines_to_csv(headlines, output_filename)
        
        # Print summary
        print(f"\nScraping completed!")
        print(f"Total headlines found: {len(headlines)}")
        print(f"Headlines saved to: {output_filename}")
        
        # Show first few headlines as preview
        print("\nPreview of headlines:")
        for i, headline in enumerate(headlines[:5], 1):
            print(f"{i}. [{headline['tag'].upper()}] {headline['headline']}")
        
        if len(headlines) > 5:
            print(f"... and {len(headlines) - 5} more headlines")
    else:
        print("No headlines found or error occurred during scraping")

def scrape_multiple_pages(urls):
    """
    Scrape headlines from multiple URLs
    
    Args:
        urls (list): List of URLs to scrape
    """
    all_headlines = []
    
    for url in urls:
        logger.info(f"Scraping {url}")
        headlines = scrape_headlines_from_url(url)
        all_headlines.extend(headlines)
        
        # Be respectful - add delay between requests
        time.sleep(1)
    
    if all_headlines:
        output_filename = 'multiple_sites_headlines.csv'
        save_headlines_to_csv(all_headlines, output_filename)
        print(f"Scraped {len(all_headlines)} headlines from {len(urls)} URLs")
        print(f"Results saved to: {output_filename}")

if __name__ == "__main__":
    # Scrape example.com
    scrape_example_com()
    
    # Uncomment below to scrape multiple sites
    # urls_to_scrape = [
    #     "https://example.com",
    #     "https://httpbin.org/html",
    #     # Add more URLs here
    # ]
    # scrape_multiple_pages(urls_to_scrape)

# %%
