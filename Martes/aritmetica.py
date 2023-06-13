def suma(a, b):
    if a is not None and b is not None:
        c = a + b
    else:
        print("Envia ambos valores")
        c = 0
    return c


def resta(a=0, b=1):
    return a - b