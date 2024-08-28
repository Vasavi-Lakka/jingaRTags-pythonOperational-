from django.shortcuts import render

def conditional(request):
    d={'a':2000, 'b':1000, 'c':4000}
    return render(request, 'conditional.html', context=d)



# Create your views here.
def looping(request):
    d={'name':'vassu', 'mb':[12345,2456]}
    return render(request, 'looping.html', context=d)