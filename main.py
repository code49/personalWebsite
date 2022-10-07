# ----- intro -----

"""

main running file for code49's personal website.
hydralit/streamlit will run from here, pulling code for other pages from files.

"""

# ----- import required libraries -----

# required for the base script
import time
import os

# ----- import tool libraries from pytools

# import the setup routine to be run
from pytools.module_setup import moduleSetup
from pytools.messager import messagerSetup, clear, horizontalRule

# ----- define developer mode setting -----

dev_mode = True

# ----- messager setup -----

messager = messagerSetup(dev_mode=True, run_erase=False)

# ----- module setup -----

# add in strings of require-install modules here
module_list = [
    "python-dotenv",
    "streamlit",
    "hydralit",
    "hydralit_components"
]
moduleSetup(module_list)

# now that dotenv is ensured, import settings
import settings

# ----- import add-on libraries -----

import streamlit as st
import hydralit as hy
import hydralit_components as hc

# ----- load environment variables -----

settings = settings.getSettings([])

# ----- completion message -----

clear()
time.sleep(1)
messager.info("setup complete.")
messager.info(f"----- new {os.path.basename(__file__)} run -----")

# ----- code -----

if __name__ == '__main__':

    # --- setup streamlit, hydralit, hydralit navbar ---

    # setup streamlit page configuration
    st.set_page_config(
        page_title="david chan",
        page_icon="🚋",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            "Report a Bug": "mailto:davidlechan@gmail.com", #bug report url; setting this to email address
            "About": "I'm David, an ECE student. This is a website dedicated to some of the neat things I've been able to do over the years!"
        },
    )

    # create hydralit app
    app = hy.HydraApp(

        # page title/favicon
        title="david chan",
        favicon="🔺",
        
        # theme configuration
        navbar_theme={
            'txc_inactive': '#FFFFFF',
            'menu_background':'#C20101',
            'txc_active':'#000000',
            'option_active':'#F7F7F7'
        },
        # future feature: banner images?

        # setting configuration
        allow_url_nav=True,
        sidebar_state="collapsed",
        clear_cross_app_sessions=True,
        
    )

    # --- setup hydralit paging ---

    # wrapper class imports
    from experience.classnotes import RenderClassnotesPage
    from experience.resume import RenderResumePage

    # add sub-pages as apps to the main app

    app.add_app(
        title="classnotes",
        icon="✏️",
        app=RenderClassnotesPage()
    )

    app.add_app(
        title="resume",
        icon="📜",
        app=RenderResumePage()
    )

    app.run()