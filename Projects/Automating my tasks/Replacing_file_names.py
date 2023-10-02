# Noted:
# 1 - you will need to install ffmpeg onto your PC and allow it to be found in your environment path
#       Because I ran this on VSC and not PyCharm, there is no extension readily available for ffmpeg
# 2 - ffmpeg requires the file to have no spaces, so you have to adjust the name to not have them


import os


def remove_old_file(f_n, old_ext):
    if old_ext in f_n:
        os.remove(f_n)


def ffmpeg_opertaion(file_name, new_ext):
    f_name, f_ext = os.path.splitext(file_name)
    new_file = f_name + new_ext
    print(f_name, f_ext, new_file)
    os.system(
        f"""ffmpeg -i {file_name} -vn -ar 44100 -ac 2 -b:a 192k {new_file}""")


def reverting_names(file_name):
    original = file_name.replace("-", " ")
    os.replace(file_name, original)


def adjusting_file_name(file_name, old_extention, new_extention):
    adjust_name = file_name.replace(" ", "-")
    os.replace(file_name, adjust_name)
    file_name, file_ext = os.path.splitext(file_name)


def main():
    print("Hello, what is the file directory:")
    directory = input()
    directory.replace('\\', '\\\\')
    os.chdir(directory)

    print("What file type do you want to replace [without '.']: ")
    old_ext = '.' + input()

    print("What file type do you want to replace [without '.']: ")
    new_ext = '.' + input()

    print("Do you want to delete the original file: [Y/N]")
    remove_old = True if input().upper() == 'Y' else False

    print("------------ Adjust Name ------------")
    for f_n in os.listdir():
        adjusting_file_name(f_n, old_ext, new_ext)

    print("------------ Converting Codec ------------")
    for f_n in os.listdir():
        ffmpeg_opertaion(f_n, new_ext)

    print("------------ Reverting Name ------------")
    for f_n in os.listdir():
        reverting_names(f_n)

    if remove_old == True:
        print("------------ Deleting Old Files ------------")
        for f_n in os.listdir():
            remove_old_file(f_n, old_ext)


if __name__ == "__main__":
    main()
