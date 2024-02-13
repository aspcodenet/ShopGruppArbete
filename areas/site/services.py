from datetime import datetime
from flask_mail import Message
from sqlalchemy import select

from extensions import mail
from models import Newsletter, Subscriber, db

def send_newsletter(newsletter_id: int) -> None:
    stmt = select(Newsletter).where(Newsletter.id == newsletter_id)
    newsletter = db.session.execute(stmt).scalar()
    if not newsletter.is_sent:
        stmt = select(Subscriber.email).where(Subscriber.active)
        active_subscriber_emails = db.session.execute(stmt).scalars().all()
        with mail.connect() as conn:
            for email in active_subscriber_emails:
                msg = Message(recipients = [email],
                              body = newsletter.content,
                              subject = newsletter.subject
                              )
                conn.send(msg)
        newsletter.date_sent = datetime.now()
        newsletter.is_sent = True
        db.session.add(newsletter)
        db.session.commit()