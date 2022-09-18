# ----- intro -----

"""
This file is meant to straightforwardly implement multithreading support
for various purposes, mostly things like tkinter and running menus and backgroun tasks at the same time.
"""

# ----- import necessary libraries -----

import threading  # for threading, duh :)
import os  # for getting process data

# ----- threading class -----


class threader(object):

    def __init__(self):
        self.threads = list()

    def createThread(self, function_to_run, *args, **kwargs):
        """
        Creates a thread for a given process, with given arguments.

        Parameters:
        -----------

        function_to_run: function
            function object (remember not to call it with parentheses, just the reference instead)

        *args: arguments
            unnamed arguments to pass to function_to_run()

        **kwargs: keyword arguments
            named arguments to pass to function_to_run()

        Returns:
        --------

        None
        """
        temp_thread_pid = None

        def bigFunction(self):
            global temp_thread_pid
            function_to_run(*args, **kwargs)
            temp_thread_pid = os.getpid()

        thread = threading.Thread(
            target=bigFunction, name=function_to_run.__name__)
        thread.start()

        self.threads.append({
            "thread": thread,
            "task": function_to_run.__name__,
            "id": temp_thread_pid
        })

    def getThreads(self):
        """
        Gets the name (function) and process_id of all currently running threads and prints them out.

        Parameters:
        -----------

        None

        Returns:
        --------

        thread_info_list: list
            list containing dictionaries for each thread; dictionaries will have the following format:
            {"task": thread_task, "id": thread_pid}
        """

        # do some pre-formatting
        string_list = ["the following are the currently running threads:",
                       "format: thread:process id", ""]
        for i in range(0, len(self.threads)):
            thread = self.threads[i]
            task = thread["task"]
            id = thread["id"]
            string_list.append(f"{i}. {task}: {id}")

        # print out the lines as requested
        self.final.blankLine()
        self.final.dashedFormattedLine(string_list)
        for string in string_list:
            print(string)
        self.final.dashedFormattedLine(string_list)
        self.final.blankLine()

        # return a list of the threads' names and pids
        thread_info_list = []
        for thread in self.threads:
            thread_info_list.append({
                "task": thread["task"],
                "id": thread["id"]
            })
        return thread_info_list

    def exitOnThreadEnd(self):
        """
        Exits the program upon completion of all threads.

        Parameters:
        -----------

        None

        Returns:
        --------

        None
        """

        for thread in self.threads:
            thread.join()
        exit
