import httpx
from bs4 import BeautifulSoup

# Define the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Define the URL
url = 'https://www.ambitionbox.com/list-of-companies?page=1'

async def fetch_page():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response
        except httpx.RequestError as e:
            print(f"An error occurred: {e}")
            return None

response = await fetch_page()

if response and response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the entire HTML content to check for the structure (optional, for debugging)
    # print(soup.prettify())

    # Find and print all <span> elements with the class 'companyCardWrapper__interLinking'
    for j in soup.find_all('span', class_='companyCardWrapper__interLinking'):
        print(j.text.strip())
else:
    print("Failed to retrieve the webpage after multiple attempts.")
