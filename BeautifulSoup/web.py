import requests
from bs4 import BeautifulSoup
def get_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load the webpage")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_list = soup.find_all('span', class_='text')
    authors_list = soup.find_all('small', class_='author')
    lists =[]
    for quotes, authors in zip(quotes_list, authors_list):
        quotes = quotes.get_text(strip =True)
        authors = authors.get_text(strip =True)
        lists.append((quotes, authors))
    return lists
if __name__ == "__main__":
    print("Quotes and Authors from the website:")
    quotes = get_quotes()
    if quotes:
        for quote, author in quotes:
            print(f'"{quote}" - {author}')
    else:
        print("No quotes found.")




