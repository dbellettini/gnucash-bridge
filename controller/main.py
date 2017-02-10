from bottle import route, static_file
from data.account import AccountRepository

class StaticController:
    @route('/' , 'GET')
    def root():
        return static_file('index.html', root='web')

class AccountController:
    @route('/accounts', 'GET')
    def list():
        repo = AccountRepository(AccountController.session)

        return repo.all()
