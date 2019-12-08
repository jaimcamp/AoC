#!/usr/bin/python3

import numpy as np


example = '123456789012'
vec = np.array([int(x) for x in example])
input_vec = np.array([int(x) for x in open('input.txt').read().strip()])
m_input_vec = input_vec.reshape((-1, 6, 25))
less_0 = np.argmin(np.sum((m_input_vec == 0), (1, 2)))
selected_m = m_input_vec[less_0]
np.sum(selected_m == 1) * np.sum(selected_m == 2) 

def first_non_2(vector):
    assert type(vector) == np.ndarray
    return vector[np.argmax(vector != 2)]

m_non2 = np.apply_along_axis(first_non_2, 0, m_input_vec)
