import os
import shutil

# Ejecutables 
# Excel
# Pdf
# Imagenes

from_dir = "C:/Users/MaxFa/Documents/Byjus/C102"
to_dir = "C:/Users/MaxFa/Downloads/Act"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    if extension == "":
        continue

    if extension in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "ImageFiles" 
        path3 = to_dir + "/" + "ImageFiles" + "/" + filename
    if os.path.exists(path2):
        print("Moviendo el Archivo: " + filename)
        shutil.move(path1, path3)
    else:
        os.mkdir(path2)
        print("Moviendo el Archivo: " + filename)
        shutil.move(path1, path3)