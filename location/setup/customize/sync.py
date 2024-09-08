import sys
import importlib
import re

# Importing phrases from file-lines.py (adjust the path based on your structure)
ollama_common = importlib.import_module("file_lines")
phrases = ollama_common.phrases

def remove_initial_hash_from_file(phrases):
    pathToRoot = "../../../"
    if len(sys.argv[1]) > 1:
        pathToRoot = sys.argv[1]
        if not pathToRoot.endswith('/'):
            pathToRoot += '/'
    
    # Process each file listed in 'phrases'
    for filename, phrase_list in phrases.items():
        print()  # Blank line
        print(f"Processing file: {pathToRoot}{filename}")

        # Read lines from the file
        with open(pathToRoot + filename, 'r') as file:
            lines = file.readlines()

        # Process the lines to remove blocks or individual lines
        updated_lines = []
        skip_block = False  # Flag to track if we are in a block to be removed

        for i, line in enumerate(lines):
            stripped_line = line.strip()

            # Check if we are currently skipping a block
            if skip_block:
                # If we're at the end of a block, stop skipping
                if stripped_line == '}':
                    skip_block = False
                # Skip the line
                continue

            # Check if the current line starts a block that needs to be removed
            for phrase in phrase_list:
                # If the phrase matches the start of a block (like 'env: {')
                if stripped_line == phrase:
                    # If this is the start of a block, set the skip flag
                    if stripped_line.endswith('{'):
                        skip_block = True
                        break
                    # If it's a single line phrase, skip just this line
                    elif stripped_line == phrase:
                        print(f"Skipping line: {stripped_line}")
                        break
            else:
                # If no match, add the line to the updated lines
                updated_lines.append(line)

        # Write the updated lines back to the file
        with open(pathToRoot + filename, 'w') as file:
            file.writelines(updated_lines)

# Call the function to process all files listed in the phrases dictionary
remove_initial_hash_from_file(phrases)


