from application import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, nullable=False)

    def __init__(self, role):
        self.role = role

    @staticmethod
    def init_roles(*args, **kwargs):
        user = Role(role="USER")
        admin = Role(role="ADMIN")
        db.session().add(user)
        db.session().add(admin)
        db.session().commit()

class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

    role = db.relationship("Role", lazy=True)

    loans = db.relationship("Loan", lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role.role]

