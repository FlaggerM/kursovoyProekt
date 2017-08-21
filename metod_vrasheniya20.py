# -*- coding: utf-8 -*-
"""
numpy - содержит вычислительные функции, которых нет в стандартной библиотеке.
 Array - конвертирует список в массив;
 zeros - создать массив с заданной размерностью  и заполнить его нулями;
 diag - извлечь диагональ массива;
 diagflat - создание массива с заданной размерностью и указаной диагональю, и заполнить все остальное нулями;
 dot - сложение матриц.
"""

from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A, b, N=1000, x=None):
    if x is None:
        x = zeros(len(A[0]))  	# создаем векрот Х
    pprint(x)
    print(len(A[0]))
    D = diag(A)  				# создаем D и заполняем его диагональю из А
    R = A - diagflat(D) 		# удаляем(вычитаем) диагональ(D) из А 
								# A = D + R

    for i in range(N):  		# цикл для вычисления корня(корней) по формуле: x^(k+1)= (b − Rx^(k) )D^−1
        x = (b - dot(R, x)) / D

    return x


def jacobi1(a, b):
    """Вспомогательная функция для вызова основной(jacobi)"""
    a = array(a)
    b = array(b)
    #guess = array([1.0, 1.0, 1.0])
    sol = jacobi(a, b, N=1000)

    return sol


if __name__ == '__main__':
    A = array([
               [8., 4., 2.],
               [3., 5., 1.],
               [3., -2., 10.]
     ])
    b = array([10., 5., 5.])
    #guess = array([1.0, 1.0, 1.0])
    #A = array([
    #    [1., 2.],
    #    [1., 2.]
    #])
    #b = array([3., 3.])
    sol = jacobi(A, b, N=50)

    print("A:")
    pprint(A)

    print("b:")
    pprint(b)

    print("x:")
    pprint(sol)
