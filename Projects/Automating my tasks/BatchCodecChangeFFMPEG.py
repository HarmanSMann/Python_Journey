import os
import subprocess

def remove_old_file(file_name, old_ext):
    """
    Removes the file if it has the specified old extension.
    """
    if file_name.endswith(old_ext):
        try:
            os.remove(file_name)
            print(f"Deleted old file: {file_name}")
        except OSError as e:
            print(f"Error deleting file {file_name}: {e}")

def ffmpeg_operation(file_name, new_ext):
    """
    Converts the file to the new extension using ffmpeg.
    """
    base_name, old_ext = os.path.splitext(file_name)
    new_file = base_name + new_ext
    print(f"Converting {file_name} to {new_file}")
    try:
        subprocess.run(
            ["ffmpeg", "-i", file_name, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", new_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg error: {e}")

def revert_name(file_name):
    """
    Reverts the hyphenated file name back to its original name with spaces.
    """
    original_name = file_name.replace("-", " ")
    if original_name != file_name:
        try:
            os.rename(file_name, original_name)
            print(f"Reverted {file_name} to {original_name}")
        except OSError as e:
            print(f"Error renaming file {file_name}: {e}")

def adjust_file_name(file_name):
    """
    Replaces spaces with hyphens in the file name.
    """
    adjusted_name = file_name.replace(" ", "-")
    if adjusted_name != file_name:
        try:
            os.rename(file_name, adjusted_name)
            print(f"Adjusted {file_name} to {adjusted_name}")
        except OSError as e:
            print(f"Error renaming file {file_name}: {e}")

def main():
    """
    Main function to handle user inputs and perform file operations.
    """
    # Get directory input from user
    directory = input("Enter the file directory: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory. Please enter a valid directory.")
        return
    
    os.chdir(directory)
    
    # Get old and new file extensions
    old_ext = '.' + input("Enter the old file extension (without '.'): ").strip()
    new_ext = '.' + input("Enter the new file extension (without '.'): ").strip()
    
    # Check if original files should be deleted
    remove_old = input("Do you want to delete the original files? [Y/N]: ").strip().upper() == 'Y'
    
    # Adjust file names to have no spaces
    print("------------ Adjusting File Names ------------")
    for file_name in os.listdir():
        if file_name.endswith(old_ext):
            adjust_file_name(file_name)
    
    # Convert files using ffmpeg
    print("------------ Converting Files ------------")
    for file_name in os.listdir():
        if file_name.endswith(old_ext):
            ffmpeg_operation(file_name, new_ext)
    
    # Revert file names to original
    print("------------ Reverting File Names ------------")
    for file_name in os.listdir():
        if file_name.endswith(new_ext):
            revert_name(file_name)
    
    # Remove old files if requested
    if remove_old:
        print("------------ Deleting Old Files ------------")
        for file_name in os.listdir():
            remove_old_file(file_name, old_ext)

if __name__ == "__main__":
    main()
