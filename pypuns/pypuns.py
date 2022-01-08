import random
import json

from .puns.languages import all_languages



class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass



# Gets all puns of a category.
def get_all_puns(language='en', category='puns', puns_file='default'):
    """
    Parameters
    ----------
    language: str
        Choices: 'en', 'it'
    category: str
        Choices: 'all', 'blackhumor', 'thonguetwist', 'puns'
    puns_file: str
        Choices: 'default'
    Returns
    -------
    puns: list
    """

    if language not in all_languages:
        raise LanguageNotFoundError(f'Currently the {language} language is not supported. Submit your puns for this new language on github!')

    puns = all_languages[language]

    if category not in puns:
        raise CategoryNotFoundError(f'Currently the {category} category is not supported. Submit new categories for the {language} language on github!')

    return puns[category]
    


# Random selection of a pun from all puns of a category.
def get_pun(language='en', category='puns', puns_file='default'):
    """
    Parameters
    ----------
    language: str
        Choices: 'en', 'it'
    category: str
        Choices: 'all', 'blackhumor', 'thonguetwist', 'puns'
    puns_file: str
        Choices: 'default'
    Returns
    -------
    pun: str
    """

    pun = get_all_puns(language, category, puns_file)
    
    return random.choice(pun)

