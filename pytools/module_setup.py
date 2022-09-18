# ----- intro -----

"""
This is just meant to be a file that ensures the project is properly set up each time the program is run - this is just done by ensuring pip is setup,
and then installing modules as necessary.

Credit to @ArtOfWarfare on stackOverflow for this solution:
    I've just very lightly modified the functions he's shared here: https://stackoverflow.com/posts/25643988/revisions
"""

# ----- check the module_setup.json file to see whether modules even need to be  -----

import json  # this is to read the .json file
import time  # this is just to add some delays to make the terminal window more


def moduleSetup(module_list: list) -> None:
    """

    sets up required libraries, downloading pip if necessary.

    Parameters:
    -----------

    module_list: list
        list containing strings representing the names of required libraries for the script.

    Returns:
    --------

    None

    """

    print("module installation: checking previous installs.")
    
    with open('./python_dev_tools/setup_status.json') as file:
        data = json.load(file)
        
    if not data["module_setup_status"]:

        print("module installation: this project has not been set up yet. installing modules now.")

        # ----- import baseline library stuff -----

        # for using python/pip to install pip and other needed modules
        from subprocess import call
        # for removing the get-pip.py file after having installed pip, name is for ensuring correct pipPath for different OS
        from os import remove, name
        # from urllib import urlretrieve #for getting get-pip.py file from the internet
        from urllib.request import urlretrieve
        from os.path import isfile, join  # for dealing with pip's filepath
        # this gets the filepath prefix for the system, for example C: on windows
        from sys import prefix
        # used to get the pip.exe filepath on unix-based systems
        from subprocess import Popen, PIPE
        # this is used to check to see if the package is already installed
        from pkgutil import iter_modules

        # ----- ensure correct pip setup -----

        # function that installs pip and cleans up the get-pip.py file afterward
        def installPip():

            urlretrieve("https://bootstrap.pypa.io/get-pip.py",
                        "get-pip.py")  # get get-pip.py file from online
            # run the .py file to install pip
            call(["python", "get-pip.py"])
            # remove the file to clean up the mess
            remove("get-pip.py")

        # function that returns the pip executable and installs pip if it cannot find it
        def getPip():

            # find the pip.exe filepath, depending on OS type
            if name == "nt":  # windows
                pipPath = join(prefix, 'Scripts', 'pip.exe')
            else:  # unix
                finder = Popen(['which', 'pip'],
                               stdout=PIPE, stderr=PIPE)
                pipPath = finder.communicate()[0].strip()

            # check if pip is installed, install it if not
            if not isfile(pipPath):
                installPip()
                if not isfile(pipPath):
                    raise NameError(
                        "failed to find/install pip, try manually installing pip and trying again, or if that doesn't work manually set pipPath to the pip.exe filepath.")

            return pipPath

        # ----- function that installs a given necessary module -----

        def installIfNeeded(module_pip_name):

            try:  # ideally, pip should be able to find the module needed based on the given name, but in some cases the name might be wrong, and that should raise an error
                if module_pip_name not in [tuple_[1] for tuple_ in iter_modules()]:
                    print(
                        f"{module_pip_name} has not been installed. Installing the module now.")
                    call([getPip(), "install", module_pip_name])

                    print(f"{module_pip_name} has been installed.")

            except:  # this will raise an error if pip can't install the module for some reason
                raise KeyError(
                    f"failed to install module {module_pip_name}. check that the module name is correct and then try again.")

        # ----- running the two functions -----

        getPip()
        for module in module_list:
            installIfNeeded(module)

        # ----- update setup_status.json -----

        with open('./python_dev_tools/setup_status.json', 'r') as file:
            data = json.load(file)
        new_data = {
            "module_setup_status": True
        }
        with open('./python_dev_tools/setup_status.json', 'w') as file:
            data = json.dump(new_data, file)

        print("the project is now set up, you should not need to do this again.")
        time.sleep(2)

        import os
        os.system('cls||clear')
