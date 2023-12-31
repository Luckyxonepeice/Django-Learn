from django.shortcuts import render

rooms=[
    {'id':1, 'name':"Let's Learn"},
    {'id':2, 'name':'Design with Me'},
    {'id':3, 'name':'FrontEnd Developers'}
]
def home(request):
    context = {'rooms':rooms}
    return render(request,'home.html',context)

def rooms(request):
    return render(request,'room.html')