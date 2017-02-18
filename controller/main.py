from bottle import route, static_file
from data.account import AccountRepository


class StaticController:
    @staticmethod
    @route('/<filepath:path>')
    @route('/' , 'GET')
    def root(filepath = 'index.html'):
        return static_file(filepath, root='web')


class AccountController:
    @staticmethod
    @route('/accounts', 'GET')
    def list():
        repo = AccountRepository(AccountController.session)

        return repo.all()
