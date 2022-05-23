import os, shutil

# Our lists
dstFiles = []
srcFiles = []
#------------
src = r"" # Provide the directory of your source folder inside of the quotation marks.
dst = r"" # Create a folder and then provide the directory of your destination folder inside the quotation.


# This is the main function, it takes in 2 arguments source and destination then copies files.
def copy(source, destinatiun):
    for file in os.listdir(source):
        try:
            if os.path.isdir(os.path.join(source, file)):
                shutil.copytree(os.path.join(source, file), os.path.join(destinatiun, file))
        except FileExistsError:
            print("Sorry, an error has occured. Pleaase try again.")
        except PermissionError:
            print("Sorry, an error has occured. Pleaase try again.")
        else:
            with open(f"{source}\\{file}", "rb") as f:
                with open(f"{destinatiun}\\{file}", "wb") as dstf:
                    dstf.write(f.read())

# These loops bellow are listing every file from the 2 directories then appending them to a list
for dstFile in os.listdir(dst):
    dstFiles.append(dstFile)
for srcFile in os.listdir(src):
    srcFiles.append(srcFile)

# These if statements are checking files and figuring out which directory is missing a file
# if there's a file missing they're "copying" and pasting that file into the directory
if len(srcFiles) != len(dstFiles):
    for srcFile in srcFiles:
        if srcFile not in dstFiles:
            copy(src, dst)
    for dstFile in dstFiles:
        if dstFile not in srcFiles:
            copy(dst, src)
