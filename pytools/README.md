# python-dev-tools (pytools)

![project banner image](readmebanner.png)

## purpose:

The purpose of this project is to create a simple, easy-to-use set of commonly-used tools for python program development. This includes many features, from differentiating different use-cases of print statements (i.e. ones needed for debugging vs. ones needed in the final program) to automatically installing PyPI modules straight from the internet.

---

## directory directory:

This is meant to be a simple guide to the directory.

    | pytools/ ; overarching repo directory
    -----| .env ; file containing user-specific environment variables like api keys, secrets, etc.
    -----| main.py ; "main" jumping off file for new programs
    -----| settings.py ; for importing environment variables into the main file
    -----| pytools/ ; sub-directory for the actual 'tools' for the project
    ----------| messager_output/ ; sub-directory for saving project output logs
    ---------------| all/ ; sub-directory for all-encompassing output logs
    --------------------| all.log.<some_number> ; all-encompassing log files, capped at 500 mb
    ---------------| warn_up/ ; sub-drectory for warning and more severe output logs
    --------------------| warn_up.log.<some_number> ; warning and more severe output log files, capped at 500 mb
    ----------| messager.py ; for printing/logging messages to the terminal and log-file system
    ----------| setup_status.json ; file containing data about whether the project has been set up
    ----------| threading.py ; file containing the class for easily creating and monitoring multi-thread programs
    ----------| __init__.py ; empty .py file needed to import classes into an outer directory

---

## project_template:

This is really meant to be a simple way of starting off using the development tools - it includes a basic structure of the files typically needed for a program such as settings and a main file. It also simply incorporates many of the features included in this toolkit, so you don't need to do any of the boring setup :)

---

## usage:

This section is meant to be a general guide on how to use the various tools of the python-dev-tools toolkit.

In general, tools can be used by instantiating an instance of the tool class and then calling tool methods accordingly.


### messager:

This is a tool meant to simplify terminal messaging and debugging/output logging for projects, powered by Python's logging library.

#### setup:

To setup the messager, import the `messagerSetup()`, `clear()`, and `horizontalRule()` functions directly from pytools.messager into the main file, ensuring dev_mode is set to False if desired (to remove "DEBUG"-type logs from the terminal). Then, create an instance of the messager (not a custom class, just a function returning the library-provided one) by calling the `messagerSetup()` function:

    from pytools.messager import messagerSetup, clear, horizontalRule
    logger = messagerSetup()

#### messages:

There are 5 types of messages to use. A broad-strokes breakdown:
    
    - DEBUG: for printing/logging messages useful in debugging or otherwise developing a project.
    - INFO: for typical 'everything-is-fine' program outputs.
    - WARNING: for minor, non-obtrusive error warnings.
    - ERROR: for medium-importance error warnings.
    - CRITICAL: for significant errors/problems.

*Check out the formal definitions + the logging library documentation [here](https://docs.python.org/3/howto/logging.html).*

Once set up, each can be called using a simple command from the logger instance:

    messager.debug("this is a debug-level message.")
    messager.info("this is a info-level message.")
    messager.warning("this is a warning-level message.")
    messager.error("this is a error-level message.")
    messager.critical("this is a critical-level message.")
    
Which nets something like this:

- [DEBUG] <04.25 10:52:07> main.py::main() (line 51): this is a debug-level message.
- [INFO] 10:52:07: this is a info-level message.
- [WARNING] <2022.04.25 10:52:07> main(): this is a warning-level message.
- [ERROR] <2022.04.25 10:52:07> main.py::main() (line 54): this is a error-level message.
- [CRITICAL] <2022.04.25 10:52:07> main.py::main() (line 55): this is a critical-level message.

#### log files:

In addition to pretty console printing, the messager automatically logs outputs to various files, found in the "messager_output" subdirectory. All messages are recorded to various log files in the "all" directory (the larger the number after the .log, the more recent the output), while messages of "WARNING" or more severe type are logged to files in the "warn_up" directory. Files are restricted to 500 mb to reduce memory loads by default, but the exact value can be configured within the messager.py file.

#### helpers:

There are also two helper functions for prettier terminal outputs, `clear()` and `horizontalRule()`. Hopefully the use of `clear()` is reasonably apparent. `horizontalRule()` creates a horizontal line as long as the console window by default, but can be custom-configured using `length=` and a non-negative integer as a parameter.

### module_setup:

This is perhaps the most useful feature of the entire toolkit. Essentially, it's a nice way to ensure that all external modules (installed from PyPI) are installed wihtout making users run lines from the command line; theoretically this could be solved using fancy AHK scripts, but I think this method is significantly cleaner and "more automatic". 

Using the feature is quite simple. First, you need to create a list of the PyPI modules you want to require. Ensure that the names are as listed in PyPI, not just the ones you use to import them - for example Python Image Library (PIL) is listed in PyPI as "Pillow" instead of "PIL". Because the tool will simply try to install the package using pip (meaning that it won't know that say, PIL is actually named Pillow when installing), this is very important.

Additionally, "python-dotenv" must always be required + installed in order for settings<area>.py to work properly.

An example of doing this:

    from pytools.moduleSetup import moduleSetup

    dev_mode = True #for whether dev_mode should be enabled or not
    module_list = [
        "python-dotenv", #remember that this is required for settings.py to work
        "url-lib3",
        "markupsafe",
        "other PyPI modules"
    ]

From there, call the function:

    moduleSetup(module_list, dev_mode)

and you're done. Simple, right? 

### threading:

This file is meant to simply add support for multithreading in your projects. Make sure to create an instance of threader() before using it. 

Each new parallel process can be added like this:

    threader.createThread(function_to_run, *args, **kwargs)

You can check which functions are currently running like this (threads are named by the function they run):

    threader.getThreads()

You can even set the whole program to end upon your threads finishing like so:

    threader.exitOnThreadEnd()
