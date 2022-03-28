import Calc

def test_add2numbers():
    x=10
    y=20
    res=Calc.add2numbers(x,y)
    assert res==x+y

def test_sub2numbers():
    x=10
    y=20
    res=Calc.sub2numbers(x,y)
    assert res==x-y

def test_mul2numbers():
    x=10
    y=20
    res=Calc.mul2numbers(x,y)
    assert res==x*y

def test_div2numbers():
    x=10
    y=20
    res=Calc.div2numbers(x,y)
    assert res==x/y