# sync.py

import sys
import importlib
import re
#from collections import OrderedDict

ollama_common = importlib.import_module("ollama-common")
#phrases = OrderedDict(ollama_common.phrases) # Preserve order from incoming object
phrases = ollama_common.phrases

def remove_initial_hash_from_file(phrases):
    pathToRoot = "../../../"
    if len(sys.argv[1]) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'
    for filename, phrase_list in phrases.items():
        print() # Blank line
        print(f"\rProcessing file: {pathToRoot}{filename}")

        # Read lines from the file
        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        # Process the lines to remove initial '#' where necessary
        updated_lines = []
        for line in lines:
            stripped_line = re.sub(r'^\s*#', '', line, 1).rstrip() # Remove initial spaces and '#' and then any trailing spaces
            print() # Blank line
            print(f"LINE: {stripped_line}")
            for phrase in phrase_list:
                print(f"{phrase}")
                if stripped_line == phrase:
                    print(f"Found: {phrase}")
                    if re.match(r'^\s*#', line): # If # is either the first character in the line or is preceded only by whitespace
                        updated_lines.append(line.replace('#', '', 1))  # Remove the initial '#' and retain spaces
                    else:
                        updated_lines.append(line)
                    break
            else:
                updated_lines.append(line)

        # Write the updated lines back to the file
        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

# Call the function to process all files listed in the phrases dictionary
remove_initial_hash_from_file(phrases)

