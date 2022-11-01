import unittest
from codes import KisDataProvider
from unittest.mock import *
import requests

class KisDataProviderTests(unittest.TestCase):
    
    def test_test(self):
        self.assertEqual("1","1")

    def __init__(self):
        self.dp = KisDataProvider()

    def de_test_Kis_getinfo(self) :
        info = self.dp.get_info()
        
        self.assertEqual("1","1")