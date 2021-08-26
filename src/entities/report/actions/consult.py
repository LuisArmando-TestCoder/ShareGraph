from utilities.getStore import getStore

filePath = "./entities/bill/store.json"
productFilePath = "./entities/product/store.json"

def getProduct(name):
    for product in getStore(productFilePath):
        if product["name"] == name:
            return product

def getProductBillsAverage(name):
    productPriceSummation = 0
    productAmount = 0

    for bill in getStore(filePath):
        for sell in bill:
            if sell["name"] == name:
                productAmount += 1
                productPriceSummation += sell["amount"] * getProduct(
                    name
                )["price"]

    return productPriceSummation / (productAmount if productAmount else 1)

def getSellsAverage(bills):
    # print("The average of sells has being")
    allProductsPricesSummation = 0
    allSellsAmount = 0

    for bill in bills:
        allSellsAmount += 1

        for sell in bill:
            allProductsPricesSummation = sell["amount"] * getProduct(sell["name"])["price"]

    print(f"The average of sells has being {allProductsPricesSummation / allSellsAmount}")
    
def getProductsAverage():
    print("The average of sells for each product")
    for product in getStore(productFilePath):
        print(f"For {product['name']} the average sells are {getProductBillsAverage(product['name'])}")

def getHighestSellWithBill(bills):
    maximumBillIndex = 0
    maximumBill = 0

    for billIndex in range(len(bills)):
        billSummation = 0

        for sell in bills[billIndex]:
            billSummation += sell["amount"] * getProduct(
                sell["name"]
            )["price"]

        if billSummation > maximumBill:
            maximumBill = billSummation
            maximumBillIndex = billIndex

    print(f"The highest sell is {maximumBill}")
    print(f"For the following bill {bills[maximumBillIndex]}")

def main():
    bills = getStore(filePath)

    getSellsAverage(bills)
    getProductsAverage()
    getHighestSellWithBill(bills)

