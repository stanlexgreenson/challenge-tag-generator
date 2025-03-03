# Challenge Tag Generator

Generates a TXT file with all the tracks in the directory where the script is ran. It also searches subdirectories.

The intended usage of this script is to gather all tracks that the user wants to add to the match settings for TrackMania Forever servers.

The script expects to be inside of a directory named `Tracks` or any subdirectory inside it.

# Usage

You must have Python installed on your machine.

1. Place the script inside your `.../GameData/Tracks` folder or any subdirectory inside it.
2. Run the script.

A `challenges.txt` file will be generated containing challenge tags like this:

```
...
    <challenge>
        <file>track-path</file>
    </challenge>
...
```

>[!warning]
>This script has only been tested on Windows