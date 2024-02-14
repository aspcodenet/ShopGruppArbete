from flask import Blueprint, render_template

from .admin_services import get_newsletter

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin() -> str:
    return render_template('admin/admin.html')

@admin_blueprint.route('/newsletters')
def manage_newsletters() -> str:
    return render_template('admin/newsletters.html')

@admin_blueprint.route('/newsletter/<newsletter_id>')
def edit_newsletter(newsletter_id: int) -> str:
    newsletter = get_newsletter(newsletter_id)
    return render_template('admin/newsletter.html',
                           newsletter = newsletter)