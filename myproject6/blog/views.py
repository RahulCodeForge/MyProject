from django.shortcuts import render
from datetime import datetime

# Create your views here.

def post_details(request):

    post={
        'Name':'Rahul kumar',
        'Age': '24',
        'title':"My second template post",
         'descruiption': "Django is high on demand",
         'author':None,
         'created_at':datetime(2026,7,21,10,56),
         'tags':['django','python', 'web development'],
        




    }

    return render(request,'blog/post_details.html',{'post':post})