import nltk
import re
import string

wine_remove_words = ['wine', 'rosé', 'red',
                     'white', 'drink', 'aroma', 'flavor', 'vineyard']
other_remove_words = ['\'s', "'"]


def tokenize_grape_names(grape_names):
    """Given a list of grape names, split them
    on spaces and hyphens to yield tokens"""
    grape_tokens = []
    for name in grape_names:
        name = name.lower()

        # split on - and space using regex
        tokens = re.split('[- ]', name)
        grape_tokens += tokens
    return grape_tokens


def create_pre_lemmatizing_remove_words(grape_names):
    """Create list of words that needs to be removed
    from wine reviews before lemmatization happens"""
    grape_tokens = tokenize_grape_names(grape_names)
    pre_lem_remove = set(
        [p for p in string.punctuation]
        + nltk.corpus.stopwords('english')
        + grape_tokens
    )
    return pre_lem_remove


def create_post_lemmatizing_remove_words():
    """Create list of words to be removed
    after lemmatization has happened"""
    post_lem_remove = set(
        wine_remove_words
        + other_remove_words
    )
    return post_lem_remove


def wine_tokenizer(desc, grape_names):
    """Turn wine descriptions into lowercase tokens.
    Lemmatize (plural to singular, -ing & -ed to root verb
    form, etc.), remove punctuations & stopwords.
    e.g.: Aromas include tropical fruit, broom, brimstone and dried herb.-->
    ['aromas', 'include', 'tropical', 'fruit', 'broom', 'brimstone',
    'dried', 'herb']"""
    pre_lem_remove = create_pre_lemmatizing_remove_words(grape_names)
    post_lem_remove = create_post_lemmatizing_remove_words()

    tokens = nltk.tokenize.word_tokenizer(desc.lower())
    lemmatizer = nltk.stem.WordNetLemmatizer()

    cleaned_tokens = [lemmatizer.lemmatize(t) for t in tokens
                      if not (
        (t in pre_lem_remove)
        or (lemmatizer.lemmatize(t) in post_lem_remove)
        or (t.isnumeric())
    )]

    return cleaned_tokens
