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

        # --- section 0: header + intro ---

        st.write(
            """
            ## class notes

            ---

            One of my more recent "mini" projects is creating an archive-style repository of all the notes 
            from my classes, both so that I can look back on them later and so that others can use them in their own 
            studies. Note that some are simply compilations of exam review sheets, as I didn't take formal notes
            about the material in the course. Here are a few of the most interesting ones, as well as a list of 
            all of the ones I have done so far.
            """
        )

        # --- section 1: drive embed ---

        st.markdown(
            """
            <iframe 
            src="https://drive.google.com/drive/folders/1Ni_yWcpKrmQ9Lyz6Fuxctz1KMv9KX1kC?usp=sharing" 
            style="width:100%; 
            height:600px; 
            border:0;"></iframe>""",
            unsafe_allow_html=True
        )


# #for testing purposes
# thingy = RenderClassnotesPage()
# thingy.run()
