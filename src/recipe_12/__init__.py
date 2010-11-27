from django.conf import settings

middleware = settings.MIDDLEWARE_CLASSES
middleware = list(middleware)
middleware.append("recipe_13.middleware.CurrentUserMiddleware")

settings_extra = {
    "MIDDLEWARE_CLASSES": tuple(middleware)
}