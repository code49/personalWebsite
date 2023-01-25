"""

function definitions for creating standardised footers to streamlit/hydralit pages.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit as hy
import hydralit_components as hc

# python builtins
import json
import random
import base64
from pathlib import Path

# ----- code -----

# function converting images to base64 bytes
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# function converting images to the requisite html objects
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

# page footer render function
def renderFooter():

    """

    handles creating the streamlit/hydralit components for the footer section of each page.
    
    Parameters:
    -----------

    None

    Returns:
    --------

    None

    """
    
    # horizontal rule
    st.markdown("---")

    # gather random quote
    with open('quotes.json', 'r', encoding='utf-8') as in_file:
        possibilities = json.load(in_file)[:-1]
        quote_data = random.choice(possibilities)

    # markdowns with centering html
    st.markdown(
        f"""
        <p style='text-align: center; color: grey;'> <span style="font-size: 12px"> 
        <em>{quote_data["text"]}</em> - {quote_data["author"]} 
        </span></p>
        """, 
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style='text-align: center; color: grey;'> <span style="font-size: 15px">
        David Le Chan<br>
        davidlechan@gmail.com<br>
        +1 (650)-383-8954<br><br>
        <a href="https://linkedin.com/in/david-le-chan"> LinkedIn </a><br>
        <a href="https://github.com/code49"> GitHub </a>
        </span></p>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<p style='text-align: center; color: grey;'>" + img_to_html('image.png') + "</p>", unsafe_allow_html=True)