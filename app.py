from flask import Flask
from models import db, seedData
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from flask_security import roles_accepted, auth_required, logout_user

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.run()


