# ----- intro -----

"""
This is the new and improved system for creating debug/output logs and terminal messages, using the logging library: 
https://docs.python.org/3/howto/logging.html
"""


# bundling into a function for easy import
def messagerSetup(dev_mode=True, run_erase=False):
    """

    bundles the logging library setup into a single function for simple importing into project files.

    Parameters:
    -----------

    dev_mode: bool (optional)
        boolean representing whether 'DEBUG'-type logs are printed to the console. defaults to True.

    run_erase: bool (optional)
        boolean representing whether log files are reset on each run (setup) of the program. defaults to False.

    Returns:
    --------

    logger: logging logger object
        logging logger object representing the configured logger object.

    """

    # ----- import necessary libraries -----

    import logging  # for messaging and automatic debug logging
    from logging.handlers import RotatingFileHandler
    import sys  # for console outputs
    import os  # for filesystem handling

    # ----- maximum log file size -----

    max_log_size_mb = 500  # making 0.5 gb the maximum log file size
    max_log_size_bytes = max_log_size_mb * (10 ^ 6)  # auto-conversion to bytes

    # ----- if log files exist and run_erase is true, erase them -----

    if run_erase:
        path_dir = './messager/'
        for suffix in ["all", "warn_up"]:
            for file in os.listdir(path_dir + suffix):
                os.remove(os.path.join(dir, file))

    # ----- create and configure an instance of the logger class -----
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)  # ensure that all message types are handled

    # ----- configure logging formats -----
    debug_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {filename}::{funcName}() (line {lineno}): {message}', datefmt='%m.%d %H:%M:%S', style='{')

    info_formatter = logging.Formatter(
        fmt='[{levelname}] {asctime}: {message}', datefmt='%H:%M:%S', style='{')

    warning_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {funcName}(): {message}', datefmt='%Y.%m.%d %H:%M:%S', style='{')

    critical_error_formatter = logging.Formatter(
        fmt='[{levelname}] <{asctime}> {filename}::{funcName}() (line {lineno}): {message}', datefmt='%Y.%m.%d %H:%M:%S', style='{')

    # ----- setup level filter -----

    class singleFilter(object):
        """

        class for filtering logs to singular levels. inspired by https://stackoverflow.com/questions/8162419/python-logging-specific-level-only.

        Parameters:
        -----------

        level: logging level attribute
            logging level attribute representing the level of log to filter to (e.g. logging.DEBUG).

        """

        def __init__(self, level):
            self.level = level

        def filter(self, record):
            return record.levelno == self.level

    class devModeFilter(object):
        """

        same as the singleFilter() class, but for filtering out 'DEBUG'-type logs from the terminal.

        Parameters:
        -----------

        dev_mode: bool 
            boolean representing whether 'DEBUG'-type logs are printed to the console. defaults to True.

        """

        def __init__(self, level, dev_mode):
            self.level = level
            self.dev_mode = dev_mode

        def filter(self, record):

            if dev_mode:
                return record.levelno == self.level
            else:
                return False

    # ----- setup console logger handlers -----

    # debug has to be done manually because of dev_mode
    console_debug_handler = logging.StreamHandler()
    console_debug_handler.setLevel(logging.DEBUG)
    console_debug_handler.addFilter(devModeFilter(logging.DEBUG, dev_mode))
    console_debug_handler.setFormatter(debug_formatter)
    console_debug_handler.setStream(sys.stdout)

    # for simplifying code to setup remaining console log handlers
    console_info_handler = logging.StreamHandler()
    console_warning_handler = logging.StreamHandler()
    console_error_handler = logging.StreamHandler()
    console_critical_handler = logging.StreamHandler()

    handler_list = [
        [console_info_handler, logging.INFO, info_formatter],
        [console_warning_handler, logging.WARNING, warning_formatter],
        [console_error_handler, logging.ERROR, critical_error_formatter],
        [console_critical_handler, logging.CRITICAL, critical_error_formatter]
    ]

    for entry in handler_list:
        entry[0].setLevel(entry[1])  # set the lower-bound level
        # restrict to lower-bound level
        entry[0].addFilter(singleFilter(entry[1]))
        entry[0].setFormatter(entry[2])  # set the format style
        entry[0].setStream(sys.stdout)  # set log to output to terminal

    # ----- setup file logger handlers -----

    file_all_handler = RotatingFileHandler(
        "./pytools/messager_output/all/all.log", maxBytes=max_log_size_bytes, backupCount=10)
    file_all_handler.setLevel(logging.DEBUG)
    file_all_handler.setFormatter(critical_error_formatter)

    file_warning_up_handler = RotatingFileHandler(
        "./pytools/messager_output/warn_up/warn_up.log", maxBytes=max_log_size_bytes, backupCount=10)
    file_warning_up_handler.setLevel(logging.WARNING)
    file_warning_up_handler.setFormatter(critical_error_formatter)

    # ----- add handlers to the logger -----

    logger.addHandler(console_debug_handler)
    logger.addHandler(console_info_handler)
    logger.addHandler(console_warning_handler)
    logger.addHandler(console_error_handler)
    logger.addHandler(console_critical_handler)
    logger.addHandler(file_all_handler)
    logger.addHandler(file_warning_up_handler)

    return logger


def clear() -> None:
    """

    clears the terminal window.

    Parameters:
    -----------

    None

    Returns:
    --------

    None

    """

    import os
    os.system('cls||clear')


def horizontalRule(length: int = 0) -> None:
    """

    function for creating horizontal rules across the terminal screen.

    Parameters:
    -----------

    length: int (optional)
        custom integer length (i.e. not the full width of the terminal) of the horizontal rule.

    """

    # prevent erroring by checking that length is an integer not < 0
    if (length < 0) or (not type(length) is int):
        raise TypeError(
            "horizontal rule length is not an integer greater than 0.")

    # get terminal width if no custom length has been set
    if length == 0:
        import os
        length = os.get_terminal_size.lines

    # create the rule string
    rule_string = ""
    for i in range(length):
        rule_string += "-"

    # print the rule string
    print(rule_string)
