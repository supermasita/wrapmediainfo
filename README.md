# wrapmediainfo
A very simple Python wrapper for Mediainfo. 

It uses the Mediainfo's templating functionality to get the following information:
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


Requirements:
- Mediainfo

How to use:
- In a script: Call function "mediaMetadataExtract" with the filename as parameter. Metadata will be parsed and you will get a dictionary.
- From command line:

$ python wrapmediainfo.py -f "/home/mst/temporal/videos/Sample_Big_Buck_Bunny_Trailer_(HD)_(Source).flv"
{'videoCodec': 'On2 VP6', 'videoFormatProfile': None, 'videoFormat': 'VP6', 'audioBitrate': '64000', 'filename': '/home/mst/temporal/videos/Sample_Big_Buck_Bunny_Trailer_(HD)_(Source).flv', 'displayAspectRatio': '16:9', 'duration': '33049', 'audioLanguage': None, 'audioChannels': '2', 'audioCodec': 'MPEG-1 Audio layer 3', 'videoBitrate': '2720694', 'filesize': '11582028', 'width': '1280', 'height': '720'}
