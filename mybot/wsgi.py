"""
WSGI config for mybot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from nlpbot.views import NlpView

# class main():
#     def __init__(self):
#         self.NlpView=NlpView()
#     def nlpmain(self):
#         self.NlpView.run()

# main_obj=main()
# main_obj.nlpmain()
# call the nlp view for starting the chat..
Nlpview=NlpView()
Nlpview.run()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybot.settings')

application = get_wsgi_application()



