from nose.tools import *
import sys
sys.path.append("../")
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DWN!")

def test_basic():
    print("I RaN!")
