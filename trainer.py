import scraper
from gensim.models import Word2Vec

nasa_question_links = ['http://edmreviewer.com/2017/08/26/martin-garrix-pizza/','http://www.thepostathens.com/article/2017/08/martin-garrix-pizza-strings','https://inhabitat.com/nasa-funded-food-3d-printer-gets-its-first-prototype-3d-prints-an-entire-pizza/', 'https://www.businessinsider.in/This-robot-can-3D-print-a-pizza-in-under-five-minutes/When-piping-hot-BeeHexs-pizzas-rival-those-made-by-real-chefs-maybe-even-better-It-has-the-potential-to-create-more-interesting-foods-like-say-a-pastry-with-hundreds-of-different-layers-French-says-These-are-things-that-you-just-cant-make-with-human-hands-/slideshow/52733251.cms','https://en.wikipedia.org/wiki/Pizza_(song)','http://www.youredm.com/2017/08/21/martin-garrix-pizza-will-drop-friday/', 'http://beehex.com/','https://www.businessinsider.in/This-robot-can-3D-print-and-bake-a-pizza-in-six-minutes/Customers-will-also-eventually-be-able-to-order-pizzas-through-the-BeeHex-app-which-will-ping-them-when-theyre-ready-First-you-choose-the-pizzas-size-10-or-12-inch-dough-plain-tomato-or-gluten-free-sauce-tomato-basil-pesto-or-vodka-and-cheese-mozzarella-or-burrata-/slideshow/57456218.cms','https://www.inverse.com/article/28758-pizza-3d-printer-space-travel-beehex-nasa', 'https://futurism.com/nasa-astronauts-can-now-3d-print-pizzas-in-space/', 'https://www.indiatimes.com/technology/science-and-future/inspired-by-nasa-beehex-can-3d-print-a-pizza-for-you-in-just-five-minutes-flat-272988.html', 'http://www.zdnet.com/article/nasa-astronauts-may-soon-be-able-to-3d-print-pizzas-in-space/', 'https://www.digitaltrends.com/cool-tech/beehex-3d-printed-pizza/','http://www.huffingtonpost.co.uk/cohan-chew/did-beehex-just-hit-print_b_10108424.html', 'https://www.3ders.org/articles/20170301-pizza-3d-printing-startup-beehex-brings-in-the-dough-1m-to-be-exact.html','https://motherboard.vice.com/en_us/article/aekjnb/nasas-3d-food-printer-will-make-pizza-at-amusement-parks', 'https://spinoff.com/beehex','https://www.nasa.gov/directorates/spacetech/home/feature_3d_food.html', 'http://allthatsinteresting.com/3d-printer-print-pizzas']

nasa_corpus = scraper.links_to_corpus(nasa_question_links)

print(nasa_corpus)

def train_model(corpus):
    model = Word2Vec(corpus, size = 50, window = 10, min_count = 1, workers = 4)
    return model

model = train_model(nasa_corpus)



