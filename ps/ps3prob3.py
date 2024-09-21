import requests
from bs4 import BeautifulSoup
import re


# Define the debate metadata.
moderators = ["MODERATOR", "SCHIEFFER", "SCHIEFFER", "LEHRER", "HOLT", "WALLACE"]

candidates = [
    {"Dem": "GORE", "Rep": "BUSH"},
    {"Dem": "KERRY", "Rep": "BUSH"},
    {"Dem": "OBAMA", "Rep": "MCCAIN"},
    {"Dem": "OBAMA", "Rep": "ROMNEY"},
    {"Dem": "CLINTON", "Rep": "TRUMP"},
    {"Dem": "BIDEN", "Rep": "TRUMP"}
]

titles = [
    "October 3, 2000: The First Gore-Bush Presidential Debate",
    "October 13, 2004: The Third Bush-Kerry Presidential Debate",
    "October 15, 2008: The Third McCain-Obama Presidential Debate",
    "October 3, 2012: The First Obama-Romney Presidential Debate",
    "September 26, 2016: The First Clinton-Trump Presidential Debate",
    "September 29, 2020: Presidential Debate"
]

years = range(2000, 2024, 4)
url = "https://debates.org/voter-education/debate-transcripts"

# Get the overview HTML page.
response = requests.get(url)
main_html = BeautifulSoup(response.content, 'html.parser')

# Extract the <a> tags with href attributes.
a_nodes = main_html.find_all('a', href=True)
labels = [a_node.get_text() for a_node in a_nodes]

# Find the index of titles in the labels.
selected_indices = [labels.index(title) for title in titles]

# Extract debate URLs using the selected indices.
debate_urls = [a_nodes[i]['href'] for i in selected_indices]

# Fix the URL for 2020 transcript, which is a full URL unlike the others.
debate_urls = [re.sub(r"https://www.debates.org", "", url, count=1) for url in debate_urls]

n = len(debate_urls)

assert all([re.match(r"^/voter-education", url) for url in debate_urls])
assert n == len(years)

# Fetch the HTML content for each debate
debates_html = [BeautifulSoup(requests.get(f"https://debates.org{url}").content, 'html.parser') for url in debate_urls]
assert len(debates_html) == n

def get_content(html):
    # Extracts debate content from html.
    content_node = html.find('div', {'id': 'content-sm'})
    if not content_node:
        raise Exception("No content found!")
    text = content_node.get_text(strip=True)
    
    # Sanity check
    header = content_node.find('h1')
    if header:
        print(header.get_text())
    
    return text

# Get the body content for all debates.
debates_body = [get_content(html) for html in debates_html]
assert len(debates_body) == n

# Visual sanity checks:
print(debates_body[0][:1000])
print(debates_body[5][:1000])

lengths = [len(body) for body in debates_body]
assert min(lengths) > 70000 and max(lengths) < 120000
