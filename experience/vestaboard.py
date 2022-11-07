"""

source code for the 'ucsf bchsi' page of the webiste.

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
class RenderVestaboardPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'vestaboard' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 0: title ---

        st.markdown(
            """
            ## Vestaboard:
            _paid programming intern_
            _June - August 2021_
            """
        )

        # --- section 1: intro ---

        st.image("./resources/experience/vestaboard_header")
        
        st.write(
            """
            Vestaboard is a startup based in South San Francisco building smart split-flap display boards,
            combining the look and sound of a old-timey train station while integrating all the smarts of
            modern day technology.
            """
        )

# for testing purposes
thing = RenderVestaboardPage()
thing.run()