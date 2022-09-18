# ----- intro -----

"""
This file is for automatically loading settings from the .env file.  
"""

# ----- load environment variables -----

# setup dotenv properly
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
print(find_dotenv())
load_dotenv(find_dotenv())

# ----- create function to return environment variables to main file -----


def getSettings(settings_list):
    """
    Function that extracts settings from a .env file

    Parameters
    ----------

    settings_list: list
        list of strings containing each setting's name

    Returns
    -------

    settings: dict
        dictionary of settings

    """
    settings = {}
    for setting in settings_list:
        settings[setting] = os.getenv(setting)

    return settings
