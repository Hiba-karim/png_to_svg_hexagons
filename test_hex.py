# Import all functions and classes from the cs_project module
from cs_project import *

# Test for hexagonal arithmetic operations
def test_hex_arithmetic():
    # Testing hex addition
    assert hex_add(Hex(1, -3, 2), Hex(3, -7, 4)) == Hex(4, -10, 6)
    # Testing hex subtraction
    assert hex_subtract(Hex(1, -3, 2), Hex(3, -7, 4)) == Hex(-2, 4, -2)

# Test for hexagonal direction calculation
def test_hex_direction():
    # Testing if the direction calculation is correct for direction index 2
    assert hex_direction(2) == Hex(0, -1, 1)

# Test for finding a hexagonal neighbor
def test_hex_neighbor():
    # Testing if the neighbor calculation is correct for direction index 2
    assert hex_neighbor(Hex(1, -2, 1), 2) == Hex(1, -3, 2)

# Test for finding a hexagonal diagonal neighbor
def test_hex_diagonal():
    # Testing if the diagonal neighbor calculation is correct for direction index 3
    assert hex_diagonal_neighbor(Hex(1, -2, 1), 3) == Hex(-1, -1, 2)

# Test for calculating hexagonal distance
def test_hex_distance():
    # Testing if the distance calculation is correct between two hexes
    assert hex_distance(Hex(3, -7, 4), Hex(0, 0, 0)) == 7

# Test for rotating a hexagon to the right
def test_hex_rotate_right():
    # Testing if the right rotation of a hex is correct
    assert hex_rotate_right(Hex(1, -3, 2)) == Hex(3, -2, -1)

# Test for rotating a hexagon to the left
def test_hex_rotate_left():
    # Testing if the left rotation of a hex is correct
    assert hex_rotate_left(Hex(1, -3, 2)) == Hex(-2, -1, 3)

# Test for rounding a hexagon using linear interpolation
def test_hex_round():
    a = Hex(0.0, 0.0, 0.0)
    b = Hex(1.0, -1.0, 0.0)
    c = Hex(0.0, -1.0, 1.0)
    # Testing if the rounding of a hex using linear interpolation is correct
    assert hex_round(hex_lerp(Hex(0.0, 0.0, 0.0), Hex(10.0, -20.0, 10.0), 0.5)) == Hex(5, -10, 5)

# Test for hexagonal line drawing (Lerp)
def test_hex_linedraw():
    # Testing if the line drawing between two hexes is correct
    assert hex_linedraw(Hex(0, 0, 0), Hex(3, -3, 0)) == [
        Hex(0, 0, 0),
        Hex(1, -1, 0),
        Hex(2, -2, 0),
        Hex(3, -3, 0),
    ]
