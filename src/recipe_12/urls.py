from django.conf.urls.defaults import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^update/$', 'recipe_13.views.update'),
    (r'^admin/', include(admin.site.urls)),
)
