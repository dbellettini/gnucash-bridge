from collections import OrderedDict
from uuid import UUID

class AccountRepository:
    def __init__(self, session):
        self.session = session

    def all(self):
        root_account = self.session.book.get_root_account()
        mapped = {'items': []}

        for child in root_account.get_children_sorted():
            mapped['items'].append(self.map_account(child))

        return mapped

    def map_account(self, account):
        dict = OrderedDict([
            ('id', account_uuid(account)),
            ('name', account.name)
        ])

        children = []
        for child in account.get_children_sorted():
            children.append(self.map_account(child))

        if len(children) > 0:
            dict['children'] = children;

        return dict

def account_uuid(account):
    return str(UUID(account.GetGUID().to_string()))

