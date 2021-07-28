from utilities.addDictionaryToFileStore import addDictionaryToFileStore
filePath = "./entities/user/store.json"
def main():
    productDiccionary = {
         "name": input("Introduzca su nombre: "),
         "lastname": input("Introduzca sus apellidos: "),
         "province": input("Introduzca la provincia en la que vive: "),
        "email": input("Introduzca su correo electronico: "),
        "password": input("Introduzca su contraseña: ")
        }
    
    while True:
            confirm_password = input("Confirme su contraseña porfavor:")
            if confirm_password == password:
                print("Bienvenido", name,lastname)
                break
            else: 
                print("Oops, algo salio mal, intentelo de nuevo")