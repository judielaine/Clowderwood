# json2Dict
#
# Created: 2024/05/24 08:16:45
# Last modified: 2024/06/23 11:24:33
# 

import json
import os
import sys
import magic

def json2dict(json_file):
    """
    Load a json file into a dictionary.
    
    Parameters:
    - json_file: Path to the json file.
    
    Returns:
    - dataDict: Dictionary containing json data
    
    Raises:
    - FileNotFoundError: If the config file does not exist.
    - json.JSONDecodeError: If the file is not valid JSON.
 
    """

    thisPath = os.path.abspath(__file__)
    dataDict = {}
    
    try:
        with open(json_file, 'r') as file:
            dataDict = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"{thisPath}\n did not find {json_file}: {e}")
    except json.JSONDecodeError as e:
        fileMagic = magic.from_file(json_file)
        raise ValueError(f"{thisPath}\n did not decode JSON from {json_file},\n which is type {fileMagic}.\n{e}")
    except Exception as e:
        raise Exception (f"{thisPath}\n had error parsing JSON with {json_file}: {e}")

    return dataDict