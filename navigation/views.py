from django.shortcuts import render

def about (request):
   return render(request,'about.html')

def contact (request):
    return render(request,'contact.html')

def new (request):
    d={'author':'siam','age': 25 ,'list':[1,2,3],'courses' :[
        { 
            'id':1,
            'name':'python',
            'fee': 20000
        },
        {
            'id':2,
            'name':'python5',
            'fee': 25000
        },
        {
            'id':3,
            'name':'python5',
            'fee': 2300
        }
    ]}
    return render(request,'new.html',d)
