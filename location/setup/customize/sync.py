# sync.py

import sys
import importlib
import re
#from collections import OrderedDict

ollama_common = importlib.import_module("ollama-common")
#phrases = OrderedDict(ollama_common.phrases) # Preserve order from incoming object
phrases = ollama_common.phrases

def removing_ollama_lines(phrases):
    pathToRoot = "../../../"
    if len(sys.argv[1]) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'

    # Process each file and its associated phrases
    for filename, phrase_list in phrases.items():
        print() #Blank Line
        print(f"\rProcessing file: {pathToRoot}{filename}")

        # Read lines from the file
        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        # Process the lines to remove initial '#' where necessary
        updated_lines = []
        skip_block = False  # Used for cypress.config.ts processing
        revert_block = False  # Used for chat.cy.ts processing

        for line in lines:
            stripped_line = re.sub(r'^\s*#', '', line, 1).rstrip()  # Remove initial spaces and '#'
            print(f"LINE: {stripped_line}")

            # Remove the initial hash tag if found in phrases
            for phrase in phrase_list:
                if stripped_line == phrase:
                    print(f"Found: {phrase}")
                    if re.match(r'^\s*#', line):  # If the line starts with a # or is preceded only by whitespace
                        updated_lines.append(line.replace('#', '', 1))  # Remove the initial '#' and retain spaces
                    else:
                        updated_lines.append(line)
                    break
            else:
                updated_lines.append(line)

            # Process specific files
            if filename == "cypress.config.ts":
                # Handle block skipping logic for env block
                if "env:" in line:
                    skip_block = True
                    updated_lines.append(line)
                elif "}" in line and skip_block:
                    skip_block = False  # End of the env block, stop skipping
                elif not skip_block:
                    updated_lines.append(line)

            if filename == "chat.cy.ts":
                # Handle reverting beforeEach block in chat.cy.ts
                if "beforeEach(function ()" in line:
                    revert_block = True
                    updated_lines.append(line.replace('function ()', '()'))  # Replace function with arrow function
                elif revert_block and "});" in line:
                    revert_block = False  # End of the beforeEach block
                    updated_lines.append(line)
                elif not revert_block:
                    updated_lines.append(line)

        # Write the updated lines back to the file
        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

# Call the function to process all files listed in the phrases dictionary
removing_ollama_lines(phrases)