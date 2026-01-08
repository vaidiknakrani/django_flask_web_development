from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def home_page(request):
    return HttpResponse("<h1> Welcome to the django page ... </h1>")
def Newapp(request):
    return HttpResponse("<h1> This is a new page.. </h1>")
# def profile(request):
#     return HttpResponse('<html><body style="background:#000;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;overflow:hidden;"><style>@keyframes spiral{0%{transform:rotate(0deg) scale(0.1);opacity:0;}50%{transform:rotate(180deg) scale(1.5);opacity:1;}100%{transform:rotate(360deg) scale(0.1);opacity:0;}}</style><h1 style="color:#007bff;font-family:sans-serif;font-size:80px;animation:spiral 0.2512994459955699978785656999996649756432674999999999989999999999899999999s linear infinite;"><-----**&&**&&**@@@@@@@@@@**&&**&&**------></h1></body></html>')


def home(request):
    Persons = Person.objects.all()
    data = {'Persons':Persons}
    return render(request,'index.html',data)