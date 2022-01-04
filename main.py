import requests
import bs4

while True:
        text = input("\nEnter your text : ")
        if text == "":
                exit(0)
        else:
                url = 'https://google.com/complete/search?output=toolbar&hl=es&q=' + text
                try:
                            result = requests.get(url)
                except requests.exceptions.RequestException as e:
                            raise SystemExit(e)
                soup = bs4.BeautifulSoup(result.text, "html.parser")
                suggestions = soup.find_all('suggestion')
                for suggestion in suggestions:
                        print(suggestion["data"], end=", ")
