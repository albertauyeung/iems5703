from bs4 import BeautifulSoup as BS
import requests

# Base URL of content pages
base_url = "http://highscalability.com/blog/?currentPage={:d}"

# A variable for collecting links to individual articles
links = []

# Loop through the first 10 content pages
for i in range(1, 11):

    # Generate the actual URL to the content page
    url = base_url.format(i)
    print(url)

    # Send HTTP request
    res = requests.get(url, timeout=5)
    if res.status_code == 200:

        # Parse the page using BeautifulSoup
        soup = BS(res.text, 'lxml')

        # Extract links of individual articles
        anchors = soup.select("h2 a")
        for a in anchors:
            links.append(a["href"])
