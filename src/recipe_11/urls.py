from django.conf.urls.defaults import patterns
from views import hello_class

urlpatterns = patterns('',
    (r'^hello-class/$', hello_class()),
    (r'^hello-function/$', 'recipe_10.views.hello_function')
)
