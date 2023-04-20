from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def displayOptions(request):
        Lister=["1) Lorem Ipsum","2) Lorem Ipsum","3) Lorem Ipsum","4) Lorem Ipsum", ]
        args={'Lister':Lister}
        return render(request, 'Options.html',args)


