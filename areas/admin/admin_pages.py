from flask import Blueprint, render_template, redirect, url_for

from .admin_services import get_all_newsletter, get_newsletter
from .admin_services import send_newsletter as sender

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

@admin_blueprint.route('/admin/newsletters/send/<newsletter_id>')
def send_newsletter(newsletter_id: int) -> str:
    sender(newsletter_id)
    return redirect(url_for('admin.manage_newsletters'))