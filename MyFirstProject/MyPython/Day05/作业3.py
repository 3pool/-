def factorial (n):
    m = int(n)
    fac = 1
    for i in range(1,m+1):
        fac = fac*i
    print('%d ! = %d' % (m, fac))
factorial(8)
