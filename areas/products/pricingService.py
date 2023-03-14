from models import Category, Product
from .CurrentUserContext import CurrentUserContext,Agreement,AgreementRow


def calculatePrice(currentUserContext:CurrentUserContext, allCategories:list, prod:Product):
    if currentUserContext == None or not  currentUserContext.Agreements:
        return prod
    lowestPrice = prod.UnitPrice
    categoryNames = [cat.CategoryName for cat in allCategories ]
    for agreement in currentUserContext.Agreements:
        if agreement.ProductMatch and agreement.ProductMatch not in prod.ProductName:
            continue
        if agreement.ManufacturerMatch and agreement.ManufacturerMatch not in prod.Manufacturer:
            continue
        if agreement.CategoryMatch and agreement.CategoryMatch not in categoryNames:
            continue
        discounted = 1 - agreement.PercentageDiscount/100
        price = price * discounted
        if price < lowestPrice:
            lowestPrice = price
            
    prod.UnitPrice = lowestPrice
    
