# Python program to retrieve info about a file from TGAAC:Chronicles wrt the translation project

import json
import sys

def bslash_to_fslash(s: str):
    return "/".join(s.split("\\"))

def main(filepath: str):
    # Make file path relative to game folder
    filepath = filepath.split("nativeDX11x64")[1]
    filename = filepath.split("\\")[-1]
    path = filepath.split(filename)[0]
    path = bslash_to_fslash(path)[:-1] # slice gets rid of trailing slash
    data = json.load(open("fileinfo.json"))
    selected_data = [entry for entry in data["Altered Files"] 
                     if entry["filename"]==filename and entry["path"]==path]

    if len(selected_data) == 0:
        print("No data found for this file.\nIt may be that the file will be translated in future, or it may contain no text to translate.")
    else:
        print("File Info:")
        for key in selected_data[0]:
            print(str(key) + ": " + str(selected_data[0][key]))
        
    input("\nPress enter to exit.\n")
    return

if __name__ == "__main__":
    filepath = sys.argv[1]
    main(filepath)
