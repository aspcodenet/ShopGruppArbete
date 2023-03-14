from models import Category, Product
from .pricingService import calculatePrice

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(1,4,False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    p = Product.query.filter(Product.ProductID ==id).first()
    return adjustPrice(p)

def getTrendingProducts():
    items = Product.query.order_by(Product.ProductID.desc()).paginate(1,8,False).items
    return [adjustPrice(item) for item in items]

def adjustPrice(prod:Product):
    return calculatePrice(None,Category.query.all(),prod)     

