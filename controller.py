from bottle import route
from uuid import UUID

def account_uuid(account):
    return str(UUID(account.GetGUID().to_string()))

class AccountController:
    @route('/accounts')
    def list():
        root_account = AccountController.session.book.get_root_account()

        accounts = []
        for account in root_account.get_children_sorted():
            accounts.append({
                'id': account_uuid(account),
                'name': account.name
            })

        return {'items': accounts}

