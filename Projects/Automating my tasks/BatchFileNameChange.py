# Modifications based on the sample code from here:
# https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/?ref=rp

import os


def renameFile(f, replace_ext, replace_ext_condition, cut_off):
    # split the file naming convention
    file_name, file_ext = os.path.splitext(f)

    # check if file name matters
    if replace_ext == None or replace_ext == file_ext[1:]:
        print("Attempting file name change: " + file_name + file_ext)
        oldname = file_name
        head, sep, trailing = oldname.partition(cut_off)
        if head[len(head) - 1] == ' ':
            print("end SPACE detected")
            file_name = head[:-1]
        else:
            file_name = head
        # check if the name has been changed so you dont overwrite something that doesnt have to be
        if file_name != oldname:
            new_name = f'{file_name}{file_ext}'
            os.replace(f, new_name)
            print("new file names: " + file_name)
        else:
            print("Skipped file, '" + cut_off + "' not detected")


def main():
    # some starter code:
    # Grab some information: directory, where you want to end it, and optionally file extention if they want to only change a few files with the same suffix
    print("Hello, what is the file directory:")
    directory = input()
    # covert \ because coding confusions and how it is used
    directory.replace('\\', '\\\\')
    os.chdir(directory)

    # for example: all my files say "something - remove me.extention"
    # I would then select the point to be '-'
    print("Where do you want the cut off point to be to start: ")
    cut_off = input()

    print("Any specific file types? [Y/N]: ")
    replace_ext_condition = input()

    replace_ext = None
    if replace_ext_condition.upper() == "Y":
        print("What type: ")
        replace_ext = input()

    for f in os.listdir():
        renameFile(f, replace_ext, replace_ext_condition, cut_off)


if __name__ == "__main__":
    main()
