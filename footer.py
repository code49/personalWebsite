"""

function definitions for creating standardised footers to streamlit/hydralit pages.

"""

# ----- import libraries -----

# streamlit/hydralit
import streamlit as st
# import hydralit as hy # there's a bug with hydralit so disabling for now
import hydralit_components as hc

# ----- code -----


# page footer render function
def renderFooter():

    """

    handles creating the streamlit/hydralit components for the footer section of each page.
    
    Parameters:
    -----------

    None

    Returns:
    --------

    None

    """
    
    # horizontal rule
    st.markdown("---")

    # markdowns with centering html
    st.markdown(
        """
        <p style='text-align: center; color: grey;'> <span style="font-size: 12px"> 
        <em> "Guess what? You're going to wake up tomorrow and have an absolutely phenomenal day. 
        And if your day isn't phenomenal, it'll still be better than today." </em> - Celine "starsmitten" Cheung 
        </span></p>
        """, 
        unsafe_allow_html=True
    )
    st.write("") # for spacing
    st.markdown(
        """
        <p style='text-align: center; color: grey;'> <span style="font-size: 15px">
        David Le Chan<br>
        davidlechan@gmail.com<br>
        +1 (650)-383-8954<br>
        <a href="https://linkedin.com/in/david-le-chan"> linkedin.com/in/david-le-chan </a>
        </span></p>
        """, 
        unsafe_allow_html=True
    )
    # st.markdown(
    #     """
    #     <p style='text-align: center; color: grey;'> <span style="font-size: 15px">
    #     davidlechan@gmail.com
    #     </span></p>
    #     """, 
    #     unsafe_allow_html=True
    # )
    # st.markdown(
    #     """
    #     <p style='text-align: center; color: grey;'> <span style="font-size: 15px">
    #     +1 (650) - 383 - 8954
    #     </span></p>
    #     """, 
    #     unsafe_allow_html=True
    # )
    # st.markdown(
    #     """
    #     <p style='text-align: center; color: grey;'> <span style="font-size: 15px">
    #     <a href="https://linkedin.com/in/david-le-chan"> linkedin.com/in/david-le-chan </a>
    #     </span></p>
    #     """, 
    #     unsafe_allow_html=True
    # )