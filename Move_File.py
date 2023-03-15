import os
import shutil

# from_dir = "/Users/nashwanhaque/Downloads"
from_dir = "/Users/nashwanhaque/Downloads"
document_dir = "/Users/nashwanhaque/Desktop/Downloaded_documents"
photo_dir = "/Users/nashwanhaque/Desktop/Downloaded_pictures"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir +'/'+file_name
        path2 = document_dir + '/' + "Document_files"
        path3 = document_dir + '/' + "Document_files" + '/' + file_name

        print("path1", path1)
        print("path2", path2) 
        print("path3", path3)

        if os.path.exists(path2):
            print("Moving" + file_name + "....")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "....")
            shutil.move(path1, path3)
    
    elif extension in ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.psd', '.ai', '.raw']:
        path1 = from_dir +'/'+file_name
        path2 = photo_dir + '/' + "Photo_files"
        path3 = photo_dir + '/' + "Photo_files" + '/' + file_name

        print("path1", path1)
        print("path2", path2) 
        print("path3", path3)

        if os.path.exists(path2):
            print("Moving" + file_name + "....")

            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving" + file_name + "....")
            shutil.move(path1, path3)
