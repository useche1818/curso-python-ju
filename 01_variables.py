# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funcion del sistema

print(len(my_string_variable)) #esta contando la cantidad de variables en la cadeba

#Variables en una sola linea "no es una buena practica pero se puede hacer ¡Cuidado con abusar de esta sintaxis!"

name, surname, alias, age = "jose", "Us", "kerokgaming", 31
print("me llamo:", name, surname,".Mi edad es:", age,". Mi alias es: ", alias)