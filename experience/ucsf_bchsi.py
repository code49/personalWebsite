"""

source code for the 'ucsf bchsi' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderUCSFBakarPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'ucsf bchsi' page.

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
            ## UCSF BCHSI
            _unpaid programming intern, June - August 2020_
            
            ---
            """
        )

        # --- section 1: intro ---

        st.image("./resources/experience/ucsf_building.jpg")

        st.write(
            """
            The Bakar Computational Health Sciences Institute (BCHSI) is a division of the University of California
            San Francisco dedicated to applying computational tools to help solve medical problems, from helping 
            process sound data used to image living hearts to building models to understand how genetics impact
            common diseases.
            \n
            At UCSF, I worked on Philter, an open-source project dedicated to de-identifying 
            clinical notes (text documents doctors write during patient visits to note both quantitative and qualitative observations). 
            Through de-identifying these notes by removing personal health information 
            (names, locations, dates, etc.), the data in these notes could be made more 
            widely available for study, all while protecting the privacy of patients.
            """
        )

        # --- section 2: what I did ---

        st.markdown(
            """
            My project revolved around creating a post-processing algorithm for Philter's de-identified output. Initially,
            Philter simply marked each case of identifying information with a standardised tag (e.g. [\*\*\*NAME\*\*\*] where a
            patient's name was listed) in the text. This could lead to issues of privacy in cases where Philter has a false-negative 
            (i.e. fails to detect a phrase as identifying information, as would happen roughly 1 percent of the time), as the identity 
            of the patient would be quickly revealed.

            I was charged with writing software to replace these censoring tags with randomised data, helping to hide these 
            false-positives "in plain sight." In order to keep the 'camouflage' intact, therefore, it was important to ensure that
            this data matched the context of the original identifying information.
            """
        )

        st.image("./resources/experience/ucsf_bchsi_example.png")
        st.caption("_a sample personal information replacement my algorithm made on a clinical note, with identified and replaced tags color highlighted._")

        st.markdown(
            """
            My algorithm supported a host of identifying information types, from names to dates, phone numbers, even various random
            locations around the Bay Area. This project not only challenged me in terms of complexity, but also in terms of scale. The
            program had to run over the i2b2 clinical notes test dataset, which contains nearly 2 million notes (and that was just the proof 
            of concept!), so efficiency and simplicity were key considerations, particularly as the size of i2b2 pales in comparison to 
            the number of clinical notes generated by the UCSF healthcare system, where Philter was intended to be used. 
            """
        )

        # --- section 3: non-technical learnings ---

        st.write(
            """
            Aside from using data libraries such as pandas and numpy on a large scale for the first time, my time at
            UCSF also allowed me to get a first-hand look at the forefront of computational biology research, as well
            as the dynamics within a large research institution such as UCSF. It was fantastic seeing how the tools I
            had learned about in class translated into solving real-world problems, and how a diverse group of developers,
            researchers, even doctors can come together to work towards a collective end goal.
            """
        )

        # --- section 4: skills used ---

        st.markdown(
            """
            ---
            _skills I used:_
            
            - Python
                - pandas
                - numpy
                - spacy NLP
            """
        )

# for testing purposes
thing = RenderUCSFBakarPage()
thing.run()