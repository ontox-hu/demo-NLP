import spacy_streamlit as ss
import streamlit as st
import custom_viz as cv

color = "#09A3D5"
models = ["en_aop_ner_trf"]
title = "NLP TOX"
description = "Text analysis with NLP model trained on toxicological articles"
default_text = "The data showed that Quercetin significantly prevented neurotoxicity in mice."
token_attributes = ["idx", "text", "pos_", "tag_", "dep_","ent_type_"]
ner_attributes = ["text", "label_", "start_char", "end_char"]
visualizers = [ "ner"]
similarity_texts = ("methanol", "ethanol")
cols = {"MOLECULE":"red", "DISEASE":"lightblue", "DNA":"pink", "ORGANISM":"orange", "EFFECT":"green", "EVENT":"yellow", "LOC":"grey"}


cv.visualize(models,default_text, visualizers = [ "ner"],\
                          token_attrs = token_attributes,\
                          show_json_doc = False,show_meta = False, show_config = False, \
                          show_visualizer_select = True,\
                          sidebar_title = title, sidebar_description = description, ner_colors = cols)



