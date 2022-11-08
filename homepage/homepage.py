"""

source code for the 'homepage' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderHomePage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'homepage' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 0: content ---

        columns = st.columns([1, 7, 1])

        with columns[1]:
            st.write(
                """
                ## Welcome!

                This site is meant as a catalogue of all the projects I've done,
                as well as a way for me to look back at all the neat experiences I've had, fantastic people I've met,
                and valuable lessons I've learned over the years. 

                Feel free to navigate around using the above bar, and I'd appreciate any feedback/ideas as well!
                """
            )

#for testing purposes
thingy = RenderHomePage()
thingy.run()
