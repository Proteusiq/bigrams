from bigrams import Grams, replacer



def test_replacer(artifacts) -> None:

    sentences = [
        replacer(
            sentence=s,
            bigrams_mapper=artifacts.bigram_mapper,
            window_size=2,
        )
        for s in artifacts.in_sentences
    ]

    assert sentences == artifacts.out_senteces


def test_grams(artifacts) -> None:

    bi = Grams(window_size=2, threshold=2)
    sentences = bi.fit(X=artifacts.in_sentences).transform(X=artifacts.in_sentences)
    assert sentences == artifacts.out_senteces

    sentences = Grams(window_size=2, threshold=2).fit_transform(X=artifacts.in_sentences)
    assert sentences == artifacts.out_senteces
