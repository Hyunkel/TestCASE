import requests
import json
import unittest
import b


class TestURL(unittest.TestCase, b.CustomAssertions):
    def setUp(self):
        print("Thiet Lap cac Truong Hop Cua TestUnitTes")

    def tearDown(self):
        print("Don dep cac truong hop cua TestUnitest")
    
    global url
    global r
    url = url = "http://localhost:3000/kqxsmb?id=8-11-2017"
    r = requests.get(url)
    def test1(self):
        self.check_stt_code(r)

class TestURL2(unittest.TestCase, b.CustomAssertions):
    def setUp(self):
        print("Thiet Lap cac Truong Hop Cua TestUnitTes")

    def tearDown(self):
        print("Don dep cac truong hop cua TestUnitest")
    
    global url
    global r
    url = url = "http://localhost:3000/kqxsmb?id=8-11-2017"
    r = requests.get(url)
    def test2(self):
        self.check_data_full_mb(r.content)

if __name__ == "__main__":
    unittest.main()