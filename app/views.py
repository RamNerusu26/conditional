from django.shortcuts import render

# Create your views here.
def conditional(request):
    dic={'a':116,'b':420,'c':1182}
    return render(request,'conditional.html',dic)