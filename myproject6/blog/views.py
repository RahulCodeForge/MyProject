from django.shortcuts import render

# Create your views here.

def post_details(request):

    post={
        'Name':'Rahul kumar',
        'Age': '24',



    }

    return render(request,'blog/post_details.html',post)