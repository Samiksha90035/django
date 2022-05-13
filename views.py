from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'homenew',
        'bdata':'welcome to django1',
        'clist':['PHP', 'java', 'python'],
        'numbers':[10,20,30,40,50],
    'students_details':[
           {'name':'pradeep','phone':'8798900977'},
            {'name':'testing','phone':'8299228912'}       
 ]
        }
    return render(request,"index.html.txt")
def aboutUs(request):
    return render(request,"aboutUs.html.txt ")
def course(request):
    return HttpResponse("<u><b>WELCOME TO THE COURSES!!</b></u>")
def coursedetails(request,courseid):
    return HttpResponse(courseid)
 
    




    
