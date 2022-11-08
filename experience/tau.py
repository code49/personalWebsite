"""

source code for the 'tau' page of the webiste.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
import hydralit_components as hc

from hydralit import HydraHeadApp

# ----- code -----

# wrapper class
class RenderTauPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'tau motors' page.

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
            ## Tau Motors
            _paid programming + electronics development intern_ \n
            _June - August 2022_
            
            ---
            """
        )

        # --- section 1: intro ---

        st.image("./resources/experience/tau_header.jpg")
        
        st.write(
            """
            Tau Motors is a Redwood City based startup using a combination of hardware and
            software tools to create wound-field electric motors. Through a pipeline
            that combines automatic model testing (via FEA modeling software) with physical bench
            tests, Tau has the ability to generate designs optimised to reduce rare earth materials,
            energy consumption, and cost.
            """
        )

        # --- section 2: what I did ---

        st.write(
            """
            At Tau, I got the opportunity to help with both software and hardware sides of the company.
            On the software side, I learned to use Python libraries such as streamlit to create an inventory
            management system to streamline circuit board development, as prototype boards often took long times
            to fabricate due to not having enough parts. In terms of hardware, I helped to both build (applying
            solder masks, placing surface-mount parts, reflowing boards, and soldering connectors and other pieces)
            and test high voltage power management circuits for prototype motor designs. I also learned 
            how to navigate and use circuit board development programs such as KiCAD, as well as new electrical 
            engineering concepts such as complex impedance and power bridges.
            """
        )

        st.image("./resources/experience/tau_work.jpg")

        # --- section 3: non-technical learnings ---

        st.write(
            """
            Like at Vestaboard, my time at Tau was dominated by new learnings about the nature of
            startup culture, watching as the team pulled in resources to quickly understand and address problems. 
            I also benefited from close (COVID-free!) access to the small team to learn about many different aspects 
            of the company, from how test benches are chosen and programmed to minimise energy usage to how differences 
            in how FEA programs interpolate shapes between defined data points can affect test results. In addition, being 
            in person meant that I could get a lot of personal advice from the kind and friendly team, such as what they 
            wished known at the start of their careers, college clubs to look into, and even some insights on how to 
            fix issues with my car (which some of them had helped design).
            """
        )

        # --- section 4: skills used ---

        st.write(
            """
            _skills I used:_

            - software development
                - pandas/SQLite backend
                - streamlit frontend
            - hardware development
                - KiCAD (PCB development software)
                - solder masks and placing surface mount electronics components
                - reflow ovens (circuit board construction)
                - testing methodologies for high voltage circuits
                - "advanced" EE concepts, such as complex impedance
            """
        )

# # for testing purposes
# thing = RenderTauPage()
# thing.run()