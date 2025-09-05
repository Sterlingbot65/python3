def modify_file(input_file, output_file):
    try:
        # Open and read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified file written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



input_filename = "original.txt"
output_filename = "modified.txt"

modify_file(input_filename, output_filename)
