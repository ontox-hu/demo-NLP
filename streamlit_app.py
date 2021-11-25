import spacy_streamlit as ss
import streamlit as st
import custom_viz as cv

color = "#09A3D5"
models = ["en_tox"]
title = "NLP TOX"
description = "Text analysis with NLP model trained on toxicological articles"
default_text = "Benzene in concentrations higher than 3mg can cause vomiting in humans."
token_attributes = ["idx", "text", "pos_", "tag_", "dep_","ent_type_"]
ner_attributes = ["text", "label_", "start_char", "end_char"]
visualizers = [ "ner", "parser", "similarity", "tokens"]
similarity_texts = ("methanol", "ethanol")
cols = {"COMPOUND":"red", "DOSE":"lightblue", "EXP_ROUTE":"green", "ORGANISM":"orange", "PHENOTYPE":"lightbrown", "PARENT_OFFSPRING":"yellow", "IN_VITRO_VIVO":"pink"}


cv.visualize(models,default_text, visualizers = [ "ner", "parser", "similarity", "tokens"],\
                          similarity_texts = similarity_texts, token_attrs = token_attributes,\
                          show_json_doc = False,show_meta = False, show_config = False, \
                          show_visualizer_select = True,\
                          sidebar_title = title, sidebar_description = description, ner_colors = cols)



