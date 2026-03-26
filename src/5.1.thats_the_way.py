import os

def files_deep(path):
    
    return [f for f in os.listdir(path) if f.startswith("deep")]


new_path = input("Enter a path : ")
print(files_deep(new_path))
