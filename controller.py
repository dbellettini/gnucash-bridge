from bottle import route
from collections import OrderedDict
from uuid import UUID

def account_uuid(account):
    return str(UUID(account.GetGUID().to_string()))


def map_account(account):
    dict = OrderedDict([
        ('id', account_uuid(account)),
        ('name', account.name)
    ])

    children = []
    for child in account.get_children_sorted():
        children.append(map_account(child))

    if len(children) > 0:
        dict['children'] = children;

    return dict

def map_root_account(root_account):
    mapped = {'items': []}

    for child in root_account.get_children_sorted():
        mapped['items'].append(map_account(child))

    return mapped

class AccountController:
    @route('/accounts', 'GET')
    def list():
        root_account = AccountController.session.book.get_root_account()

        return map_root_account(root_account)

