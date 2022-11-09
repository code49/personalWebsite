"""

source code for the 'about' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

class RenderAboutPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'about' page.

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
            ## hi there!
            """
        )

        # --- section 1: intro ---

        columns = st.columns([2, 5, 2])

        with columns[1]:
            st.image(
                image="./resources/about/portrait.jpg",
                caption="that's me! thanks to my friend's mom for taking nice photos :)",
            )

        st.write(
            """
            I'm David, an electrical and computer engineering student from the Bay Area in California.
            I'm currently studying at Carnegie Mellon University (c/o 2026) in the college of engineering.

            I'm interested in building cool things, whether it be at my desk with my keyboard and VS Code or
            at the lab with a soldering iron and oscilliscope. To me, creating and implementing ideas
            is the best way to learn new and unusual things, going beyond the standardised content classes
            have to teach. 

            --- 
            """
        )

        # --- section 2: website info ---

        st.write(
            """
            #### what's this about a website?

            This site is meant as a catalogue of all the projects I've done,
            as well as a way for me to look back at all the neat experiences I've had, fantastic people I've met,
            and valuable lessons I've learned over the years. 

            It's built on ``streamlit`` and ``hydralit``, libraries for creating webpages in Python.
            Technically, it's mostly meant for creating data visualisations and queries (which is
            what I was building at Tau Motors, where I learned about these tools), but since when
            did programmers use things the way they were intended? 

            That being said, because these libraries weren't really designed for full-scale web development,
            there are some design limitations. Hopefully more features will be added to streamlit/hydralit soon,
            so that this site can finally act the way I want it to. 

            [Here](https://github.com/code49/personalWebsite) is the link to the GitHub repo for the 
            project if you want to take a look around. Feel free to contact me with suggestions/ideas!

            ---
            """
        )

        # --- section 3: contact ---

        st.write(
            """
            #### wow! you seem really cool!

            Well, maybe that's not what you're thinking right now. 
            
            But either way, I'd love to chat! Meeting new people is always an eye-opening experience for me, and my 
            ideas have been inspired by everything from my model train tracks to those nets they put on large fruit 
            in Asian supermarkets. I'd be thrilled to talk about suggestions for the site, things I might be able
            to work with you on, or anything else!

            Here's my contact info:
            - davidlechan@gmail.com
            - +1 (650) - 383 - 8954 
            - [linkedin.com/in/david-le-chan](https://linkedin.com/in/david-le-chan)
            """
        )

#for testing purposes
thingy = RenderAboutPage()
thingy.run() 
