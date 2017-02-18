from bottle import route, static_file
from data.account import AccountRepository


class StaticController:
    @staticmethod
    @route('/<filepath:path>')
    @route('/' , 'GET')
    def root(filepath = 'index.html'):
        return static_file(filepath, root='web')


class AccountController:
    @classmethod
    @route('/accounts', 'GET')
    def list(cls):
        repo = AccountRepository(cls.session)

        return repo.all()
