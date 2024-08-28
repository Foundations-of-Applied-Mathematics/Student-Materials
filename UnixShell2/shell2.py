# shell2.py
"""Volume 3: Unix Shell 2.
<Name>
<Class>
<Date>
"""

import os
import subprocess
from glob import glob

# Problem 3
def grep(target_string, file_pattern):
    """Find all files in the current directory or its subdirectories that
    match the file pattern, then determine which ones contain the target
    string.

    Parameters:
        target_string (str): A string to search for in the files whose names
            match the file_pattern.
        file_pattern (str): Specifies which files to search.

    Returns:
        matched_files (list): list of the filenames that matched the file
               pattern AND the target string.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def largest_files(n):
    """Return a list of the n largest files in the current directory or its
    subdirectories (from largest to smallest).
    """
    raise NotImplementedError("Problem 4 Incomplete")
