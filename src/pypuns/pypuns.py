import random
import json

italian = json.load(open('./pypuns/src/pypuns/puns/it.json'))
english = json.load(open('./pypuns/src/pypuns/puns/en.json'))
german = json.load(open('./pypuns/src/pypuns/puns/de.json'))

# print(italian)


all_puns = {
    "it": italian,
    "en": english,
    "de": german
}

# print(all_puns)

class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


# Gets all puns from a category
def get_all_puns(language='it', category='all_puns', puns_file='default'):
    """
    Parameters
    ----------
    category: str
        Choices: 'all', 'blackhumour', 'thonguetwist', 'jokes'
    language: str
        Choices: 'en', 'it', 'es', 'gl', 'eu', 'de'
    puns_file: str
        Choices: 'default', path to puns .json file
    Returns
    -------
    puns: list
    """

    if language not in all_puns:
        raise LanguageNotFoundError(
            f'Currently the {language} language is not supported. Submit your puns for this new language on github!')

    puns = all_puns[language]

    # print(puns)

    if category not in puns:
        raise CategoryNotFoundError(
            f'Currently the {category} category is not supported. Submit new categories for the {language} language on github!')

    return puns[category]



# Random selection of a joke
def get_pun(language='it', category='all_puns', puns_file='default'):
    """
    Parameters
    ----------
    category: str
        Choices: 'all', 'blackhumour', 'thonguetwist', 'jokes'
    lang: str
        Choices: 'en', 'it', 'es', 'gl', 'eu', 'de'
    puns_file: str
        Choices: 'default', path to puns .json file
    Returns
    -------
    pun: str
    """

    pun = get_all_puns(language, category, puns_file)
    return random.choice(pun)


print = get_pun()
