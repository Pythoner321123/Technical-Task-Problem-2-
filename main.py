import os, shutil
dstFiles = []
srcFiles = []
src = r"D:\code\python\projects\testFolder\src"
dst = r"D:\code\python\projects\testFolder\dst"

def copy(source, destinatiun):
    for file in os.listdir(source):
        try:
            if os.path.isdir(os.path.join(source, file)):
                shutil.copytree(os.path.join(source, file), os.path.join(destinatiun, file))
        except FileExistsError:
            pass
        else:
            with open(f"{source}\\{file}", "rb") as f:
                    with open(f"{destinatiun}\\{file}", "wb") as dstf:
                        dstf.write(f.read())
              
for dstFile in os.listdir(dst):
    dstFiles.append(dstFile)
for srcFile in os.listdir(src):
    srcFiles.append(srcFile)

if len(srcFiles) != len(dstFiles):
        for srcFile in srcFiles:
            if srcFile not in dstFiles:
                copy(src, dst)   
        for dstFile in dstFiles:
            if dstFile not in srcFiles:
                copy(dst, src)
