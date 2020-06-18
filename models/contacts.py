from sql_alchemy import database


class ContactsModel(database.Model):
    __tablename__ = 'contacts'

    contact_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    job = database.Column(database.String(80))
    age = database.Column(database.Integer)
    city = database.Column(database.String(80))

    def __init__(self, contact_id, name, job, age, city):
        self.contact_id = contact_id
        self.name = name
        self.job = job
        self.age = age
        self.city = city

    def parse_json(self):
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'job': self.job,
            'age': self.age,
            'city': self.city
        }

    @classmethod
    def find_contact(cls, contact_id):
        contact = cls.query.filter_by(contact_id=contact_id).first()
        if contact:
            return contact
        return None

    def save_contact(self):
        database.session.add(self)
        database.session.commit()

    def update_contact(self, name, job, age, city):
        self.name = name
        self.job = job
        self.age = age
        self.city = city

    def delete_contact(self):
        database.session.delete(self)
        database.session.commit()
