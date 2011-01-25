import logging
import rascal

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from helloworld.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        c.sourcefile = "index.mako"
        c.fileurl = "/hello/index"
        return render('/index.mako')

    def editor(self):
        c.fileurl = request.params['fileurl']
        c.sourcefile = request.params['sourcefile']
        return render('/editor.mako')

    def form(self):
        return render('/form.mako')

    def email(self):
        if(request.params['target_state'] == '1'):
            rascal.set_pin_high(66)
            rascal.set_pin_high(71)
            result = 'Pins set high'
        elif(request.params['target_state'] == '0'):
            rascal.set_pin_low(66)
            rascal.set_pin_low(71)
            result = 'Pins set low'
        else:
            result = 'target_state is screwed up'
        return result 
        #return 'Your email is: %s' % request.params['email']

    def save(self):
        path = '/home/root/helloworld/helloworld/templates/'
        c.fileurl = request.params['fileurl']
        c.sourcefile = request.params['sourcefile']
        f = open(path + str(c.sourcefile), 'w')
        f.write(request.params['text'])
        f.close()
        return render('/editor.mako') 
