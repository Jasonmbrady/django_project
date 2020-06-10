from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        # context file placeholder
    }
    return render(request, "index.html", context)
