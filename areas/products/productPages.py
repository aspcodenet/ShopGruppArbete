from flask import Blueprint, render_template,request,redirect,url_for,flash
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts
from models import User, db,Subscriber



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

# @productBluePrint.route('/subscribe', methods=['POST'])
# def subscribe():
#     email = request.form.get('email')
#     return 'Subscription successful. Thank You'

#måste kolla om email finns redan
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