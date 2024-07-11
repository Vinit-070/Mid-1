import os
import sys

def delete_files_except(directory, extensions, script_path):
    # Convert extensions to a set for faster lookups
    extensions = {ext.lower() for ext in extensions}
    
    # Walk through all files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            file_ext = os.path.splitext(file)[1].lower()
            file_path = os.path.join(root, file)
            
            # Delete the file if its extension is not in the given extensions and it is not the script itself
            if file_ext not in extensions and file_path != script_path:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

if __name__ == "__main__":
    # Get the current script path
    script_path = os.path.abspath(__file__)
    
    # Get the directory path from the user
    directory = input("Enter the directory path (or 'default' to use the current directory): ").strip()
    
    # Use the current directory if the user enters "default"
    if directory.lower() == "default":
        directory = os.getcwd()
    
    # Get the file extensions from the user and split them into a list
    extensions_input = input("Enter the file extensions to keep (comma-separated, e.g., .txt,.jpg,.pdf): ").strip()
    extensions = [ext.strip() for ext in extensions_input.split(",")]

    # Call the function to delete files
    delete_files_except(directory, extensions, script_path)
