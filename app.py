from flask import Flask, request, current_app, render_template
from flask_migrate import Migrate, upgrade
from flask_security import SQLAlchemyUserDatastore, Security
from models import db, User, Role, seedData, Product, Category
from areas.products.productPages import productBluePrint
from areas.site.sitePages import siteBluePrint
from dotenv import load_dotenv
import click
from flask.cli import with_appcontext
from os import environ


load_dotenv()

app = Flask(__name__)
# app.config.from_object('config.ConfigDebug')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SECURITY_REGISTERABLE'] = environ.get('SECURITY_REGISTERABLE')
app.config['SECURITY_PASSWORD_SALT'] = environ.get('SECURITY_PASSWORD_SALT')

app.config['TEMP_ADMIN_ACCESS'] = True  # Temporary flag for admin access without login

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

# Register blueprints
app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

# Seeding Command
@click.command('seed-db')
@with_appcontext
def seed_db_command():
    """Seeds the database."""
    seedData(app)
    click.echo('Database seeded.')

app.cli.add_command(seed_db_command)

# Produkt
@app.route('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('products/index.html', products=products, categories=categories)

@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html',product=product)
    

@app.route('/category/<int:category_id>/product/<int:product_id>')
def show_product_in_category(category_id, product_id):
    category = Category.query.get_or_404(category_id)
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', category=category, product=product)



# Temporary check for admin access
# This is a placeholder, should be replaced with actual authentication logic
@app.before_request
def before_request():
    if 'admin' in request.path:
        temp_admin_access = request.args.get('temp_admin', '0') == '1'
        if not (temp_admin_access or current_app.config.get('TEMP_ADMIN_ACCESS', False)):
            return "Access Denied", 403

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
    
    app.run()
    