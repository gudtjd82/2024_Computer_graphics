import numpy as np

vec = np.array([-4, -2, -6])
vec = vec / np.linalg.norm(vec)
axis = np.array([0, -1, 0])

dot_prod = np.dot(vec, axis)
# print(dot_prod)

degree =np.degrees(np.arccos(dot_prod))
print(90 - degree)