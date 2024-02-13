from models import db, Category, Product

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(page=1,per_page=4,error_out=False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts():
    return Product.query.order_by(Product.ProductID.desc()).paginate(page=1,per_page=8,error_out=False).items

def getAllCategories():
    return Category.query.all()

def addCategory(name, description):
    new_category = Category(CategoryName=name, Description=description)
    db.session.add(new_category)
    db.session.commit()

def addProduct(name, category_id, unit_price, units_in_stock):
    new_product = Product(
        ProductName=name,
        CategoryId=category_id,
        UnitPrice=unit_price,
        UnitsInStock=units_in_stock
        # Set other fields as needed
    )
    db.session.add(new_product)
    db.session.commit()
