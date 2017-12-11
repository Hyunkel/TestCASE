import os
import unittest
import requests
import json


class CustomAssertions():
    def check_json(self, myjson):
        # check object valid Json
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            raise AssertionError("Khong Phai Dinh Dang Json")
    
    def check_stt_code(self, r):
        # check status code response
        try:
            print("Status code: %s" % (r.status_code))
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise AssertionError(err)
    
    def check_data_full_mb(self, obj):
        # check data response MB
        cautruc = 'GiaiDacBiet,GiaiNhat,GiaiNhi,GiaiBa,GiaiTu,GiaiNam,GiaiSau,GiaiBay'
        try:
            data = json.loads(obj)
            for k, v in data.items():
                for i in v:
                    self.assertRegexpMatches(cautruc, i, "Khong Ton Tai Gia Tri Trong Cau Truc Data")
                self.assertTrue(k, "Khong Ton Tai Key Trong Data ")
                self.assertTrue(v, "Khong Ton Tai Value Trong Data")
                self.assertEqual(11, len(v), "Data Tra Ve Thieu Hoac Thua")
                self.assertEqual(5, len(v["GiaiDacBiet"]), "GiaiDacBiet Tra Ve Sai")
                self.assertEqual(5, len(v["GiaiNhat"]), "GiaiNhat Tra Ve Sai")
                self.assertEqual(11, len(v["GiaiNhi"]), "GiaiNhi Tra Ve Sai")
                self.assertEqual(35, len(v["GiaiBa"]), "GiaiBa Tra Ve Sai")
                self.assertEqual(19, len(v["GiaiTu"]), "GiaiTu Tra Ve Sai")
                self.assertEqual(29, len(v["GiaiNam"]), "GiaiNam Tra Ve Sai")
                self.assertEqual(11, len(v["GiaiSau"]), "GiaiSau Tra Ve Sai")           
                self.assertEqual(11, len(v["GiaiBay"]), "GiaiBay Tra Ve Sai")    
        except AssertionError as err:
            raise AssertionError(err)
    
    def check_data_full_mk(self, obj):
        # check data response Mkhac
        cautruc = 'GiaiDacBiet,GiaiNhat,GiaiNhi,GiaiBa,GiaiTu,GiaiNam,GiaiSau,GiaiBay,GiaiTam'
        try:
            data = json.loads(obj)
            for k, v in data.items():
                for i in v:
                    self.assertRegexpMatches(cautruc, i, "Khong Ton Tai Gia Tri Trong Cau Truc Data")
                self.assertEqual(9, len(v), "Data Tra Ve Thieu Hoac Thua")
                self.assertEqual(6, len(v["GiaiDacBiet"]), "GiaiDacBiet Tra Ve Sai")
                self.assertEqual(5, len(v["GiaiNhat"]), "GiaiNhat Tra Ve Sai")
                self.assertEqual(5, len(v["GiaiNhi"]), "GiaiNhi Tra Ve Sai")
                self.assertEqual(11, len(v["GiaiBa"]), "GiaiBa Tra Ve Sai")
                self.assertEqual(41, len(v["GiaiTu"]), "GiaiTu Tra Ve Sai")
                self.assertEqual(4, len(v["GiaiNam"]), "GiaiNam Tra Ve Sai")
                self.assertEqual(14, len(v["GiaiSau"]), "GiaiSau Tra Ve Sai")           
                self.assertEqual(3, len(v["GiaiBay"]), "GiaiBay Tra Ve Sai")
                self.assertEqual(2, len(v["GiaiTam"]), "GiaiTam Tra Ve Sai")    
        except AssertionError as err:
            raise AssertionError(err)