import random


#Gets all jokes from a category
def get_jokes(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
    Returns
    -------
    jokes: list
    """

    if language not in all_jokes:
        raise LanguageNotFoundError('No such language %s' % language)

    jokes = all_jokes[language]

    if category not in jokes:
        raise CategoryNotFoundError('No such category %s in language %s' % (category, language))

    return jokes[category]


#Random selection of a joke
def get_joke(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
    Returns
    -------
    joke: str
    """

    jokes = get_jokes(language, category)
    return random.choice(jokes)