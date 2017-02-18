from bottle import route, static_file
from data.account import AccountRepository


class StaticController:
    @staticmethod
    @route('/' , 'GET')
    def root():
        return static_file('index.html', root='web')


class AccountController:
    @classmethod
    @route('/accounts', 'GET')
    def list(cls):
        repo = AccountRepository(cls.session)

        return repo.all()
