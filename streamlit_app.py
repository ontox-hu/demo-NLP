import spacy_streamlit
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
                          similarity_texts = ("methanol", "ethanol"), token_attrs = token_attributes,\
                          show_json_doc = False,show_meta = False, show_config = False, \
                          show_visualizer_select = True,\
                          sidebar_title = title, sidebar_description = description)

'''

## Setup
st.config.set_option("theme.primaryColor", color)
st.experimental_rerun()
st.sidebar.title(title)
st.sidebar.markdown(description)
model_names = models
format_func = str
if isinstance(models, dict):
    format_func = lambda name: models.get(name, name)
    model_names = list(models.keys())

default_model_index = (
    model_names.index(default_model)
    if default_model is not None and default_model in model_names
    else 0
)
spacy_model = st.sidebar.selectbox(
    "Model",
    model_names,
    index=default_model_index,
    key=f"{key}_visualize_models",
    format_func=format_func,
)
model_load_state = st.info(f"Loading model '{spacy_model}'...")
nlp = load_model(spacy_model)
model_load_state.empty()

active_visualizers = st.sidebar.multiselect(
    "Visualizers",
    options=visualizers,
    default=list(visualizers),
    key=f"{key}_viz_select",
)

# Text processing
default_text = (
    get_default_text(nlp) if get_default_text is not None else default_text
)
text = st.text_area("Text to analyze", default_text, key=f"{key}_visualize_text")
doc = process_text(spacy_model, text)

# Display visualizers

if "ner" in visualizers and "ner" in active_visualizers:
    ner_labels = ner_labels or nlp.get_pipe("ner").labels
    visualize_ner(doc, labels=ner_labels, colors = cols, attrs=ner_attributes, key=key)
    
if "parser" in visualizers and "parser" in active_visualizers:
    visualize_parser(doc, key=key)

if "tokens" in visualizers and "tokens" in active_visualizers:
    visualize_tokens(doc, attrs=token_attributes, key=key

if "similarity" in visualizers and "similarity" in active_visualizers:
    visualize_similarity(nlp, key=key)
