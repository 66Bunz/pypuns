import random


#Gets all puns from a category
def get_all_puns(language='en', category='all', puns='default'):
    """
    Parameters
    ----------
    category: str
        Choices: 'all', 'blackhumour', 'thonguetwist', 'jokes'
    language: str
        Choices: 'en', 'it', 'es', 'gl', 'eu', 'de'
    puns: str
        Choices: 'default', path to puns .json file
    Returns
    -------
    puns: list
    """

    if language not in all_puns:
        raise LanguageNotFoundError(f'Currently the {language} language is not supported. Submit your puns for this language on github!')

    puns = all_puns[language]

    if category not in puns:
        raise CategoryNotFoundError(f'Currently the {category} category is not supported. Submit new categories for the {language} language on github!)

    return puns[category]


#Random selection of a joke
def get_pun(language='en', category='all', puns='default'):
    """
    Parameters
    ----------
    category: str
        Choices: 'all', 'blackhumour', 'thonguetwist', 'jokes'
    lang: str
        Choices: 'en', 'it', 'es', 'gl', 'eu', 'de'
    puns: str
        Choices: 'default', path to puns .json file
    Returns
    -------
    pun: str
    """

    pun = get_all_puns(language, category, puns)
    return random.choice(pun)

