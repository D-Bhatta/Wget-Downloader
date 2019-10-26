# Wget-Downloader
Downloads a list of links and stores them in folders from a list of folder names

## Usage

    Wget_downloader.py "links.txt" "names.txt"

Here, links.txt contains all the links to be downloaded. Also, names.txt contains all the folder names the links will be downloaded into.  
Eaxmple:

### "links.txt"  
    link1.com
    link2.com
    ...
    link999.com

### "names.txt"
    link1
    link2
    ...
    link999

## Boundary Cases:
1. File Not found
2. File is empty
3. internet not available
4. can't write to directory

## Tests
1. All files are downloaded
2. Correct files in correct order
3. Passing boundary cases without error
4. Load tests