from flask_restful import Resource
from flask_restful import reqparse
from models.contacts import ContactsModel


class Contacts(Resource):
    def get(self):
        return {'contacts': [contact.parse_json() for contact in ContactsModel.query.all()]}


class Contact(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name', type=str, required=True, help="Field 'name' cannot be left blank")
    args.add_argument('job')
    args.add_argument('age', type=int, required=True, help="Field 'age' cannot be left blank")
    args.add_argument('city')

    def get(self, contact_id):
        contact = ContactsModel.find_contact(contact_id)
        if contact:
            return contact.parse_json()
        return {'messege': 'Contact not found.'}, 404

    def post(self, contact_id):
        if ContactsModel.find_contact(contact_id):
            return {"message": "Contact ID, '{}' already exists.".format(contact_id)}, 400  # bad request

        data = Contact.args.parse_args()
        contact = ContactsModel(contact_id, **data)
        try:
            contact.save_contact()
        except Exception as Error:
            return {"message": "An internal error occurred trying to save contact. '{}'".format(Error)}, 500
            # Internal Server Error
        return contact.parse_json()

    def put(self, contact_id):
        data = Contact.args.parse_args()
        find_contact = ContactsModel.find_contact(contact_id)
        if find_contact:
            find_contact.update_contact(**data)
            find_contact.save_contact()
            return find_contact.parse_json(), 200
        contact = ContactsModel(contact_id, **data)
        try:
            contact.save_contact()
        except Exception as Error:
            return {"message": "An internal error occurred trying to save contact. '{}'".format(Error)}, 500
            # Internal Server Error
        return contact.parse_json(), 201  # created code

    def delete(self, contact_id):
        contact = ContactsModel.find_contact(contact_id)
        if contact:
            try:
                contact.delete_contact()
                return {'messsege': 'Contact Deleted.'}, 200
            except Exception as Error:
                return {"message": "An internal error occurred trying to delete contact. '{}'".format(Error)}, 500
            # Internal Server Error
        return {'messsege': 'Contact not found.'}, 404
