from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Shop Homepage<br><a href="/shop/profile">Go to '
                        'profile!</a>')

def profile(request):
    return HttpResponse('Shop Profilepage <a href="/shop">Back</a>')
