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

import 

# ----- load environment variables -----

settings = settings.getSettings([])

# ----- completion message -----

clear()
time.sleep(1)
messager.info("setup complete.")
messager.info(f"----- new {os.path.basename(__file__)} run -----")

# ----- code -----

# because we are running in hydralit/streamlit; there isn't the typical 'if __main__ main()' paradigm


