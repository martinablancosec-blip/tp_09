from temperature import isoverheating

try:
    temp = float(input("Ingrese temperatura: "))

    if isoverheating(temp):
        print("alarma: Temperatura alta")
    else:
        print("temperatura normal")

except ValueError:
    print("error: ingreso inválido")