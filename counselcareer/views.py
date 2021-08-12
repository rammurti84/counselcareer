from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about-us.html')
def schedule(request):
    return render(request,'schedule.html')
def gallery(request):
    return render(request,'gallery.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')

