from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(9), nullable=False)    
    city = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False) 

    appointments = db.relationship("Appointments")   

    def __repr__(self):
        return '<User %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name

            # do not serialize the password, its a security breach
        }

class Tratments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    currency = db.Column(db.String(3), nullable=False)

    appointments = db.relationship("Appointments")
    
    def __repr__(self):
        return '<Tratment %r>' % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,

            # do not serialize the password, its a security breach
        }


class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tratment_id = db.Column(db.Integer, db.ForeignKey("tratments.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    datetime = db.Column(db.DateTime, nullable=False)

    tratment = db.relationship("Tratments")
    user = db.relationship("Users")

    def __repr__(self):
        return '<Appointment %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }