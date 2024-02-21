from flask import Blueprint, request
from flask import flash, render_template, redirect, url_for

from .admin_services import create_newsletter, get_all_newsletter, get_newsletter, update_newsletter
from .admin_services import send_newsletter as sender
from views.forms import EditNewsletter

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin() -> str:
    return render_template('admin/admin.html')

@admin_blueprint.route('/admin/newsletters')
def newsletters() -> str:
    # sort_column = request.args.get('sort_column', 'id')
    # sort_order = request.args.get('sort_order', 'asc')
    # page_num = request.args.get('page', 1, type=int)

    all_newsletters = get_all_newsletter()
    return render_template('admin/newsletters.html',
                           newsletters = all_newsletters
                        #    sort_column = sort_column,
                        #    sort_order = sort_order,
                        #    page_num = page_num
                           )

@admin_blueprint.route('/admin/newsletter/new')
def new_newsletter() -> str:
    newsletter_id = create_newsletter()
    return redirect(url_for('admin.edit_newsletter',
                            newsletter_id = newsletter_id
                            )
                        )

@admin_blueprint.route('/admin/newsletter/<newsletter_id>', methods = ['GET', 'POST'])
def edit_newsletter(newsletter_id: int = None) -> str:
    newsletter = get_newsletter(newsletter_id)
    if request.method == 'POST':
        update_newsletter(newsletter, request.form)

    form = EditNewsletter(subject = newsletter.subject,
                          content = newsletter.content)
    return render_template('admin/edit_newsletter.html',
                           newsletter = newsletter,
                           form = form)

@admin_blueprint.route('/admin/newsletters/send/<newsletter_id>')
def send_newsletter(newsletter_id: int) -> str:
    sender(newsletter_id)
    return redirect(url_for('admin.newsletters'))