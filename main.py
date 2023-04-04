import sys
import os
import re
import io
import numpy as np
import spacy
from spacy.matcher import Matcher
#from redact import scrub
#from redact import write_to_file
#from redact import in_matches
import en_core_web_sm


# Functions to Sanitize and Redact 
def scrub(text, matches, doc):
    #nlp = spacy.load("en_core_web_sm")
    #docx = nlp(text)
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

    
def write_to_file(text, path):
   #tokens = [token.orth_ for token in text]
   f = open(path + "myfile.redacted", "w")
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
    #print(matched_span.text)




def make_matcher():
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab)
    pattern1 = [{"TEXT": "("},{"IS_DIGIT": True}, {"TEXT": ")"},{"IS_SPACE": True},{"IS_DIGIT": True}, {"TEXT": "-"}, {"IS_DIGIT": True}]
    pattern2 = [ {"IS_DIGIT": True}, {"TEXT": "-"}, {"IS_DIGIT": True}]
    pattern3 = [ {"ENT_TYPE": 'PERSON'}, {"ENT_TYPE": 'PERSON'} ]
    pattern4 = [ {"LIKE_EMAIL": True}]
    pattern5 = [ {"ENT_TYPE": 'PERSON'},{"TEXT": ','}, {"ENT_TYPE": 'PERSON'}]
    pattern6 = [ {"TEXT": "He"} ]
    pattern7 = [ {"IS_DIGIT": True},{"TEXT": "-"}, {"IS_DIGIT": True}, {"TEXT": "-"}, {"IS_DIGIT": True} ]
    pattern8 = [ {"IS_ALPHA": True}, {"IS_SPACE": True}, {"IS_DIGIT": True}, {"TEXT": ","}, {"IS_SPACE": True}, {"IS_DIGIT": True} ]
    pattern9 = [{'TEXT': {'REGEX' : r'(\(\d\d\d\) \d\d\d-\d+)'}}]
    pattern10 = [{'TEXT': {'REGEX' : r'\d\d\d'}}]
    pattern11 = [{'TEXT': {'REGEX' : r'\d\d\d\d)'}}]
    pattern12 = [{"LOWER": "he"}]
    pattern13 = [{"LOWER": "she"}]
    pattern14 = [{"LOWER": "his"}]
    pattern15 = [{"LOWER": "hers"}]
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
    return matcher



def main():
    args = sys.argv[1:]
    #for i in args:
    #    print(i)
    file = args[1]
    path = args[8]
    try:
       with open(file, 'r') as file:
           data4 = file.read()
       nlp = spacy.load("en_core_web_sm")
       doc = nlp(data4)
       m = make_matcher()
       matches = m(doc)
       x, count = scrub(doc, matches, doc)
       write_to_file(x, path)
       print("File has been successfully redacted")
       if args[10] == "stderr":
           print("The redactor as redacted: ", count, " items" )
    except:
       print("Could not process file")

if __name__ == "__main__":
    main()



