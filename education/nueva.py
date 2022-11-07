"""

source code for the 'nueva' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderNuevaPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'nueva' page.

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
            ## The Nueva School
            _high school student, August 2018 - June 2022_

            [school website](https://www.nuevaschool.org/)
            
            ---
            """
        )

        # --- section 1: intro ---

        st.image("./resources/education/nueva_header.jpg")

        st.write(
            """
            I went to The Nueva School in San Mateo, California for high school. I was fortunate
            to get to take a wide variety of classes in everything from machine learning, where
            I learned about how mathematics can act like a light to guide us through
            the darkness of big data, to global health dynamics, where I learned about the different 
            factors that impact health policy across the world. I'm so glad to have gotten to meet
            so many influential students and faculty, and am excited to act as an alumni representative
            for the class of 2022. 
            """
        )

        # --- section 2: class list ---

        st.write(
            """
            Here's a list of the classes I took there, organised by subject area:

            - Programming/Computer Science
                - CS320: Advanced Machine Learning
                - CS310: Introduction to Machine Learning
                - CS240: Computer Security
                - CS223: Introduction to Algorithms
                - CS120: Mobile App Design
                - CS110: Introduction to Computer Programming
            - Engineering
                - EFD385: Advanced Mechanical Engineering
                - EFD285: Introduction to Mechanical Engineering
                - EFD241: History of Technology (Steel, Telescopes, and Trains)
                - EFD190: Introduction to Mechatronics
            - Mathematics
                - MATH540: Applied Statistics and Probability
                - MATH520: Multi-Variable Calculus
                - MATH401: Single-Variable Calculus
                - MATH301: Math 3 (pre-calculus)
                - MATH201: Math 2 (geometry, trigonometry, algebra II)
            - Sciences
                - Physics
                    - PHYS250: Modern Physics
                    - PHYS101: Fundamentals of Physics
                - Biology
                    - BIO301: Changing Global Health Dynamics
                    - BIO101: Fundamentals of Biology
                - Chemistry
                    - CHEM230: Bio-organic Chemistry
                    - CHEM101: Fundamentals of Chemistry
            - Social Sciences
                - Economics
                    - ECON210: Environmental Economics
                    - ECON101: Microeconomics
                - History
                    - HIST301: U.S. History
                    - HIST201: Modern World History
                    - HIST101: Ancient World History
            - Humanities
                - Foreign Language
                    - CHIN550: Advanced Topics in Chinese
                    - CHIN501: Chinese 5
                    - CHIN401: Chinese 4
                - English
                    - ENG450: Shakespeare in the World
                    - ENG401: Advanced Literature Seminar
                    - ENG301: English 11
                    - ENG201: English 10
                    - ENG101: English 9
            - Arts
                - MUS210: Soundwaves
            """
        )

        # --- section 4: shout-out ---
        st.write(
            """
            _Special shout-out to teachers Barak Yedidia and John Feland, whose guidance helped me find
            my passion for electrical engineering, programming, and physics, and whose teaching inspires
            me each and every day to help others understand the world. Thank you so much for all the support 
            over the years!_
            """
        )


# #for testing purposes
# thing=RenderNuevaPage()
# thing.run()
