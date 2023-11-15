#test all five functions mysqrt, mycos, myarcsin, mysin and myhaversine individually :)
from myfunctions import mysqrt, myarcsin, mysin, mycos
from myhaversine import myhaversine
from haversine import haversine # for test_myhaversine


def test_mysqrt(): # from the zoom meeting with the professor 
     tol = 10**-5
    assert -tol < mysqrt(0) < tol
    assert -tol < mysqrt(-1) < tol 
    assert 3-tol < mysqrt(9) < 3 + tol


def test_myarcsin():
    tol = 10**-5
    assert myarcsin(-2) == -90
    assert myarcsin(2) == 90
    assert 30 - tol < myarcsin(0.5) < 30 + tol


def test_mysin():
    assert mysin(0) == 0
    assert mysin(90) == 1


def test_mycos():
    assert mycos(0) == 1
    assert mycos(90) == 0


def test_myhaversine(): 
    tol = 10**-1
    assert -tol<myhaversine((0, 0), (0, 0))<tol
    assert -tol<myhaversine((90, 180), (90, 180))<tol
    # check the distance between Paris and Lyon 
    assert -tol+haversine((45.7597, 4.8422), (48.8567, 2.3508))< myhaversine((45.7597, 4.8422), (48.8567, 2.3508))< haversine((45.7597, 4.8422), (48.8567, 2.3508))
