from bs4 import BeautifulSoup
import requests

nasa_question_links = ['https://en.wikipedia.org/wiki/Pizza_(song)','http://www.youredm.com/2017/08/21/martin-garrix-pizza-will-drop-friday/','https://en.wikipedia.org/wiki/Martin_Garrix','https://en.wikipedia.org/wiki/Bee', 'http://beehex.com/','https://techcrunch.com/2017/02/28/beehex-cooks-up-1-million-for-3d-food-printers-that-make-pizzas/','https://www.businessinsider.in/This-robot-can-3D-print-and-bake-a-pizza-in-six-minutes/Customers-will-also-eventually-be-able-to-order-pizzas-through-the-BeeHex-app-which-will-ping-them-when-theyre-ready-First-you-choose-the-pizzas-size-10-or-12-inch-dough-plain-tomato-or-gluten-free-sauce-tomato-basil-pesto-or-vodka-and-cheese-mozzarella-or-burrata-/slideshow/57456218.cms','https://www.inverse.com/article/28758-pizza-3d-printer-space-travel-beehex-nasa', 'https://futurism.com/nasa-astronauts-can-now-3d-print-pizzas-in-space/', 'https://www.indiatimes.com/technology/science-and-future/inspired-by-nasa-beehex-can-3d-print-a-pizza-for-you-in-just-five-minutes-flat-272988.html', 'http://www.zdnet.com/article/nasa-astronauts-may-soon-be-able-to-3d-print-pizzas-in-space/', 'https://www.digitaltrends.com/cool-tech/beehex-3d-printed-pizza/', 'https://en.wikipedia.org/wiki/Hexadecimal', 'https://en.wikipedia.org/wiki/Hexagon', ]

nasa_question_text = []

for i in nasa_question_links:
    html_content = requests.get(i)
    html_text = html_content.text
    soup = BeautifulSoup(html_text, "lxml")
    nasa_question_text.append(soup.get_text())
    print(i)
    
test_url = 'https://en.wikipedia.org/wiki/Pizza_(song)'
html = requests.get(test_url)
html_text = html.text
soup = BeautifulSoup(html_text, "html5lib")
print(soup.get_text())

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

sentences = []
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    for i in visible_texts:
        if (i != '\n' and len(i) > 10):
            sentences.append(i)
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Pizza_(song)').read()
print(text_from_html(html))

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
words_total = []

for i in sentences:
    no_punct = ""
    for char in i:
        if char not in punctuations:
            no_punct = no_punct + char
    words = no_punct.split()
    words_total += words
    