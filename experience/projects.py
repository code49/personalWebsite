"""

source code for the 'projects' page of the webiste.

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
class RenderProjectsPage(HydraHeadApp):

    # page render function
    def run(self):

        """
        
        handles creating the streamlit/hydralit components for the 'projects' page.

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
            ## projects
            
            ---

            I find working on side projects to be exciting and a great way of learning things from their practical applications
            that classes simply can't cover given their focus on conceptual understanding of specifically outlined objectives.
            This page is meant to serve as a record of the projects I've worked on or are currently working on that I find to be
            most interesting, as well as some of the things I learned:

            ---
            """
        )

        # --- section 1: racecar ---

        # st.image("./resources/experience/racecar.jpg")

        st.write(
            """
            I'm currently working as a part of Carnegie Mellon's FSAE electric race car team on the energetics (electronics,
            both high and low voltage) subteam. We're currently working on designing and fabraicating the 'backplane,' 
            a circuit board that connects the grounded low voltage system together, for 23e, our team's submission for 
            the 2023 FSAE (and other similar competition) circuits. So far, I've been learning about how the many systems 
            of a race car integrate together, from radios to battery management circuitry, and it's been exciting to see how
            motors like the ones I helped design at Tau can come together to create a high-performance vehicle like the ones
            our team makes.

            ---
            """
        )

        # --- section 2: project iginte ---
        
        st.image("./resources/experience/projectignite.png")

        st.write(
            """
            I'm also currently working as a mentor for project ignite, a club hosting yearly project collaborations
            with local Pittsburgh high schools. Project selections and high school applications are still in progress, but the 
            current plan is to work with another mentor to teach high schoolers about the fundamentals of tools such 
            as python and arduino to build 'robotic animals' that can respond to physical inputs (light, buttons, etc.), perhaps
            in addition to a companion IoT app on a computer. More updates to come soon!

            ---
            """
        )

        # --- section 3: spotipy ---

        st.image("./resources/experience/spotipy.png")

        st.write(
            """
            In spring and summer of 2021, I worked with a friend, Theo Rode (@TheSharkhead2 on github!), to create a 
            python-based wrapper of the Spotipy library for gathering data from the Spotify API. We worked to address
            issues we found when trying to use Spotipy, such as random re-authentication requests, confusing and messy
            data, and a lack of error handling for common situations such as paused playback. By learning about how to 
            address these difficulties, I learned about function wrappers in python as well as the many intricacies of
            building API-dependent applications.

            ---
            """
        )

        # --- section 4: COVID-19 book ---

        st.image("./resources/experience/lahm.jpg")

        st.write(
            """
            From September of 2018 to April of 2020, I volunteered at the Los Altos History Museum to help maintain their
            model railroad exhibit of my hometown. Given my fascination with model trains and the fact that I used to frequent
            the local museum when I was younger, I was overjoyed to get to help, helping pick and calibrate new train models when 
            the old ones broke, fix fuse circuitry after a storm created a surge, even put in elbow grease to clean the tracks
            from the oxides that build up when electricity flows from the rails to the wheels of the locomotives.
            
            ---
            """
        )

        # --- section 5: Taiwan ---

        st.image("./resources/experience/taiwan.jpg")

        st.write(
            """
            In the summer of 2018, I travelled to Taiwan alongside a group of other high school-level students to teach English to
            young children there. Over the course of 4 weeks, we visited a total of 5 schools all around the country, teaching everything
            from compound words (pictured above) to the basics of sentence structures, even helped them communicate their interests in
            pets and video games such as League of Legends. Teaching classes, however basic, was a "trial-by-fire" for me, requiring that
            I quikcly learn how to listen to the concerns and misunderstandings of the students, pick interesting activities, even learn about
            the difference in education culture between my experiences in America versus theirs in Taiwan. 

            In addition to teaching classes, we often spent free time experiencing other aspects of life there, from learning how to play with
            空竹 (Chinese yo-yos) to the arduous 5 AM-heavy lifestyles of taro farmers in the region. This trip was truly an eye-opening
            experience for me, and I am grateful for the opportunity to have gone and the lessons I learned there.
            """
        )

# # for testing purpsoes
# thing = RenderProjectsPage()
# thing.run()
