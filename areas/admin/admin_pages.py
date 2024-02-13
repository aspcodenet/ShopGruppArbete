from flask import Blueprint, render_template

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin() -> str:
    return render_template('admin/admin.html')

admin_blueprint.route('/newsletters')
def manage_newsletters() -> str:
    return ''