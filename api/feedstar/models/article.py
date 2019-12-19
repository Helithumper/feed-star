from feedstar.extensions import db


class Article(db.Model):
    """Basic user model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True, nullable=False)
    link = db.Column(db.String(300), unique=True, nullable=False)
    source = db.Column(db.String(300), unique=False, nullable=False)

    def __repr__(self):
        return "<Article %s>" % self.title
