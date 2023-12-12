"""

source code for the 'cmu' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderCarnegiePage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'cmu' page.

        Parameters:
        -----------

        None

        Returns:
        --------

        None

        """

        # --- section 0: header section ---

        st.markdown(
            """
            ## Carnegie Mellon University
            _undergraduate student, August 2022 - May 2026+ (projected)_

            [school website](https://www.cmu.edu/)
            
            ---
            """
        )

        # --- section 1: intro ---

        st.image("./resources/education/cmu_header.jpg")

        st.write(
            """
            I'm currently at Carnegie Mellon University in Pittshurgh, Pennsylvania studying
            in the college of engineering. Although undeclared until April 2023, I intend on 
            studying electrical and computer engineering, finishing my undergraduate studies 
            in the summer of 2026.
            """
        )

        # --- section 2: class list ---

        st.write(
            """
            Here's a list of the classes I've taken at CMU so far, organised by subject area:

            - Engineering
                - 12-100: Introduction to Civil and Environmental Engineering
                - 18-100: Introduction to Electrical and Computer Engineering
                - 18-240: Structure and Design of Digital Systems
            - Computer Sciences
                - 15-122: Principles of Imperative Computation
            - Mathematics
                - 21-120: Differential and Integral Calculus
                - 21-122: Integral and Approximate Calculus
                - 21-127: Concepts of Mathematics
                - 36-219: Introduction to Probability Theory and Random Processes
            - Sciences
                - Physics
                    - 33-141: Physics I for Engineers
                    - 33-142: Physics II for Engineers
            - Humanities
                - Design
                    - 51-173: Human Experiences in Design
                - Law
                    - 66-215: The Innovation Trials
                - English
                    - 76-106: Writing about Data
                    - 76-108: Writing about Public Problems

            """
        )


# #for testing purposes
# thing=RenderCarnegiePage()
# thing.run()