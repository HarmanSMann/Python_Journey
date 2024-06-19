import os

def rename_file(file, replace_ext, cut_off):
    """
    Renames a file based on the given cut-off string and file extension.

    Parameters:
    - file (str): The name of the file to rename.
    - replace_ext (str): The file extension to filter files. If None, all files are processed.
    - cut_off (str): The substring in the file name where the cut-off should occur.
    """
    file_name, file_ext = os.path.splitext(file)
    
    # Check if the file extension matches or if no extension filtering is applied
    if replace_ext is None or replace_ext == file_ext[1:]:
        print(f"Attempting to rename file: {file_name}{file_ext}")
        old_name = file_name
        head, sep, trailing = old_name.partition(cut_off)
        
        # Remove trailing space if exists
        if head.endswith(' '):
            print("Trailing space detected")
            file_name = head[:-1]
        else:
            file_name = head
        
        # Rename file only if name has changed
        if file_name != old_name:
            new_name = f'{file_name}{file_ext}'
            try:
                os.rename(file, new_name)
                print(f"Renamed to: {new_name}")
            except Exception as e:
                print(f"Error renaming file {file}: {e}")
        else:
            print(f"Skipped file, '{cut_off}' not detected")

def main():
    """
    Main function to prompt user inputs and rename files in the specified directory.
    """
    # Get directory input from user
    directory = input("Enter the file directory: ").strip()
    
    # Validate and process the directory path
    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid directory.")
        return
    
    # Change to the target directory
    os.chdir(directory)
    
    # Get the cut-off string from user
    cut_off = input("Enter the cut-off point: ").strip()
    
    # Get file extension filtering preference from user
    replace_ext_condition = input("Any specific file types? [Y/N]: ").strip().upper()
    
    replace_ext = None
    if replace_ext_condition == "Y":
        replace_ext = input("Enter the file extension (without dot): ").strip()
    
    # Process each file in the directory
    for file in os.listdir():
        if os.path.isfile(file):
            rename_file(file, replace_ext, cut_off)

if __name__ == "__main__":
    main()
