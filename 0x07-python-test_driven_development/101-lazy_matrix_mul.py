#!/usr/bin/python3
"""Multiply matrix with NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply matrix with Numpy
    """
    mat_1 = np.array(m_a)
    mat_2 = np.array(m_b)

    return np.dot(mat_1, mat_2)
