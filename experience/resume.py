"""

source code for the 'resume' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# other
import base64 # encode pdf for display

# ----- code -----

# wrapper class
class RenderResumePage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'resume' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 0: title ---

        st.write(
            """
            ## resume
        
            ---
            """
        )

        # --- section 1: intro ---

        st.write("Sometimes a short and concise resume is better. Here's mine!")

        # --- section 2: display pdf version ---

        st.write("") # for spacing

        # show pdf
        with open("./resources/experience/davidchan-resume.pdf", "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        # --- section 3: download buttons ---

        with open("./resources/experience/resume_digital.pdf", "rb") as pdf_file:
            PDF_byte_digital = pdf_file.read()

        st.download_button(
            label="Download Digital PDF",
            data=PDF_byte_digital,
            file_name='davidchan-resume-digital.pdf'
        )

        with open("./resources/experience/resume_printable.pdf", "rb") as pdf_file:
            PDF_byte_printable = pdf_file.read()

        st.download_button(
            label="Download Printable PDF",
            data=PDF_byte_printable,
            file_name='davidchan-resume-printable.pdf'
        )

        with open("./resources/experience/resume_simple.pdf", "rb") as pdf_file:
            PDF_byte_simple = pdf_file.read()

        st.download_button(
            label="Download Simple PDF",
            data=PDF_byte_simple,
            file_name='davidchan-resume-simple.pdf'
        )

# for testing purpsoes
thing = RenderResumePage()
thing.run()
