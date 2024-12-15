import requests
from bs4 import BeautifulSoup

# Define the target URL
url = "https://finance.yahoo.com/"

# Fetch the webpage content
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract headlines based on the provided HTML structure
headlines = soup.find_all("h3", class_="clamp yf-18q3fnf")  # Adjust class to match the snippet

if not headlines:
    print("No headlines found. Check your selector.")
    exit()

# Display and save the headlines
print("Scraped Headlines:\n")
with open("headlines.txt", "w") as file:
    for idx, headline in enumerate(headlines, start=1):
        headline_text = headline.get_text(strip=True)
        print(f"{idx}. {headline_text}")
        file.write(f"{idx}. {headline_text}\n")

print("\nHeadlines saved to 'headlines.txt'")
