import numpy as np;

M = np.arange(2, 27)
print(M)
print()

M = M.reshape(5, 5)
print(M)
print()

M[1:4, 1:4] = 0
print(M)
print()

M = M@M
print(M)
print()

v = M[0, :]
result = 0;
for elem in v:
    result += elem*elem
result = np.sqrt(result)
print(result)