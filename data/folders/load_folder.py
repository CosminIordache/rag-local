import os, glob
from langchain_community.document_loaders import UnstructuredFileLoader


folder = "/home/cosmin/VSCode/git_backend"

# The ** pattern matches all directories and subdirectories, and * matches all files. The glob.glob function returns a list of matching paths.
folder = glob.glob(os.path.join(folder, '**', '*'), recursive=True)
folder = [path for path in folder if os.path.isfile(path) and 'node_modules' not in path]

# i = index of the current element in the list & p = value of the current element in the list
for i, p in enumerate(folder):
    # Check if the current file path ends with any of the specified file extensions.
    if p.endswith(('.pyc')):
        continue

    print('Current file path:', p)

    try:
        loader = UnstructuredFileLoader(p)
        # Use the DirectoryLoader to load the files in the folder
        documents = loader.load()
        #print(documents)
    except Exception as e:
                print(f"Error loading file {p}")
                print(e)
    