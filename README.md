# ShopGruppArbete
![image](https://user-images.githubusercontent.com/325316/217481437-4aed242b-2626-46bd-a338-03d7ceb4c156.png)


SHOPGRUPPARBETE
│   .gitignore               # Specifies intentionally untracked files to ignore
│   app.py                   # Main entry point for the Flask application
│   azure-pipelines.yml      # Configuration file for Azure DevOps CI/CD pipeline
│   config.py                # Configuration settings for the application
│   models.py                # Definitions of database models
│   README.md                # Documentation about this project
│   requirements.txt         # List of dependencies to install with pip
│
├───areas                    # Logical separation of the application's concerns
│   ├───products             # Contains the product section of the application
│   │   │   __init__.py      # Initializes the Python package for products
│   │   │   productPages.py  # Python script handling product-related routes
│   │   │   services.py      # Services and business logic for product features
│   │   │
│   │   └───__pycache__      # Compiled bytecode for Python modules
│   │
│   └───site                 # Contains the site section of the application
│       │   sitePages.py     # Python script handling site-related routes
│       │
│       └───__pycache__      # Compiled bytecode for Python modules
│
├───migrations               # Database migration scripts
├───static                   # Static files that don't change, served by the web server
│   ├───css                  # Cascading Style Sheets for styling web pages
│   │       *various .css files*
│   ├───fonts                # Fonts files to be used in the web pages
│   │       *various font files*
│   ├───img                  # Image files used in the web application
│   │   ├───Products         # Images specifically related to products
│   │   │       *product images*
│   │   ├───logo.png         # Website logo image
│   │   ├───shop01.png       # Additional images used in the shop
│   │   ├───shop02.png
│   │   ├───shop03.png
│   │
│   ├───js                   # JavaScript files for client-side scripting
│   │       *various .js files*
│   │
│   └───lib                  # Library files, possibly for third-party plugins
├───templates                # HTML templates that are rendered by Flask
│   ├───products             # HTML templates specifically for the products section
│   │       category.html    # Template for displaying product categories
│   │       index.html       # The main or 'index' page for the product listings
│   │       product.html     # Template for displaying individual product details
│   │
│   └───site                 # HTML templates for the site section
│           baseTemplate.html # Base HTML template for inheritance
│           formhelpers.html  # HTML to help with form elements
│
└───venv                     # Virtual environment folder for the project dependencies

Test