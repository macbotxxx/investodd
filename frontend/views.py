from django.shortcuts import render

# Create your views here.

def homepage(request):
    """Create a homepage """

    return render(request, 'pages/home.html')
