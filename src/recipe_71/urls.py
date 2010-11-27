from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import os
location = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^recipe_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': location}),
)
