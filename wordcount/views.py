from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    s = request.GET['fulltext']
    count = [x for x in s.split(' ')]
    if count[0]!='':
        l = len(count)
        return render(request,'count.html',{ 'l' : l, 'fulltext' : s})
    else:
        return render(request,'Notfound.html')
def about(request):
    return render(request,'about.html')