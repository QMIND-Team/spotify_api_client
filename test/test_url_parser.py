import unittest
import src


class TestUrlParser(unittest.TestCase):
    def test_parse_success_no_change_https(self):
        url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        parsed_url = src.parse_url(url)
        self.assertEqual(url, parsed_url)

    def test_parse_success_no_change_http(self):
        url = "http://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        parsed_url = src.parse_url(url)
        self.assertEqual(url, parsed_url)

    def test_parse_success_add_https(self):
        url = "api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        parsed_url = src.parse_url(url)
        expected_url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        self.assertEqual(expected_url, parsed_url)

    def test_parse_success_starts_with_v1(self):
        url1 = "/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        parsed_url1 = src.parse_url(url1)
        expected_url1 = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        self.assertEqual(expected_url1, parsed_url1)

        url2 = "v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        parsed_url2 = src.parse_url(url2)
        expected_url2 = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
        self.assertEqual(expected_url2, parsed_url2)

    def test_parse_url_invalid_url_provided(self):
        with self.assertRaises(Exception) as context:
            url = "https://www.shopify.com"
            src.parse_url(url)

        self.assertTrue('Invalid URL provided' in str(context.exception))


if __name__ == "main":
    unittest.main()
