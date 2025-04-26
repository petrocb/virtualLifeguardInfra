import os


def process_files_in_folder(folder_path):
    # Create the output folder
    output_folder = os.path.join(folder_path, "edited")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a .txt file
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(folder_path, file_name)
            output_file_path = os.path.join(output_folder, file_name)

            # Process the file
            with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
                for line in infile:
                    # Split the line into columns
                    columns = line.strip().split()
                    # Ensure there is data to process
                    if not columns:
                        continue

                    # Get the first column value as an integer
                    first_col = int(columns[0])

                    # Apply the rules
                    if first_col == 0:
                        # Write the line as is
                        outfile.write(line)
                    elif first_col == 14:
                        # Change the first column to 0 and write the line
                        columns[0] = "0"
                        outfile.write(" ".join(columns) + "\n")
                    # Lines with other values are skipped (not written to the output)


# Specify the folder path to process
folder_path = r"C:\Users\petro\Desktop\trainingData"  # Replace with your folder path

# Call the function
process_files_in_folder(folder_path)
