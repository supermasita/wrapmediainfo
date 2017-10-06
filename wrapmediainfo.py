#!/usr/bin/python3

mediainfoBin = "/usr/bin/mediainfo"


from subprocess import Popen, PIPE
import xml.etree.ElementTree


def mediaMetadataExtract(filename):
    """ 
    """
    command = [mediainfoBin, "--Output=file://mediainfotemplate.txt", filename]
    p = Popen(command, stdout=PIPE)
    p.wait()

    data = p.stdout.read()
    p.stdout.close()
    data = data.decode("utf-8")

    root = xml.etree.ElementTree.fromstring(data)

    #print(root.tag, root.attrib)
    
    for child in root:
        #print(child.tag, child.attrib)
        duration = int(child.find('duration').text)


    return duration


# Use from command line
if __name__ == '__main__':

    import sys
    import getopt    

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "f:")
    
    for opt, arg in opts :
        if opt == "-f" :
            filename = arg
    
    duration = mediaMetadataExtract(filename)

    print(duration)

    #print(filename)
    #print("videoCodecType ", mediaMetadata.videoCodecType)
    #print("videoBitrate ", mediaMetadata.videoBitrate)
    #print("videoWidth ", mediaMetadata.videoWidth)
    #print("videoHeight ", mediaMetadata.videoHeight) 
    #print("videoCodecName ", mediaMetadata.videoCodecName)
    #print("duration ", mediaMetadata.duration)
    #print("size ", mediaMetadata.size)
    #print("totalBitrate ", mediaMetadata.totalBitrate)
    #print("fileFormat ", mediaMetadata.fileFormat)
    #print("audioCodecType ", mediaMetadata.audioCodecType)
    #print("audioBitrate ", mediaMetadata.audioBitrate)
    #print("audioCodecName ", mediaMetadata.audioCodecName)


