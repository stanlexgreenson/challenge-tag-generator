# Generates a TXT file with all the tracks in the current directory and subdirectories.
# The generated file is formatted with the correct XML tag for challenges (excluding the <ident> tag)

import glob
import os

# Gets the absolute path of the directory where the script is executed.
path = os.getcwd()

track_extension = ".Challenge.Gbx"

# Used to slice the root path (where all the tracks are located)
root_dirname = "Tracks"

def get_tracks_paths(directory):
    
    tracks_paths = []
   
    for root, dirs, files in os.walk(directory):
        print("Currently walking on: "+ root)
        relative_track_path = root[root.index(root_dirname)+len(root_dirname)+1:]
        for file in files:
            if track_extension in file:
                tracks_paths.append(os.path.normpath(os.path.join(relative_track_path,file)))
            else:
                print("[SKIPPED] Not a Challenge file.")


    return tracks_paths


path_list = get_tracks_paths(path)
with open("challenges.txt", "w+") as txt:
    for track_path in path_list:
        txt.read()
        txt.write(
            "\t<challenge>\n"+
            "\t\t<file>"+track_path+"</file>\n"+
            "\t</challenge>\n"
            )

