import spacy_streamlit

models = ["en_tox"]
default_text = "Concentrations of diethylstilboestrol (DES) exceeding 100 microM are normally fatal to all living tissues."
spacy_streamlit.visualize(models, default_text)
