from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{boldmessage}} in the template!
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context)

def about(request):
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return HttpResponse('Rango says here is the about page. <a href="/rango/">Home Page</a>')
