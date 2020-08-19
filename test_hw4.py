from hw4 import main 
import pytest
import os.path
from os import path
import Queue

def test_values():
    main("Boston University")
    assert videxist("Boston University") == True
    main("ECE")
    assert videxist("ECE") == True
    main("Obama")
    assert videxist("Obama") == True
    main("China")
    assert videxist("China") == True

def test_queue():
    Queue
    assert videxist("Boston University") == True
    assert videxist("ECE") == True
    assert videxist("Dota") == True
    assert videxist("2020") == True
    assert videxist("United States") == True
    assert videxist("China") == True
    assert videxist("NBA") == True
    assert videxist("Kobe") == True
    assert videxist("Obama") == True
    assert videxist("Boston") == True


def videxist(keyword):
    if path.exists(keyword + ".avi") == True:
        return True
    else:
        return False