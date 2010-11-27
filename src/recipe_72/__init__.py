from django.conf import settings
import os

location = os.path.join(os.path.dirname(__file__), "media")

settings_extra = {
    "MEDIA_URL": location,
}