import div


def test_divby5_1():
    a=10
    result=div.divby5(a)
    assert result==True

def test_divby5_2():
    a=11
    result=div.divby5(a)
    assert result==False

def test_divby7_1():
    a=14
    result=div.divby7(a)
    assert result==True

def test_divby7_2():
    a=10
    result=div.divby7(a)
    assert result==False

def test_divby9_1():
    a=18
    result=div.divby9(a)
    assert result==True

def test_divby9_2():
    a=10
    result=div.divby9(a)
    assert result==False

def test_divby11_1():
    a=11
    result=div.divby11(a)
    assert result==True

def test_divby11_2():
    a=10
    result=div.divby11(a)
    assert result==False