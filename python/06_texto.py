#string cadena de texto
jedi="Qui-Gon Jinn"
aprendiz="Obi-Wan Kenobi"
reina="Padmé Amidala"
droide="R2-D2"
planeta="Naboo"
codigo="327"

print("el jedi es:", jedi)
print("el jedi", type(jedi))
print("el aprendiz es:", aprendiz)
print("el aprendiz", type(aprendiz))
print("EL droide es:", droide)
print("el droide", type(droide))
print("el planeta es:", planeta)
print("el planeta", type(planeta))
print("el codigo es:", codigo)
print("el codigo", type(codigo))

longitud_jedi=len(jedi)
print("la longitud del nombre del jedi es:" + str(longitud_jedi))
longitud_aprendiz=len(aprendiz)
print("la longitud del nombre del aprendiz es:" + str(longitud_aprendiz))

mensaje="la federación de comercio ha bloqueado en Naboo..."
print("el mensaje es:" + mensaje)
mensaje_mayusculas=mensaje.upper()
print("el mensaje en mayusculas es:" + mensaje_mayusculas)
mensaje_minusculas=mensaje.lower()
print("el mensaje en minusculas es:" + mensaje_minusculas)

comunicado="los jedi son enviados a naboo"
print("el comunicado es:" + comunicado)
comunicado_reemplazado=comunicado.replace("jedi", "sith")
print("el comunicado reemplazado es:" + comunicado_reemplazado)