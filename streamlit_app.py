import spacy_streamlit
import streamlit as st

models = ["en_tox"]
title = "NLP TOX"
description = "Text analysis with NLP model trained on toxicological articles"
default_text = "Benzene in concentrations higher than 3mg can cause vomiting in humans."
token_attributes = ["idx", "text", "pos_", "tag_", "dep_","ent_type_"]
spacy_streamlit.visualize(models,default_text, visualizers = [ "ner", "parser", "similarity", "tokens"],\
                          similarity_texts = ("methanol", "ethanol"), token_attrs = token_attributes,\
                          show_json_doc = False,show_meta = False, show_config = False, \
                          show_visualizer_select = True,\
                          sidebar_title = title, sidebar_description = description)


