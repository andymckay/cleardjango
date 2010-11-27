from django.db.models import signals
from django.utils.functional import curry

class CurrentUserMiddleware:
    def process_request(self, request):
        update_users = curry(self.update_users, request.user)
        signals.pre_save.connect(update_users, dispatch_uid=request, weak=False)
        
    def update_users(self, user, sender, instance, **kwargs):
        if hasattr(instance, "user"):
            if user and user.is_authenticated():
                instance.user = user
            else:
                instance.user = None
    
    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=request)
        return response