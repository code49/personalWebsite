"""

source code for the 'resume' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
# import hydralit as hy # there's a bug with hydralit so disabling for now
import hydralit_components as hc

# other
import base64 # encode pdf for display

# ----- code -----

# page render function
def renderResume():

    """
    
    handles creating the streamlit/hydralit components for the 'resume' page.

    Parameters:
    -----------

    None

    Returns:
    --------

    None

    """

    # --- section 0: intro ---

    st.write("Sometimes a short and concise resume is better. Here's mine!")

    # --- section 1: display pdf version ---

    st.write("") # for spacing

    # show pdf
    with open("./resources/experience/davidchan-resume.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # --- section 2: download button ---

    with open("./resources/experience/davidchan-resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Download PDF",
        data=PDFbyte,
        file_name='davidchan-resume.pdf'
    )

renderResume()