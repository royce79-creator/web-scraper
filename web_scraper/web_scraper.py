import requests
from bs4 import BeautifulSoup

def get_text(url):
  page = requests.get(url)
  citations = BeautifulSoup(page.content, 'html.parser').find_all(title="Wikipedia:Citation needed")
  return [citation.find_parent('p').text for citation in citations]

def get_citations_needed_count(url):
  words = get_text(url)
  return len(words)

def get_citations_needed_report(url):
  words = get_text(url)
  return '\n'.join([word.strip() for word in words])

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Cuthwulf_(son_of_Cuthwine)"
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
