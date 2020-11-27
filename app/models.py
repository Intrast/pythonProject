from . import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    passport = db.Column(db.String(8), nullable=False)
    education = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Employee('{self.id}', '{self.name}', '{self.surmane}', '{self.passport}', '{self.education}', '{self.salary}', '{self.experience}'"
