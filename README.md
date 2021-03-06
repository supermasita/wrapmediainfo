# wrapmediainfo
## A very simple Python wrapper for Mediainfo 

[![Build Status](https://travis-ci.org/supermasita/wrapmediainfo.svg?branch=master)](https://travis-ci.org/supermasita/wrapmediainfo)

It uses the Mediainfo's templating functionality to try to get the following information:
- 'displayAspectRatio'
- 'filesize'
- 'audioBitrate'
- 'videoBitrate'
- 'videoFormatProfile'
- 'audioLanguage'
- 'subLanguage'
- 'subCodec'
- 'height'
- 'width'
- 'audioCodec'
- 'videoCodec'
- 'audioChannels'
- 'audioFormat'
- 'videoFormat'
- 'duration'

### Requirements:
- [Mediainfo](https://mediaarea.net/en/MediaInfo)
- Tested on Ubuntu with Python 3

### Configuration:
If Mediainfo is intalled in a different path, edit wrapmediainfo.py and change
``` python
# Adjust to your system config
mediainfoBin = "/usr/bin/mediainfo"
```

### How to use:
- In a script: Call function "mediaMetadataExtract" with the filename as parameter. Metadata will be parsed and you will get a dictionary.
- From command line:
```
$ python3 wrapmediainfo.py -f "Sample_Big_Buck_Bunny_Trailer_(HD)_(Source).flv"
  {'videoCodec': 'On2 VP6', 'videoFormatProfile': None, 'videoFormat': 'VP6', 'audioBitrate': '64000', 'filename': 'Sample_Big_Buck_Bunny_Trailer_(HD)_(Source).flv', 'displayAspectRatio': '16:9', 'duration': '33049', 'audioLanguage': None, 'audioChannels': '2', 'audioCodec': 'MPEG-1 Audio layer 3', 'videoBitrate': '2720694', 'filesize': '11582028', 'width': '1280', 'height': '720', 'status': 0}
```

### Error handling:
- Non media files will show an output similar to this and *will not be considered failed* (note 'status'):
```
{'filename': 'README.md', 'filesize': '1488', 'duration': None, 'status': 0}
```
- Non existent files will show an output similat to this and *will be considered failed* (note 'status'): 
```
{'filesize': 0, 'filename': 'i_dont_exist', 'status': 1}
```

