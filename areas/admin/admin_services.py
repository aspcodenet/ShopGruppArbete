from sqlalchemy import select

from models import db, Newsletter

def get_all_newsletter() -> list[Newsletter]:
    stmt = select(Newsletter)
    return db.session.execute(stmt).scalars().all()

def get_newsletter(newsletter_id: int) -> Newsletter|None:
    if not newsletter_id:
        return None
    stmt = select(Newsletter).where(Newsletter.id == newsletter_id)
    return db.session.execute(stmt).scalar()