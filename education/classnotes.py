"""

source code for the 'class notes' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderClassnotesPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'class notes' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 0: intro ---

        st.write(
            """
            One of my more recent "mini" projects is creating an archive-style repository of all the notes/homework 
            from my classes, both so that I can look back on them later and so that others can use them in their own 
            studies. Feel free to look around!
            """
        )

        # --- section 1: drive embed ---

        st.markdown(
            """
            <iframe 
            src="https://drive.google.com/embeddedfolderview?id=1rv0GFVqEEd_-pZMyiA0ZV001Yg4GA_g7#list" 
            style="width:100%; 
            height:600px; 
            border:0;"></iframe>""",
            unsafe_allow_html=True
        )

# #for testing purposes
# thingy = RenderClassnotesPage()
# thingy.run()