from dave import db, login_manager
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, UserMixin
from flask import abort

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    github = db.Column(db.String(100), nullable=False)
    tool_img = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    readme = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Tool('{self.id}' ,'{self.name}' ,'{self.description}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User({self.email})"

class myModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return True

    def inaccessible_callback(self, name, **kwargs):
        abort(404)
