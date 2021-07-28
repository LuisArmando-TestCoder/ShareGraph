from utilities.getBasicValidInput import getBasicValidInput
from utilities.getSelectedOption import getSelectedOption

def main():
    
    print("Bienvenido al soporte de usuario que desea saber?")
    print("1. Crear cuenta 2. Desactivar cuenta 3. Editar cuenta")
    print("De las opciones anteriores escriba el numero de la que quiere consultar")
    
    consult_select = input()
 
    if consult_select == "1":
        print("Has seleccionado consulta para crear cuentaAl crear la cuenta tendras que escribir tu nombre y apellidos tambien tendras que escribir tu correo y la provincia en la que vives")
    elif consult_select == "2":
        print("Has seleccionado Desactivar cuenta al desactivar la cuenta podras borrarar los datos que almacenaste.")
    
    elif consult_select == "3":
        print("Has seleccionado editar cuenta la opcion editar cuenta te ofrece cambiar los datos que pusiste al crear la cuenta.")
    else: 
        print("Oops, ocurrio un error, por favor ingresa el numero correcto para elegir")