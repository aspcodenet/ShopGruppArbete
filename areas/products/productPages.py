from flask import Blueprint, render_template, current_app
from flask_security import roles_accepted
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts, getAllCategories



productBluePrint = Blueprint('product', __name__)

@productBluePrint.route('/')
def index() -> str:
    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()
    return render_template('products/index.html',
                           trendingCategories=trendingCategories,
                           products=trendingProducts
                           )

@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)

@productBluePrint.route('/admin/catalog')
def admin_catalog():
    if not current_app.config.get('TEMP_ADMIN_ACCESS', False):
        return "Access Denied", 403

    categories = getAllCategories()
    return render_template('admin/catalog.html', categories=categories)
