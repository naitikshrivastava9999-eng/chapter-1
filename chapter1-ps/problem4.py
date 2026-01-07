import os


directory_path = "/chapter 1/chapter1-ps/" 
""


try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
