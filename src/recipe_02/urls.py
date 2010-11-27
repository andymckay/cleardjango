from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^$', 'recipe_02.views.hello_world')
)
