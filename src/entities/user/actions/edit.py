from utilities.addDictionaryToFileStore import addDictionaryToFileStore
def main():
    change = input("1. Name 2. Lastname 3. email 4. province 5. password")
try:
    if change == "1":
        name_2 = input("Introduzca el nuevo nombre: ")
        print("El nuevo nombre es: ", name_2)
    elif change == "2":
        lastname_2 = input("Introduzca los nuevos apellidos: ")
        print("Los nuevos apellidos son: ", lastname_2)
    elif change == "3":
        email_2 = input("Introduzca el nuevo correo: ")
        print("El nuevo correo es :",email_2)
    elif change == "4":
        province_2 = input("Introduzca la nueva provincia: ")
        print("La nueva provincia en la que vive es: ",province_2)
    elif change == "5":
        password_2 = input("Introduzca la nueva contraseña: ")
        while True:
            confirmepassword_2 = input("Escriba la nueva contraseña para verificar: ")
            if confirmepassword_2 == password_2:
                print("Felicidades, la contraseña se cambio.")
                break
            else:
                print("Oops intentelo de nuevo.")
except ValueError:
    print("Hubo un error, debe de elegir un numero del 1 al 5 para continuar")    