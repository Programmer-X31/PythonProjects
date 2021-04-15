from tkinter import *
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url: str, title: str):
        self.url = url
        self.title = title

    def scrape(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        headlines = soup.find_all(class_="DY5T1d")
        headlines = [headline.text for headline in headlines]
        return headlines

    def run(self):
        root = Tk()
        Label(root, text=self.title, font=(
            "SF Mono", 15, 'bold')).pack(expand=True)
        for headline in self.scrape()[: 26]:
            Label(root, text=headline, font=('SF Mono', 10)).pack(expand=True)
        root.mainloop()


space = Scraper('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERTRNek4zS2dzU0NTOXRMekF4T0RNemR5Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURadGNUY1NCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen', "Space")
physics = Scraper('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1EVnhhblFxQ2hJSUwyMHZNRFZ4YW5Rb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EWnRjVGNTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen', "Physics")
space.run()
physics.run()
