from django.conf.urls.defaults import *

import os
location = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = patterns('',
    (r'^add', "recipe_72.views.add"),
    (r'^edit/(?P<id>\d)$', "recipe_72.views.edit"),
    (r'^recipe_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': location}),
)
