from django.http import HttpResponse

class hello_class:
    def __call__(self, request):
        return HttpResponse("Hello world!")
        
def hello_function(request):
    return HttpResponse("Hello world!")