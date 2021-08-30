#! python 3.6

from typing import List

Vector = List[float]

height_weight_age = [
    70,     # inches
    170,    # pounds
    40      # years
]

grades = [
    95,     # exam1
    80,     # exam2
    75,     # exam3
    62      # exam4
]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), 'Vectors must be the same length'
    return [v_i + w_i for v_i, w_i in zip(v, w)]

# Proof of add method
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def substract(v: Vector, w: Vector) -> Vector:
    """Substract the corresponding elements"""
    assert len(v) == len(w), 'Vectors must be the same length'
    return [v_i - w_i for v_i, w_i in zip(v, w)]

# Proof of substract method
assert substract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sum all corresponding elements"""
    assert vectors, 'No vectors provited'

    # Check the vectors are all the same size
    num_elements = len(vectors[0])

    assert all(len(v) == num_elements for v in vectors), 'Different sizes!'

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_2 + ... + v_n * w_n"""
    assert len(v) == len(w), 'Vectors must be same length'
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))     # math.sqrt is the square root function

assert magnitude([3, 4]) == 5

def square_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return magnitude(substract(v, w))

assert distance([5, 3], [1, 1]) == math.sqrt(20)
