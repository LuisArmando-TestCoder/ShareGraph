# the path starts from where the core.py was executed
from utilities.getBasicValidInput import getBasicValidInput
from utilities.addDictionaryToFileStore import addDictionaryToFileStore
from utilities.getStore import getStore


# all paths start from where the core.py was executed
filePath = "./entities/product/store.json"


def main():
    productName =  getBasicValidInput(
        "What product do you want to see? (type a product name)"
    )

    for item in getStore(filePath):
        if (item["name"] == productName):
            print(f"These are the details of your product: {item}")
