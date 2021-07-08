# the path starts from where the core.py was executed
from utilities.getBasicValidInput import getBasicValidInput
from utilities.addDictionaryToFileStore import addDictionaryToFileStore


# all paths start from where the core.py was executed
filePath = "./entities/product/store.json"


def main():
    productDictionary = {
        "name": getBasicValidInput("Product name"),
        "description": getBasicValidInput("Product description"),
        "category": getBasicValidInput("Product category"),
        "author": getBasicValidInput("Product author"),
    }

    price = ""

    while not str(price).isnumeric():
        price = input("Product price: ")

        if str(price).isnumeric():
            if not int(price) >= 0:
                continue

    productDictionary["price"] = int(price)

    addDictionaryToFileStore(filePath, productDictionary)
