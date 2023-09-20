import re
import requests

# URL of the website you want to scrape
url = 'https://www.scimagojr.com/journalsearch.php?q=28773&tip=sid&clean=0'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Use a regular expression to find email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails_found = re.findall(email_pattern, response.text)

    # Print the extracted email addresses
    for email in emails_found:
        print(email)
else:
    print('Failed to retrieve the page')
