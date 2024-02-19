from flask import Blueprint, render_template

from .admin_services import get_all_newsletter, get_newsletter

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin() -> str:
    return render_template('admin/admin.html')

@admin_blueprint.route('/admin/newsletters')
def manage_newsletters() -> str:
    
    all_newsletters = get_all_newsletter()
    return render_template('admin/newsletters.html',
                           newsletters = all_newsletters)

@admin_blueprint.route('/admin/newsletter/<newsletter_id>')
def edit_newsletter(newsletter_id: int) -> str:
    newsletter = get_newsletter(newsletter_id)
    return render_template('admin/newsletter.html',
                           newsletter = newsletter)