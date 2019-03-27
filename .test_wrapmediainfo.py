import unittest
from wrapmediainfo import media_metadata_extract


class TestStringMethods(unittest.TestCase):

    def test_video1(self):
        self.assertRegex(media_metadata_extract(
            "video1")['videoFormat'], "AVC")
        self.assertRegex(media_metadata_extract(
            "video1")['audioCodec'], "AAC LC")
        self.assertRegex(media_metadata_extract(
            "video1")['videoBitrate'], "82473")
        self.assertEqual(media_metadata_extract("video1")['status'], 0)

    def test_video2(self):
        self.assertRegex(media_metadata_extract(
            "video2")['videoFormat'], "Theora")
        self.assertRegex(media_metadata_extract(
            "video2")['audioCodec'], "Vorbis")
        self.assertRegex(media_metadata_extract(
            "video2")['videoBitrate'], "92643")
        self.assertEqual(media_metadata_extract("video2")['status'], 0)

    def test_non_file(self):
        self.assertRegex(media_metadata_extract(
            "not_a_file")['filename'], "not_a_file")
        self.assertEqual(media_metadata_extract("not_a_file")['filesize'], 0)
        self.assertEqual(media_metadata_extract("not_a_file")['status'], 1)


if __name__ == '__main__':
    unittest.main()
