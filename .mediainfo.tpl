# This file is used wrapmediainfo.py to generate the XML output from Mediainfo that afterwards parses 
General;<?xml version='1.0' encoding='UTF-8'?><file><track type='General'><filename>%CompleteName%</filename><filesize>%FileSize%</filesize><duration>%Duration%</duration></track>
Video;<track type='Video'><width>%Width%</width><height>%Height%</height><displayAspectRatio>%DisplayAspectRatio/String%</displayAspectRatio><videoFormat>%Format%</videoFormat><videoFormatProfile>%Format_Profile%</videoFormatProfile><videoCodec>%Codec/String%</videoCodec><videoBitrate>%BitRate%</videoBitrate></track>
Audio;<track type='Audio'><audioLanguage>%Language/String%</audioLanguage><audioChannels>%Channel(s)%</audioChannels><audioCodec>%Codec/String%</audioCodec><audioBitrate>%BitRate%</audioBitrate></track>
Text;<track type='Text'><sub>%Language/String%</sub><subCodec>%Codec%</subCodec></track>
File_End;</file>
