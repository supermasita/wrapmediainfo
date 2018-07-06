import unittest
from wrapmediainfo import mediaMetadataExtract


class TestStringMethods(unittest.TestCase):

    def test_video1(self):
        self.assertRegex(mediaMetadataExtract("video1")['videoFormat'],"AVC")
        self.assertRegex(mediaMetadataExtract("video1")['audioCodec'],"AAC LC")
        self.assertRegex(mediaMetadataExtract("video1")['videoBitrate'],"82473")
    
    def test_video2(self):
        self.assertRegex(mediaMetadataExtract("video2")['videoFormat'],"Theora")
        self.assertRegex(mediaMetadataExtract("video2")['audioCodec'],"Vorbis")
        self.assertRegex(mediaMetadataExtract("video2")['videoBitrate'],"92643")

if __name__ == '__main__':
    unittest.main()
