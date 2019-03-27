#!/usr/bin/python3
# https://github.com/supermasita/wrapmediainfo

import xml.etree.ElementTree
import subprocess
mediainfo_binary = "/usr/bin/mediainfo"


def help():
    """
    Prints information about how to use the command. Returns string.
    """
    print("Usage: wrapmediainfo.py -f {filename}")
    exit(1)


def media_metadata_extract(filename):
    """
    Parses media metadata. Returns dictionary. 
    """
    mediainfo_dict = {}
    try:
        command = "%s --Output=file://.mediainfo.tpl %s" % (
            mediainfo_binary, filename)

        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True, timeout=3,
            universal_newlines=True)
    except subprocess.CalledProcessError as e:
        mediainfo_dict["status"] = e.returncode
        mediainfo_dict["filesize"] = 0
        mediainfo_dict["filename"] = filename
    else:
        mediainfo_dict["status"] = 0
        root = xml.etree.ElementTree.fromstring(output)
        for child_of_root in root:
            for grandchild_of_root in child_of_root:
                mediainfo_dict[grandchild_of_root.tag] = grandchild_of_root.text

    return mediainfo_dict


# Use from command line
if __name__ == '__main__':

    import sys
    import getopt

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "f:")

    if not opts:
        help()

    for opt, arg in opts:
        if opt == "-f":
            filename = arg

    mediainfo_dict = media_metadata_extract(filename)

    print(mediainfo_dict)
