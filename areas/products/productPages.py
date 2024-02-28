from flask import Blueprint, render_template, current_app, request, redirect, url_for, flash
from flask_security import roles_accepted
from models import User, db,Subscriber
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts, getAllCategories, addCategory, addProduct

productBluePrint = Blueprint('product', __name__)

@productBluePrint.route('/')
def index():
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()
    return render_template('products/index.html', trendingCategories=trendingCategories, products=trendingProducts)

@productBluePrint.route('/category/<id>')
def category(id):
    category = getCategory(id)
    return render_template('products/category.html', category=category)

@productBluePrint.route('/product/<id>')
def product(id):
    product = getProduct(id)
    return render_template('products/product.html', product=product)

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

@productBluePrint.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        category_id = request.form.get('category_id')
        unit_price = request.form.get('unit_price')
        units_in_stock = request.form.get('units_in_stock')
        
        addProduct(product_name, category_id, unit_price, units_in_stock)
        
        flash('Product added successfully!')
        return redirect(url_for('.admin_catalog'))
    else:
        # GET request: display the form
        categories = getAllCategories()  
        return render_template('admin/add_product.html', categories=categories)

@productBluePrint.route('/delete_product/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    if request.method == 'POST':
        if deleteProduct(id):
            flash('Product deleted successfully!')
        else:
            flash('Error deleting product.')
        return redirect(url_for('.admin_catalog'))
    return render_template('admin/confirm_delete_product.html', product_id=id)

@productBluePrint.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = getProduct(id)
    if request.method == 'POST':
        product_name = request.form['product_name']
        category_id = request.form['category_id']
        unit_price = request.form['unit_price']
        units_in_stock = request.form['units_in_stock']
        if updateProduct(id, product_name, category_id, unit_price, units_in_stock):
            flash('Product updated successfully!')
        else:
            flash('Error updating product.')
        return redirect(url_for('.admin_catalog'))
    categories = getAllCategories()  # For category selection dropdown
    return render_template('admin/edit_product.html', product=product, categories=categories)

@productBluePrint.route('/add_category', methods=['POST'])
def add_category():
    category_name = request.form.get('category_name')
    description = request.form.get('description')
    addCategory(category_name, description)
    flash('Category added successfully!')
    return redirect(url_for('.admin_catalog'))

@productBluePrint.route('/delete_category/<int:id>', methods=['GET', 'POST'])
def delete_category(id):
    if request.method == 'POST':
        if deleteCategory(id):
            flash('Category deleted successfully!')
        else:
            flash('Error deleting category.')
        return redirect(url_for('.admin_catalog'))
    return render_template('admin/confirm_delete_category.html', category_id=id)

@productBluePrint.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    if request.method == 'POST':
        category_name = request.form['category_name']
        description = request.form['description']
        if updateCategory(id, category_name, description):
            flash('Category updated successfully!')
        else:
            flash('Error updating category.')
        return redirect(url_for('.admin_catalog'))
    category = getCategory(id)
    return render_template('admin/edit_category.html', category=category)
