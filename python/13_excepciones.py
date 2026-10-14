print("°❀⋆.ೃ࿔*.ೃ࿔*:･°❀⋆.ೃCONTROL DE ENERGIA❀⋆.ೃ࿔*:･°❀°❀⋆.ೃ࿔*:･")
energia_texto="ochenta"
try:
    energia=int("mucho")
    print(energia)
except ValueError:
    print("error: debe ser numerico")

print("fin del sistema")

"""
 TIPOS:
    ValueError
    TypeError
    KeyError
    IndexError
    ZeroDivisionError
"""

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")

def calcular_energia(total, cantidad):
    try:
        resultado=total/cantidad
        return resultado
    except ZeroDivisionError as error:
        print("error: division entre cero")
        return None
    
    except TypeError:
        print("error:valores deben ser numericos")
        return None

print("caso1:", calcular_energia(100,4))
print("caso2:", calcular_energia(100,0))
print("caso3:", calcular_energia(100,"cuatro"))

print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:DIAGNOSTICO R2-D2･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･")
try:
    energia=int(90)
    print("energia", energia)
except ValueError:
    print("error de lectura")
else:
    print("diagnostico completado")
finally:
    print("cerrado diagnostico")

def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("la energia debe ser numero entero")
    if energia<0 or energia >100:
        raise ValueError("la energia debe estar entre 0 y 100")
    return energia

try:
    resultado=validar_energia(60)
    print("energia", resultado)
except(TypeError, ValueError) as error:
    print("error:", error)
        