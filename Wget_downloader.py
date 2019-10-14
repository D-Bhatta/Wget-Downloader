import WgetDownloader

def main(argv):
    [lo_, hi_] = argv[1:3]
    filename1, filename2 = str(lo_), str(hi_)
    #filename1 = "links.txt"
    #filename2 = "names.txt"
    download = WgetDownloader.WgetDownloader(filename1,filename2)
    download.download()

if __name__ == "__main__":
    def _script_io():
        from sys import argv
        main(argv)
    _script_io()