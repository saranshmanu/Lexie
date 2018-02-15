import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('output.txt')
close_answers=[('cipher',None),('hex',None),('crypto',None),('cypher',None)]

gensim.scripts.glove2Word2Vec.glove2Word2Vec('output.txt','output2.txt')


def get_short(answer, close_answers):
    

    first_depth = model.most_similar(positive = [answer], topn = 10)
    first_depth += close_answers

    second_depth = []

    for i,_ in first_depth:
        second_depth += model.most_similar(positive = [i], topn = 3)

    short_list=first_depth+second_depth
    return short_list

short_list_caesar = get_short('caesar', close_answers)

caesar_json = json.dumps({"short": short_list_caesar})