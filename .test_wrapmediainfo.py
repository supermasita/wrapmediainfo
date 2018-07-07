import unittest
from wrapmediainfo import mediaMetadataExtract


class TestStringMethods(unittest.TestCase):

    def test_video1(self):
        self.assertRegex(mediaMetadataExtract("video1")['videoFormat'],"AVC")
        self.assertRegex(mediaMetadataExtract("video1")['audioCodec'],"AAC LC")
        self.assertRegex(mediaMetadataExtract("video1")['videoBitrate'],"82473")
        self.assertEqual(mediaMetadataExtract("video1")['status'],0)
    
    def test_video2(self):
        self.assertRegex(mediaMetadataExtract("video2")['videoFormat'],"Theora")
        self.assertRegex(mediaMetadataExtract("video2")['audioCodec'],"Vorbis")
        self.assertRegex(mediaMetadataExtract("video2")['videoBitrate'],"92643")
        self.assertEqual(mediaMetadataExtract("video2")['status'],0)
    
    def test_non_file(self):
        self.assertRegex(mediaMetadataExtract("not_a_file")['filename'],"not_a_file")
        self.assertEqual(mediaMetadataExtract("not_a_file")['filesize'],0)
        self.assertEqual(mediaMetadataExtract("not_a_file")['status'],1)

if __name__ == '__main__':
    unittest.main()
