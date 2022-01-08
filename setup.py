from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

VERSION = '0.1.0.0'
DESCRIPTION = 'Simple random puns picker'

# Setting up
setup(
    name='pypuns_test',
    version=VERSION,
    url='https://github.com/PyPuns/PyPuns',
    author='Bunz',
    author_email='66bunz@gmail.com',
    
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,

    packages=['pypuns', 'pypuns.puns'],
    include_package_data=True,
    
    install_requires=[],

    keywords=['python', 'puns', 'pypuns', 'chatbots', 'chat', 'jokes', 'random jokes', 'random joke', 'joke', 'pun', 'random pun', 'random puns'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Build Tools',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
    ],

    project_urls={
        'Bug Reports': 'https://github.com/PyPuns/pypuns/issues',
        'Funding': 'https://www.buymeacoffee.com/66bunz',
        'Say Thanks!': 'https://saythanks.io/to/66Bunz',
        'Source': 'https://github.com/PyPuns/pypuns',
        "Bug Tracker": "https://github.com/PyPuns/pypuns/issues",
    },
)
