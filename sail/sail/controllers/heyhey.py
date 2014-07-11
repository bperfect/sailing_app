from tg import expose

from sail.lib.base import BaseController

class MainController(BaseController):

    @expose('sail.templates.request')
    def index(self):
        return dict(hey=3)

    @expose('json')
    def demoForm(self, name=None, phone_num=None, start=None, end=None, boats=None, rating=None, **kw):
        return dict(success='true', name=name, rating=rating)
