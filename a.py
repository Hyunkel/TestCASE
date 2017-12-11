import requests
import json
import unittest
import b
import xmlrunner


class TestURL(unittest.TestCase, b.CustomAssertions):
    global url
    global r
    url = url = "http://localhost:3000/kqxsmb?id=8-11-2017"
    r = requests.get(url)
    def test1(self):
        self.check_stt_code(r)

class TestURL2(unittest.TestCase, b.CustomAssertions):
    global url
    global r
    url = url = "http://localhost:3000/kqxsmb?id=8-11-2017"
    r = requests.get(url)
    def test2(self):
        self.check_data_full_mb(r.content)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./Demo_xml'))
