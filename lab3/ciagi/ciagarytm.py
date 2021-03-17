def znajdz_n_ty_wyraz_ciagu(a1, ktory, roznica):
    dzialanie = 0
    for i in range(0,ktory):
        n = a1 + (ktory-1) * roznica
        dzialanie += n
        return dzialanie

def suma_n_pierwszych_wyrazow_ciagu(a1,n):
    an = a1 * n
    suma_n = (a1+an)*n/2
    return suma_n




