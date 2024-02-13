from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_security import roles_accepted
from models import User, db,Subscriber
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts, getAllCategories, addCategory, addProduct

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

@productBluePrint.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    #print(email)
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    if existing_subscriber:
        flash('Email already used. Please choose another one.', 'error')
    else:
        new_subscriber = Subscriber(email=email, active=True)
        db.session.add(new_subscriber)
        db.session.commit()
        flash('Subscription successful', 'success')

        return 'Welcome to the Group3 family! 🎉 Get ready for a delightful dose of inspiration, insights, and exclusive content delivered straight to your inbox.'

@productBluePrint.route('/admin/catalog')
def admin_catalog():
    if not current_app.config.get('TEMP_ADMIN_ACCESS', False):
        return "Access Denied", 403

    categories = getAllCategories()
    return render_template('admin/catalog.html', categories=categories)

@productBluePrint.route('/add_category', methods=['POST'])
def add_category():
    category_name = request.form.get('category_name')
    description = request.form.get('description')
    
    addCategory(category_name, description)  
    flash('Category added successfully!')
    return redirect(url_for('.admin_catalog'))

@productBluePrint.route('/add_product', methods=['POST'])
def add_product():
    product_name = request.form.get('product_name')
    category_id = request.form.get('category_id')
    unit_price = request.form.get('unit_price')
    units_in_stock = request.form.get('units_in_stock')
    
    addProduct(product_name, category_id, unit_price, units_in_stock) 
    flash('Product added successfully!')
    return redirect(url_for('.admin_catalog'))

# Add other routes for editing and deleting categories and products here
@productBluePrint.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    # Call a service function to get the category by ID
    pass

@productBluePrint.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    # Similar logic for editing a product
    pass

@productBluePrint.route('/delete_category/<int:id>', methods=['POST'])
def delete_category(id):
    # Call a service function to delete the category
    return redirect(url_for('.admin_catalog'))

@productBluePrint.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    # Similar logic for deleting a product
    return redirect(url_for('.admin_catalog'))
