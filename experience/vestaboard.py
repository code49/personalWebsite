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
            _paid programming intern_ \n
            _June - August 2021_
            
            ---
            """
        )

        # --- section 1: intro ---

        st.image("./resources/experience/vestaboard_header.jpg")
        
        st.write(
            """
            Vestaboard is a startup based in South San Francisco building smart split-flap display boards,
            combining the looks and sounds of a cruicial element of old-timey train station while integrating 
            all the smarts of modern day technology. Users can use their Vestaboard to write a message to their 
            kids when away on business, see live sports scores, even be inspired by quotes from celebrities 
            and influencers.
            """)

        # --- section 2: what I did ---

        st.write(
            """
            I worked at Vestaboard to implement Word-Of-The-Day, an "installable" (plugins that control
            the board, automatically collecting data from the internet to generate messages) that polled the 
            English Oxford Dictionary's word of the day to display to the board. Creating my installable
            required that I write many new features, including RSS feeds, pagination (getting the server
            to queue and send a group of messages in order, since definitions took more space than a single 'frame'
            on the board), and progress bars.
            """
        )

        st.image("./resources/experience/vestaboard_improvements.png")



# for testing purposes
thing = RenderVestaboardPage()
thing.run()