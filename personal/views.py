from django.shortcuts import render

# Create your views here.



# returns the request
def home_screen_view(request):
    print(request.headers)
    return render(request, "personal/home.html", {})
