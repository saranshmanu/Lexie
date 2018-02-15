import scraper

nasa_question_links = ['https://en.wikipedia.org/wiki/Pizza_(song)','http://www.youredm.com/2017/08/21/martin-garrix-pizza-will-drop-friday/', 'http://beehex.com/','https://www.businessinsider.in/This-robot-can-3D-print-and-bake-a-pizza-in-six-minutes/Customers-will-also-eventually-be-able-to-order-pizzas-through-the-BeeHex-app-which-will-ping-them-when-theyre-ready-First-you-choose-the-pizzas-size-10-or-12-inch-dough-plain-tomato-or-gluten-free-sauce-tomato-basil-pesto-or-vodka-and-cheese-mozzarella-or-burrata-/slideshow/57456218.cms','https://www.inverse.com/article/28758-pizza-3d-printer-space-travel-beehex-nasa', 'https://futurism.com/nasa-astronauts-can-now-3d-print-pizzas-in-space/', 'https://www.indiatimes.com/technology/science-and-future/inspired-by-nasa-beehex-can-3d-print-a-pizza-for-you-in-just-five-minutes-flat-272988.html', 'http://www.zdnet.com/article/nasa-astronauts-may-soon-be-able-to-3d-print-pizzas-in-space/', 'https://www.digitaltrends.com/cool-tech/beehex-3d-printed-pizza/',]

nasa_corpus = scraper.links_to_corpus(nasa_question_links)

print(nasa_corpus)

def train_model(corpus):
    model = Word2Vec(corpus, size = 50, window = 10, min_count = 1, workers = 4)
    


