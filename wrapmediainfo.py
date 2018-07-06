#!/usr/bin/python3
# https://github.com/supermasita/wrapmediainfo 

# Adjust to your system config
mediainfoBin = "/usr/bin/mediainfo"

# 
from subprocess import Popen, PIPE
import xml.etree.ElementTree


def help():
    """
    Prints information about how to use the command. Returns string.
    """
    print("Usage: wrapmediainfo.py -f {filename}")
    exit(1)

def mediaMetadataExtract(filename):
    """
    Parses media metadata. Returns dictionary. 
    """
    command = [mediainfoBin, "--Output=file://.mediainfo.tpl", filename]
    p = Popen(command, stdout=PIPE)
    p.wait()

    data = p.stdout.read()
    p.stdout.close()
    data = data.decode("utf-8")

    root = xml.etree.ElementTree.fromstring(data)

    mediainfoDict = {}

    for child_of_root in root:
        for grandchild_of_root in child_of_root:
            mediainfoDict[grandchild_of_root.tag] = grandchild_of_root.text

    
    return mediainfoDict


# Use from command line
if __name__ == '__main__':

    import sys
    import getopt    

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "f:")

    if not opts :
        help()
    
    for opt, arg in opts :
        if opt == "-f" :
            filename = arg
    
    mediainfoDict = mediaMetadataExtract(filename)

    print(mediainfoDict)

