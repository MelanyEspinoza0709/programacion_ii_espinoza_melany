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

#para reemplzar una palabra por otra jeje 
comunicado="los jedi son enviados a naboo"
print("el comunicado es:" + comunicado)
comunicado_reemplazado=comunicado.replace("jedi", "sith")
print("el comunicado reemplazado es:" + comunicado_reemplazado)

planetas="Naboo, tatooine,Coruscant, Alderaan"
planetas_lista=planetas.split(",")
print(planetas_lista)
print("La lista de planetas es:" + str(planetas_lista))
print("El primer planeta de la lista es:" + planetas_lista[0])

droide = "R2-D2"
print("El droide es:" + droide) 
print("El primer caracter del droide es:" + droide[0])  
print("El segundo caracter del droide es:" + droide[1]) 
print("El tercer caracter del droide es:" + droide[2])
print("El cuarto caracter del droide es:" + droide[3])      
print("El quinto caracter del droide es:" + droide[4])
print("El sexto caracter del droide es:" + droide[-1])
planeta = "      Naboo      "
print("El planeta es:" + planeta)
print("El planeta sin espacios es:" + planeta.strip())