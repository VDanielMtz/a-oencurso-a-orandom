try:
    añoencurso=int(input("por favor ingrese el año actual: "))
    añorandom=int(input("por favor ingrese un año aleatorio: "))
    if añoencurso<añorandom:
        op=añorandom - añoencurso
        print("faltan ", op, " años para llegar a ese año :D")
    elif añoencurso>añorandom:
        op=añoencurso-añorandom
        print("han pasado ", op, " años desde ese año :P")
    elif añoencurso==añorandom:
        print ("usted ha ingresado el mismo año D:")
    exit()
except ValueError:
    print("ingrese valores numericos por favor")
    exit()