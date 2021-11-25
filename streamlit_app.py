import spacy_streamlit as ss
import streamlit as st

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

'''
spacy_streamlit.visualize(models,default_text, visualizers = [ "ner", "parser", "similarity", "tokens"],\
                          similarity_texts = similarity_texts, token_attrs = token_attributes,\
                          show_json_doc = False,show_meta = False, show_config = False, \
                          show_visualizer_select = True,\
                          sidebar_title = title, sidebar_description = description)

'''

## Setup

nlp = ss.load_model("en_tox")

'''
active_visualizers = st.sidebar.multiselect(
    "Visualizers",
    options=visualizers,
    default=list(visualizers),
    key=f"{key}_viz_select",
)
'''
# Text processing
#text = st.text_area("Text to analyze", default_text, key=f"{key}_visualize_text") # Problem here. why?
doc = ss.process_text(spacy_model, default_text)

# Display visualizers

if "ner" in visualizers: #and "ner" in active_visualizers:
    ner_labels = nlp.get_pipe("ner").labels
    ss.visualize_ner(doc, labels=ner_labels, colors = cols, attrs=ner_attributes, key=key)
    
if "parser" in visualizers: # and "parser" in active_visualizers:
    ss.visualize_parser(doc, key=key)

if "tokens" in visualizers: # and "tokens" in active_visualizers:
    ss.visualize_tokens(doc, attrs=token_attributes, key=key)

if "similarity" in visualizers: # and "similarity" in active_visualizers:
    ss.visualize_similarity(nlp, default_texts = similarity_texts, key=key)


