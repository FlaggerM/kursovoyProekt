# -*- coding: utf-8 -*-
"""
numpy/scipy - содержит вычислительные функции, которых нет в стандартной библиотеке.
 Array - конвертирует список в массив;
pprint - форматированый вывод.
"""
import scipy
import pprint

def lu(a):
	n = len(a)
	L = [[0] * n for i in range(n)]
	U = [[0] * n for i in range(n)]
	for i in range(n):
		L[i][i] = 1
	for i in range(n):
		for j in range(n):
			U[i][j] = a[i,j]
	for i in range(0, n):
			for j in range(i, n):
				L[j][i] = (U[j][i])/(U[i][i])
	for k in range(1, n):
		for i in range(k-1, n):
			for j in range(i, n):
				L[j][i] = (U[j][i])/(U[i][i])
		for i in range(k, n):
			for j in range(k-1, n):
				U[i][j] = U[i][j] - L[i][k-1]*U[k-1][j]
	return L, U

if __name__ == '__main__':
	A = ([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
	A = scipy.array(A)
	L, U = lu(A)
	pprint.pprint(A)
	pprint.pprint(L)
	pprint.pprint(U)
