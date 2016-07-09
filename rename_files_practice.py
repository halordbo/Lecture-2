import os
def rename_files():
    # (1) get file names in a folder
    file_names = os.listdir(r"C:\Users\tom-lab\Desktop\prank\prank")
    print (file_names)
    saved_path= os.getcwd()
    print (saved_path)
    os.chdir(r"C:\Users\tom-lab\Desktop\prank\prank")
    # (2) rename all file
    for names in file_names:
        #write your code here
    
    os.chdir(saved_path)

rename_files() 
