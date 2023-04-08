import sys
import os
import re
import io
import numpy as np
import spacy
from spacy.matcher import Matcher
import en_core_web_sm
import glob



def scrub_names(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences), redact_count


def scrub_dates(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'DATE':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences), redact_count



def scrub_phones(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'PHONE':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences), redact_count



def scrub_genders(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'GENDER':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences), redact_count




def scrub_addresses(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'ADDRESS':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences), redact_count





# Functions to Sanitize and Redact 
def scrub(text, matches, doc):
    redact_count = 0
    redacted_sentences = []
    for token in text:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif token.ent_type_ == 'DATE':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif token.ent_type_ == 'PHONE':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif token.ent_type_ == 'GENDER':
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        elif in_matches(token.text, matches, doc):
            redacted_sentences.append('\u2588')
            redact_count = redact_count + 1

        else:
            redacted_sentences.append(token.text)

    return " ".join(redacted_sentences), redact_count

    
def write_to_file(text, path, i):
   #tokens = [token.orth_ for token in text]
   f = open(path + "email" + str(i) + ".redacted", "w")
   try:
      f.write(str(text))
      print("wrote file to: ", path)
   except:
      print("Unable to write file")
   #print(f.read())
   f.close()


def in_matches(ent, matches, doc):
  for match_id, start, end in matches:
    matched_span = doc[start:end]
    if matched_span.text == ent:
      return True


def make_people_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern3 = [ {"ENT_TYPE": 'PERSON'}, {"ENT_TYPE": 'PERSON'} ]
    pattern4 = [ {"LIKE_EMAIL": True}]
    pattern5 = [ {"ENT_TYPE": 'PERSON'},{"TEXT": ','}, {"ENT_TYPE": 'PERSON'}]
    matcher.add("PERSON", [pattern3])
    matcher.add("PERSON", [pattern4])
    matcher.add("PERSON", [pattern5])
    return matcher


def make_date_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern7 =  [{"IS_DIGIT": True}]
    pattern16 = [{"LOWER": "january"}]
    pattern17 = [{"LOWER": "february"}]
    pattern18 = [{"LOWER": "march"}]
    pattern19 = [{"LOWER": "april"}]
    pattern20 = [{"LOWER": "may"}]
    pattern21 = [{"LOWER": "june"}]
    pattern22 = [{"LOWER": "july"}]
    pattern23 = [{"LOWER": "august"}]
    pattern24 = [{"LOWER": "september"}]
    pattern25 = [{"LOWER": "october"}]
    pattern26 = [{"LOWER": "november"}]
    pattern27 = [{"LOWER": "december"}]
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
    pattern40 = [{"IS_DIGIT": True}]
    matcher.add("DATE", [pattern7])
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
    return matcher


def make_phone_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern1 = [{"TEXT": "("},{"IS_DIGIT": True}, {"TEXT": ")"},{"IS_SPACE": True},{"IS_DIGIT": True}, {"TEXT": "-"}]
    pattern2 = [ {"IS_DIGIT": True}, {"TEXT": "-"}, {"IS_DIGIT": True}]
    pattern7 = [ {"IS_DIGIT": True},{"TEXT": "-"}, {"IS_DIGIT": True}, {"TEXT": "-"}, {"IS_DIGIT": True} ]
    pattern8 = [ {"IS_ALPHA": True}, {"IS_SPACE": True}, {"IS_DIGIT": True}, {"TEXT": ","}, {"IS_SPACE": True}, {"IS_DIGIT": True}]
    pattern9 = [{'TEXT': {'REGEX' : r'(\(\d\d\d\) \d\d\d-\d+)'}}]
    pattern10 = [{'TEXT': {'REGEX' : r'\d\d\d'}}]
    #pattern11 = [{'TEXT': {'REGEX' : r'\d\d\d\d)'}}]
    matcher.add("PHONE", [pattern1])
    matcher.add("PHONE", [pattern2])
    matcher.add("PHONE", [pattern7])
    matcher.add("PHONE", [pattern8])
    matcher.add("PHONE", [pattern9])
    matcher.add("PHONE", [pattern10])
    #matcher.add("PHONE", [pattern11])
    return matcher


def make_gender_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern1 = [{"LOWER": "he"}]
    pattern2 = [{"LOWER": "she"}]
    pattern3 = [{"LOWER": "his"}]
    pattern4 = [{"LOWER": "hers"}]
    pattern5 = [{"LOWER": "boy"}]
    pattern6 = [{"LOWER": "girl"}]
    pattern7 = [{"LOWER": "mom"}]
    pattern8 = [{"LOWER": "dad"}]
    pattern9 = [{"LOWER": "mother"}]
    pattern10 = [{"LOWER": "father"}]
    pattern11 = [{"LOWER": "male"}]
    pattern12 = [{"LOWER": "female"}]
    pattern13 = [{"LOWER": "man"}]
    pattern14 = [{"LOWER": "woman"}]
    pattern15 = [{"LOWER": "males"}]
    pattern16 = [{"LOWER": "females"}]
    pattern17 = [{"LOWER": "boys"}]
    pattern18 = [{"LOWER": "girls"}]
    matcher.add("GENDER", [pattern1])
    matcher.add("GENDER", [pattern2])
    matcher.add("GENDER", [pattern3])
    matcher.add("GENDER", [pattern4])
    matcher.add("GENDER", [pattern5])
    matcher.add("GENDER", [pattern6])
    matcher.add("GENDER", [pattern7])
    matcher.add("GENDER", [pattern8])
    matcher.add("GENDER", [pattern9])
    matcher.add("GENDER", [pattern10])
    matcher.add("GENDER", [pattern11])
    matcher.add("GENDER", [pattern12])
    matcher.add("GENDER", [pattern13])
    matcher.add("GENDER", [pattern14])
    matcher.add("GENDER", [pattern15])
    matcher.add("GENDER", [pattern16])
    matcher.add("GENDER", [pattern17])
    matcher.add("GENDER", [pattern18])
    return matcher


def make_address_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern1 = [{"IS_DIGIT": True}]
    pattern2 = [{"IS_DIGIT": True}, {"IS_SPACE": True}, {"IS_ALPHA": True}]
    pattern3 = [{"IS_DIGIT": True}, {"IS_SPACE": True}, {"IS_ALPHA": True},{"IS_SPACE": True}, {"IS_ALPHA": True}]
    pattern4 = [{"IS_DIGIT": True}, {"IS_ALPHA": True}]
    matcher.add("ADDRESS", [pattern1])
    matcher.add("ADDRESS", [pattern2])
    matcher.add("ADDRESS", [pattern3])
    matcher.add("ADDRESS", [pattern4])
    return matcher







def main():
    args = sys.argv[1:]
    nlp = spacy.load("en_core_web_sm")
    toll = 0
    i = 0
    for index, obj in enumerate(args):
        if obj == '--input':
            #print('you chose: ', obj)
            files = args[index+1]
        else:
            pass


    for name in glob.glob(files, recursive = True):
        print(name)

        try:
            with open(name, 'r') as file:
                data4 = file.read()
        except:
            print('could not open file')

        doc = nlp(data4)
                
        for index, obj in enumerate(args):

            if obj == '--names':
                pm = make_people_matcher()
                name_matches = pm(doc)
                doc, count = scrub_names(doc, name_matches, doc)
                doc = nlp(doc)
                toll = toll + count


            elif obj == '--dates':
                dm = make_date_matcher()
                date_matches = dm(doc)
                doc, count = scrub_dates(doc, date_matches, doc)
                doc = nlp(doc)
                toll = toll + count


            elif obj == '--phones':
                phm = make_phone_matcher()
                phone_matches = phm(doc)
                doc, count = scrub_phones(doc, phone_matches, doc)
                doc = nlp(doc)
                toll = toll + count


            elif obj == '--genders':
                gm = make_gender_matcher()
                gender_matches = gm(doc)
                doc, count = scrub_genders(doc, gender_matches, doc)
                doc = nlp(doc)
                toll = toll + count


            elif obj == '--address':
                am = make_address_matcher()
                address_matches = am(doc)
                doc, count = scrub_addresses(doc, address_matches, doc)
                doc = nlp(doc)
                toll = toll + count


            elif obj == '--output':
                path = args[index+1]
                print(path)

            elif obj == '--stats':
                print("The redactor as redacted: ", toll, " items" )
            
            else:
                pass

        write_to_file(doc, path, i)
        i = i + 1





if __name__ == "__main__":
    main()
