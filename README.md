# ShopGruppArbete
![image](https://user-images.githubusercontent.com/325316/217481437-4aed242b-2626-46bd-a338-03d7ceb4c156.png)


SHOPGRUPPARBETE
│   .env                     # Database environment variables, like SQLALCHEMY_DATABASE_URI, SECRET_KEY etc.
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

###################################
        Initial Setup:
###################################

# Install Python: 

Make sure Python is installed on the system. Preferably, use a version that is compatible with the application, such as Python 3.8 or newer.

# Set Up a Virtual Environment:
    To keep things concise let's use Bash Terminal

    1) Navigate to the project directory in the terminal.
        Run *python3 -m venv venv* to create a virtual environment named venv.

    2) Activate the virtual environment:
        On Windows:     *venv\Scripts\activate*
        On macOS/Linux: *source venv/bin/activate*

# Install Required Packages:

    1) Ensure pip is up to date: pip install --upgrade pip.

    2)Install the required packages: pip install -r requirements.txt.

# Set Up Environment Variables:

    1) Create a .env file in the project root with the necessary environment variables, like SQLALCHEMY_DATABASE_URI, SECRET_KEY, and others.
        If you are confused as to how this is formatted navigate to: dotenv_layout.txt 

# Database Specific:
    
    1) Install Database System:
        Install the specific database system you are using, in this case MySQL.
    
    2) Configure Database:
        Set up a new database schema through the database’s management tool.
        
        Ensure the SQLALCHEMY_DATABASE_URI in your .env file matches the database credentials and schema.

# Run Migrations:

    1) Execute flask db init to initialize the migration directory (only once for setup).
    2) Run *flask db migrate -m "Initial migration."* to create the initial migration files. 
        The Quotes ("Initial migration.") can have whichever message generally highlighting what the specific migration implies 
    3) Apply the migrations to the database with *flask db upgrade*.

# Seeding the Database:
    1) Seed the Database:
        Use the custom CLI command provided in your app.py to seed the database: flask seed-db.

# Final Checks:
    1) Test the Application:
        Start the application: *flask run* or *python app.py*.
        Navigate to http://localhost:5000 in a web browser to see if the site is running correctly.
    2) Check Interpreter path:
        Use virtual environment path for python.