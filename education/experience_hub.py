"""

source code for the 'experience hub' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderExperienceHubPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'experience hub' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 1: CMU ---

        cols = st.columns([2, 2, 4, 2])
        
        # image
        with cols[1]:

            pass

        # description
        with cols[2]:

            pass

        