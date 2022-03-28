import div
import pytest

@pytest.fixture
def input():
    a=25
    return a

def test_divby5_1(input):
    result=div.divby5(input)
    assert result==True

def test_divby5_2(input):
    result=div.divby5(input)
    assert result==False

def test_divby7_1(input):
    result=div.divby7(input)
    assert result==True

def test_divby7_2(input):
    result=div.divby7(input)
    assert result==False

def test_divby9_1(input):
    result=div.divby9(input)
    assert result==True

def test_divby9_2():
    a=10
    result=div.divby9(input)
    assert result==False

def test_divby11_1(input):
    result=div.divby11(input)
    assert result==True

def test_divby11_2(input):
    result=div.divby11(input)
    assert result==False