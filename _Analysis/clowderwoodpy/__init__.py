# Created: 2024/05/24 08:16:45
# Last modified: 2024/06/24 09:20:35
#
""" Clowderwood Python scripts

Provides helpers for analyzing Clowderwood data using

Returns:
    _type_: _description_
"""

from pathlib import Path
import fnmatch
from .json2dict import json2dict

THIS_PACKAGE = "clowderwoodpy"
THIS_VERSION = "0.0.1"

CW_DATA_FILE = "../config/clowderwoodDataFile.json"
CW_DATA_LABEL = "../config/clowderwoodDataLabels.json"
CW_EXTENSION_FILE = "../config/fileExtensions.json"


def cw_start(verbose=False):
    """
    Load CW_DATA_FILE, which lists the different data source directories for different
    states in processing. Convert the paths to absolute. Optionally, explain the data
    dictionary.

    Args:
        verbose (bool, optional): Indicate whether to print explanations. Defaults to False.

    Returns:
        cwDataDict: Dictionary containing the configuration data.
    """

    try:
        cwDataDict = json2dict(CW_DATA_FILE)
        rootAPath = Path(__file__).resolve().parents[2]
        for source, paths in cwDataDict.items():
            for state, rel_path in paths.items():
                if isinstance(rel_path, list):
                    abs_paths = [(rootAPath / path).resolve() for path in rel_path]
                    cwDataDict[source][state] = [str(path) for path in abs_paths]
                else:
                    abs_path = (rootAPath / rel_path).resolve()
                    cwDataDict[source][state] = str(abs_path)

        cwLabelDict = json2dict(CW_DATA_LABEL)

        if verbose:
            # Print explanations about the data
            #      0         1         2         3         4         5         6         7
            print("\nWelcome to", THIS_PACKAGE, "v", THIS_VERSION, ".\n")
            print(
                " This initialization has loaded a dictionary which contains the current \n",
                "raw, processed, and summarized data locations. The dictionary is\n",
                "organized by sensor or source classes, as the first level key:",
            )
            #    0         1         2         3         4         5         6         7
            pathTypeSet = set()
            for source in cwDataDict.keys():
                print("\t", source)
                pathTypeSet = pathTypeSet.union(set(cwDataDict[source].keys()))
            #      0         1         2         3         4         5         6         7
            print(
                "\n Each sensor has directories for different data processing states. These\n",
                "directories include the following, with the caution that not all sources\n",
                "have all data processing states. These are the second level key:",
            )
            #    0         1         2         3         4         5         6         7
            for state in pathTypeSet:
                print("\t", state)
            print(
                "\n In preparing the dictionary the paths are converted to absolute \n",
                "paths from the values recorded in",
                CW_DATA_FILE,
                ".",
            )

        return cwDataDict, cwLabelDict
    except ImportError as e:
        print(f"{THIS_PACKAGE} v {THIS_VERSION} failed to load data locations: {e}")
        return None


def getCW_DATA_FILEList(dataFileDictionary, source, stateDirs):
    """
    Given the cwDataDict and specific source and stateDir keys, get a list
    of appropriately extensioned files in the directories.

    Parameters:
    - dataFileDictionary: produced by cwStart
    - source: first level key in dataFileDictionary
    - stateDirs: second level key in dataFileDictionary

    Returns:
    - fileList: List of files with appropriate extensions.
    """

    fileList = []
    fileExtensionDict = json2dict(CW_EXTENSION_FILE)
    fileExtension = fileExtensionDict[stateDirs]

    if isinstance(dataFileDictionary[source][stateDirs], list):
        for directory in dataFileDictionary[source][stateDirs]:
            directory_path = Path(directory).resolve()
            tmpList = [
                str(file)
                for file in directory_path.glob("*")
                if fnmatch.fnmatch(file.name.lower(), f"*{fileExtension}")
            ]
            fileList = fileList + tmpList
    else:
        directory = dataFileDictionary[source][stateDirs]
        directory_path = Path(directory).resolve()
        fileList = [
            str(file)
            for file in directory_path.glob("*")
            if fnmatch.fnmatch(file.name.lower(), f"*{fileExtension}")
        ]

    return fileList
