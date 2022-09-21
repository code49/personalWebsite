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

# because we are running in hydralit/streamlit; there isn't the typical 'if __main__ main()' paradigm

# --- setup hydralit, hydralit navbar ---

# create hydralit app
app = hy.HydraApp(

    # page title/favicon
    title="david chan",
    favicon="🔺",
    
    # theme configuration
    navbar_theme={
        'txc_inactive': '#FFFFFF',
        'menu_background':'#C20101',
        'txc_active':'#FFFFFF',
        'option_active':'#F7F7F7'
    },
    # future feature: banner images?

    # setting configuration
    allow_url_nav=True,
    sidebar_state="collapsed",
    clear_cross_app_sessions=True,
    
)

app.run()