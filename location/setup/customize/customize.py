#customize.py

import sys
import importlib
import re
import os

# Import phrases from file-lines.py
file_lines = importlib.import_module("file-lines")
phrases = file_lines.phrases

def adding_ollama_lines(phrases):
    pathToRoot = "../../../"
    if len(sys.argv[1]) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'

    # Process each file and its associated phrases
    for filename, phrase_list in phrases.items():
        file_path = pathToRoot + filename
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist. Skipping.")
            continue
        print(f"Processing file: {pathToRoot}{filename}")

        # Read lines from the file
        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        skip_block = False  # Used for cypress.config.ts processing
        revert_block = False  # Used for chat.cy.ts processing

        for line in lines:
            stripped_line = line.strip()

            # Add the initial hash tag if the phrase matches
            for phrase in phrase_list:
                if stripped_line == phrase:
                    print(f"Found: {phrase}")
                    if not re.match(r'^\s*#', line):  # If the line does NOT start with a #, add it back
                        updated_lines.append(f"# {line}")
                    else:
                        updated_lines.append(line)
                    break
            else:
                updated_lines.append(line)

            # Process specific files
            if filename == "cypress.config.ts":
                # Handle block skipping logic for env block
                if "env:" in line:
                    skip_block = True  # Start skipping lines
                elif "}" in line and skip_block:
                    skip_block = False  # End of the env block
                    continue  # Do not add the closing bracket for the env block
                elif not skip_block:
                    updated_lines.append(line)

            if filename == "chat.cy.ts":
                # Handle reverting beforeEach block in chat.cy.ts
                if "beforeEach(() => {" in stripped_line:
                    revert_block = True
                    # Replace the arrow function block with the original block from phrases
                    updated_lines.extend(phrases["chat.cy.ts"])
                    continue  # Skip lines until the original block is fully replaced

                elif revert_block and "});" in stripped_line:
                    revert_block = False  # End of the beforeEach block
                    continue  # Skip the closing bracket of the arrow function block

                if not revert_block:
                    updated_lines.append(line)

        # Write the updated lines back to the file
        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

# Call the function to process all files listed in the phrases dictionary
adding_ollama_lines(phrases)
