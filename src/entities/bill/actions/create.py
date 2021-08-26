# the path starts from where the core.py was executed
from utilities.getBasicValidInput import getBasicValidInput
from utilities.addDictionaryToFileStore import addDictionaryToFileStore
from utilities.getStore import getStore
from entities.user.actions.create import main as createUser

# all paths start from where the core.py was executed
filePath = "./entities/bill/store.json"
userFilePath = "./entities/user/store.json"


def main():
    products = []

    clientId = getBasicValidInput("Client id")
    clients = getStore(userFilePath)

    havingClient = False

    for user in clients:
        havingClient = user["id"] == clientId

    if not havingClient:
        print("Seems like your client id doesn't exists, do you want to create a user? ")

        if getBasicValidInput("(yes/no)") == "yes":
            clientId = createUser()

    while getBasicValidInput("Want to add products to the claim? (yes/no)") == "yes":
        productDictionary = {
            "client": clientId,
            "name": getBasicValidInput("Product name"),
            "amount": int(getBasicValidInput("Product amount")),
        }

        products.append(productDictionary)

    addDictionaryToFileStore(filePath, products)

    print(f"Your item with id: {len(getStore(filePath))} has been created")
