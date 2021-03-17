def znajdz_nty_wyraz_ciagu_geo(a1, q, n):
    an = a1*(q**(n-1))
    return an

def suma_n_wyrazow_ciagu_geo(a1,n,q):
    if (q==1):
        suma = a1*q
        return suma
    else:
        suma = a1 * (1-q**n/1-q)
        return suma
