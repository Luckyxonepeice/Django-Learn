from django.shortcuts import render

rooms=[
    {'id':1, 'name':"Let's Learn"},
    {'id':2, 'name':'Design with Me'},
    {'id':3, 'name':'FrontEnd Developers'}
]
def home(request):
    context = {"rooms":rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    
    context = None
    for value in rooms:
        if value['id']==int(pk):
            context={'value':value['name']}
            break
    return render(request,'base/room.html',context)