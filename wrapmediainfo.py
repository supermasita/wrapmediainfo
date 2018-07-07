#!/usr/bin/python3
# https://github.com/supermasita/wrapmediainfo 

# Adjust to your system config
mediainfoBin = "/usr/bin/mediainfo"

# 
#from subprocess import Popen, PIPE
import subprocess
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
    mediainfoDict = {}
    try:
        command = "%s --Output=file://.mediainfo.tpl %s" % (mediainfoBin, filename)

        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True, timeout=3,
            universal_newlines=True)

    except subprocess.CalledProcessError as e:
       mediainfoDict["status"] = e.returncode
       mediainfoDict["filesize"] = 0
       mediainfoDict["filename"] = filename
    else:
       mediainfoDict["status"] = 0
       root = xml.etree.ElementTree.fromstring(output)
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

