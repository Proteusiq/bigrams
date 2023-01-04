from bigrams import replacer, Grams

IN_SENTENCES = [
    ["this", "is", "new", "york", "baby", "again!"],
    ["new", "york", "and", "baby", "again!"],
]

OUT_SENTENCES = [
    ["this", "is", "new_york", "baby_again!"],
    ["new_york", "and", "baby_again!"],
]

BIGRAMS_MAPPER = {
    ("new", "york"): "new_york",
    ("baby", "again!"): "baby_again!",
}


def test_replacer():

    sentences = [replacer(sentence=s,
        bigrams_mapper=BIGRAMS_MAPPER,
        window_size=2,
    ) for s in IN_SENTENCES]
    
    assert sentences == OUT_SENTENCES

def test_grams():

    bi = Grams(window_size=2, threshold=2)
    sentences = bi.fit(X=IN_SENTENCES).transform(X=IN_SENTENCES)
    assert sentences == OUT_SENTENCES
