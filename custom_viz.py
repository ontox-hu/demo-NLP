from typing import List, Sequence, Tuple, Optional, Dict, Union, Callable
import streamlit as st
import spacy
from spacy.language import Language
from spacy import displacy
import pandas as pd
import spacy_streamlit as ss
from spacy_streamlit.util import load_model, process_text, get_svg, get_html, LOGO
from spacy_streamlit.visualizer import visualize_ner, visualize_parser, visualize_textcat, visualize_similarity, visualize_tokens


# fmt: off
NER_ATTRS = ["text", "label_", "start", "end", "start_char", "end_char"]
TOKEN_ATTRS = ["idx", "text", "lemma_", "pos_", "tag_", "dep_", "head", "morph",
               "ent_type_", "ent_iob_", "shape_", "is_alpha", "is_ascii",
               "is_digit", "is_punct", "like_num", "is_sent_start"]
# fmt: on
FOOTER = """<span style="font-size: 0.75em">&hearts; Built with [`spacy-streamlit`](https://github.com/explosion/spacy-streamlit)</span>"""

def visualize(
    models: Union[List[str], Dict[str, str]],
    default_text: str = "",
    default_model: Optional[str] = None,
    visualizers: List[str] = ["parser", "ner", "textcat", "similarity", "tokens"],
    ner_labels: Optional[List[str]] = None,
    ner_attrs: List[str] = NER_ATTRS,
    similarity_texts: Tuple[str, str] = ("apple", "orange"),
    token_attrs: List[str] = TOKEN_ATTRS,
    show_json_doc: bool = True,
    show_meta: bool = True,
    show_config: bool = True,
    show_visualizer_select: bool = False,
    show_pipeline_info: bool = True,
    sidebar_title: Optional[str] = None,
    sidebar_description: Optional[str] = None,
    show_logo: bool = True,
    color: Optional[str] = "#09A3D5",
    key: Optional[str] = None,
    ner_colors: Optional[List[str]] = None,
    get_default_text: Callable[[Language], str] = None,
) -> None:
    """Embed the full visualizer with selected components."""

    if st.config.get_option("theme.primaryColor") != color:
        st.config.set_option("theme.primaryColor", color)

        # Necessary to apply theming
        st.experimental_rerun()

    if show_logo:
        st.sidebar.markdown(LOGO, unsafe_allow_html=True)
    if sidebar_title:
        st.sidebar.title(sidebar_title)
    if sidebar_description:
        st.sidebar.markdown(sidebar_description)

    # Allow both dict of model name / description as well as list of names
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
    if not ('sentencizer' in nlp.pipe_names):
      nlp.add_pipe('sentencizer')
    model_load_state.empty()

    if show_pipeline_info:
        st.sidebar.subheader("Pipeline info")
        desc = f"""<p style="font-size: 0.85em; line-height: 1.5"><strong>{spacy_model}:</strong> <code>v{nlp.meta['version']}</code>. {nlp.meta.get("description", "")}</p>"""
        st.sidebar.markdown(desc, unsafe_allow_html=True)

    if show_visualizer_select:
        active_visualizers = st.sidebar.multiselect(
            "Visualizers",
            options=visualizers,
            default=list(visualizers),
            key=f"{key}_viz_select",
        )
    else:
        active_visualizers = visualizers

    default_text = (
        get_default_text(nlp) if get_default_text is not None else default_text
    )
    text = st.text_area("Text to analyze", default_text, key=f"{key}_visualize_text")
    doc = process_text(spacy_model, text)
    
    if "ner" in visualizers and "ner" in active_visualizers:
        ner_labels = ner_labels or nlp.get_pipe("ner").labels
        visualize_ner(doc, labels=ner_labels, colors = ner_colors, attrs=ner_attrs, key=key)
    if "parser" in visualizers and "parser" in active_visualizers:
        visualize_parser(doc, key=key)
    if "textcat" in visualizers and "textcat" in active_visualizers:
        visualize_textcat(doc)
    if "similarity" in visualizers and "similarity" in active_visualizers:
        visualize_similarity(nlp, default_texts = similarity_texts, key=key)
    if "tokens" in visualizers and "tokens" in active_visualizers:
        visualize_tokens(doc, attrs=token_attrs, key=key)


    if show_json_doc or show_meta or show_config:
        st.header("Pipeline information")
        if show_json_doc:
            json_doc_exp = st.expander("JSON Doc")
            json_doc_exp.json(doc.to_json())

        if show_meta:
            meta_exp = st.expander("Pipeline meta.json")
            meta_exp.json(nlp.meta)

        if show_config:
            config_exp = st.expander("Pipeline config.cfg")
            config_exp.code(nlp.config.to_str())

    st.sidebar.markdown(
        FOOTER,
        unsafe_allow_html=True,
    )
