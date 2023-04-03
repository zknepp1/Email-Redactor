import os
import re
import io
import numpy as np
import spacy
from spacy.matcher import Matcher








def print_names(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    tokens = []
    for token in docx:
        if token.ent_type_ == 'PERSON':
            print(token.text, token.ent_type_)
            tokens.append(token.text)
        else:
            pass


def print_org(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    tokens = []
    for token in docx:
        if token.ent_type_ == 'ORG':
            print(token.text, token.ent_type_)
            tokens.append(token.text)
        else:
            pass


def print_gpe(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    tokens = []
    for token in docx:
        if token.ent_type_ == 'GPE':
            print(token.text, token.ent_type_)
            tokens.append(token.text)
        else:
            pass
          
          
          
def print_date(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    tokens = []
    for token in docx:
        if token.ent_type_ == 'DATE':
            print(token.text, token.ent_type_)
            tokens.append(token.text)
        else:
            pass


def print_phone(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    tokens = []
    for token in docx:
        if token.ent_type_ == 'PHONE':
            print(token.text, token.ent_type_)
            tokens.append(token.text)
        else:
            pass
          
          
# Functions to Sanitize and Redact 
def scrub(text):
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text)
    redacted_sentences = []
    for token in docx:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append('\u2588')

        elif token.ent_type_ == 'DATE':
            redacted_sentences.append('\u2588')

        elif token.ent_type_ == 'PHONE':
            redacted_sentences.append('\u2588')

        elif token.ent_type_ == 'GENDER':
            redacted_sentences.append('\u2588')

        elif in_matches(token.text):
          redacted_sentences.append('\u2588')

        else:
            redacted_sentences.append(token.text)

    return " ".join(redacted_sentences)

    
def write_to_file(text):
  tokens = [token.orth_ for token in text]
  f = open("myfile.redacted", "w")
  f.write(tokens)
  #print(f.read())
  f.close()


def in_matches(ent):
  for match_id, start, end in matches:
    matched_span = doc[start:end]
    if matched_span.text == ent:
      return True
    #print(matched_span.text)

    
    
    
    
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
