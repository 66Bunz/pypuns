import json

italian = json.load(open('./pypuns/puns/it.json'))
english = json.load(open('./pypuns/puns/en.json'))
# german = json.load(open('./pypuns/puns/de.json'))

all_languages = {
    "it": italian,
    "en": english,
}