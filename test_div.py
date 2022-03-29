import div
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])
def test_divby5_1(num,output):
    result=div.divby5(num)
    assert result==output


@pytest.mark.parametrize("num,output",[(7,True),(10,False),(14,True),(8,False)])
def test_divby7_1(num,output):
    result=div.divby7(num)
    assert result==output


@pytest.mark.parametrize("num,output",[(18,True),(2,False),(90,True),(7,False)])
def test_divby9_1(num,output):
    result=div.divby9(num)
    assert result==output


@pytest.mark.parametrize("num,output",[(121,True),(2,False),(22,True),(7,False)])
def test_divby11_1(num,output):
    result=div.divby11(num)
    assert result==output
