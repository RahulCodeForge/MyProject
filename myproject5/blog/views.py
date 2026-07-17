from django.shortcuts import render
from datetime import datetime


# Create your views here.

class User:

    def __init__(self,name, age):
        self.name= name
        self.age= age

def Home(request):

    context={

        'name':'Rahul kumar',
        'age':'24',
        'skill' : ['python', 'sql', 'django'],
        'user': User('Kumar','30'),
        'blog':{
            'title' : 'Django project intro',

            'auther':{
                'name':'Ankit Kumar'
            },
            'content': '<b> This is bold</b>',
            'created_at':datetime(2026,7,18,12,3),
        },

        'empty_value': "",
    }

    return render(request,'blog/post_data.html',context)



