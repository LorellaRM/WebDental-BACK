from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(200), unique=False, nullable=False)
    lastname = db.Column(db.String(250), unique=False, nullable=False)
    phone_Number = db.Column(db.Integer(9), unique=False, nullable=False)
    city = db.Column(db.String(200), unique=False, nullable=False)
    adress = db.Column(db.String(200), unique=False, nullable=False)
    cipcode = db.Column(db.Integer(5), unique=False, nullable=False)
    



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Tratment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dental_Tratment = db.Column(db.Enum("Revisión", "Presupuesto", "Limpieza", "Empaste", "Endodoncia", "Ortodoncia", "Revisión Ortodoncia", "Implante", "Revisión Implante"), unique=True, nullable=False)
    city = db.Column(db.String(200), unique=False, nullable=False)
    adress = db.Column(db.String(200), unique=False, nullable=False)
    cipcode = db.Column(db.Integer(5), unique=False, nullable=False)
    



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_Tratment = db.Column(db.Integer)
    id_User = db.Column(db.Integer)
    date = db.Column(db.Datetime.datetime(), unique=False, nullable=False)
    



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }