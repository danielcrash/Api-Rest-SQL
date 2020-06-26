from sql_alchemy import database


class ContactsModel(database.Model):
    __tablename__ = 'contacts'

    contact_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    channel = database.Column(database.String(80))
    value = database.Column(database.String(80))
    obs = database.Column(database.String(80))

    def __init__(self, contact_id, name, channel, value, obs):
        self.contact_id = contact_id
        self.name = name
        self.channel = channel
        self.value = value
        self.obs = obs

    def parse_json(self):
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'channel': self.channel,
            'value': self.value,
            'obs': self.obs
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

    def update_contact(self, name, channel, value, obs):
        self.name = name
        self.channel = channel
        self.value = value
        self.obs = obs

    def delete_contact(self):
        database.session.delete(self)
        database.session.commit()
