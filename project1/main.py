import os
import re
import io
import numpy as np
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")


matcher = Matcher(nlp.vocab)


pattern1 = [
              {"TEXT": "("},
              {"IS_DIGIT": True},
              {"TEXT": ")"},
              {"IS_SPACE": True},
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True}
           ]

pattern2 = [
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True}
           ]


pattern3 = [
              {"ENT_TYPE": 'PERSON'},
              {"ENT_TYPE": 'PERSON'}
           ]

pattern4 = [
              {"LIKE_EMAIL": True}
           ]

pattern5 = [
              {"ENT_TYPE": 'PERSON'},
              {"TEXT": ','},
              {"ENT_TYPE": 'PERSON'}
           ]

pattern6 = [
              {"TEXT": "He"}
           ]

pattern7 = [
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True}
           ]

pattern8 = [
              {"IS_ALPHA": True},
              {"IS_SPACE": True},
              {"IS_DIGIT": True},
              {"TEXT": ","},
              {"IS_SPACE": True},
              {"IS_DIGIT": True}
           ]

pattern9 = [{'TEXT': {'REGEX' : r'(\(\d\d\d\) \d\d\d-\d+)'}}]

pattern10 = [{'TEXT': {'REGEX' : r'\d\d\d'}}]
pattern11 = [{'TEXT': {'REGEX' : r'\d\d\d\d)'}}]

pattern12 = [{"LOWER": "he"}]
pattern13 = [{"LOWER": "she"}]
pattern14 = [{"LOWER": "his"}]
pattern15 = [{"LOWER": "hers"}]

pattern16 = [{"TEXT": "january"}]
pattern17 = [{"TEXT": "february"}]
pattern18 = [{"TEXT": "march"}]
pattern19 = [{"TEXT": "april"}]
pattern20 = [{"TEXT": "may"}]
pattern21 = [{"TEXT": "june"}]
pattern22 = [{"TEXT": "july"}]
pattern23 = [{"TEXT": "august"}]
pattern24 = [{"TEXT": "september"}]
pattern25 = [{"TEXT": "october"}]
pattern26 = [{"TEXT": "november"}]
pattern27 = [{"TEXT": "december"}]

pattern28 = [{"LOWER": "jan"}]
pattern29 = [{"LOWER": "feb"}]
pattern30 = [{"LOWER": "mar"}]
pattern31 = [{"LOWER": "apr"}]
pattern32 = [{"LOWER": "may"}]
pattern33 = [{"LOWER": "jun"}]
pattern34 = [{"LOWER": "jul"}]
pattern35 = [{"LOWER": "aug"}]
pattern36 = [{"LOWER": "sep"}]
pattern37 = [{"LOWER": "oct"}]
pattern38 = [{"LOWER": "nov"}]
pattern39 = [{"LOWER": "dec"}]


pattern40 = [
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True},
              {"TEXT": "-"},
              {"IS_DIGIT": True},
              {"TEXT": "."}
           ]






matcher.add("PHONE", [pattern1])
matcher.add("PHONE", [pattern2])
matcher.add("PERSON", [pattern3])
matcher.add("EMAIL", [pattern4])
matcher.add("PERSON", [pattern5])
matcher.add("GENDER", [pattern6])
matcher.add("DATE", [pattern7])
matcher.add("DATE", [pattern8])
matcher.add("PHONE", [pattern9])
matcher.add("PHONE", [pattern10])

matcher.add("GENDER", [pattern12])
matcher.add("GENDER", [pattern13])
matcher.add("GENDER", [pattern14])
matcher.add("GENDER", [pattern15])

matcher.add("DATE", [pattern16])
matcher.add("DATE", [pattern17])
matcher.add("DATE", [pattern18])
matcher.add("DATE", [pattern19])
matcher.add("DATE", [pattern20])
matcher.add("DATE", [pattern21])
matcher.add("DATE", [pattern22])
matcher.add("DATE", [pattern23])
matcher.add("DATE", [pattern24])
matcher.add("DATE", [pattern25])
matcher.add("DATE", [pattern26])
matcher.add("DATE", [pattern27])
matcher.add("DATE", [pattern28])
matcher.add("DATE", [pattern29])
matcher.add("DATE", [pattern30])
matcher.add("DATE", [pattern31])
matcher.add("DATE", [pattern32])
matcher.add("DATE", [pattern33])
matcher.add("DATE", [pattern34])
matcher.add("DATE", [pattern35])
matcher.add("DATE", [pattern36])
matcher.add("DATE", [pattern37])
matcher.add("DATE", [pattern38])
matcher.add("DATE", [pattern39])
matcher.add("DATE", [pattern40])


doc = nlp(data4)

matches = matcher(doc)



x = scrub(doc)

write_to_file(x)



