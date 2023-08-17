from django.shortcuts import render
from django.views import View
from home.models import Staff,Contact,Client,Room

# Create your views here.

# class Staffhome(View):
#     def get(self,request):
#         if request.session['email'] is not None:
#             user=Staff.objects.filter(email=request.session['email'])
#         return render(request,'staffhome.html',{'form':user})

class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquiry.html',{'form':customer})
    
class Clients(View):
    def get(self,request):
        customer=Client.objects.all()
        # consumer=Room.objects.all()
        return render(request,'client.html',{'consumer':customer})


class Staffprofile(View):
    def get(self,request):
        if request.session['email'] is not None:
            user=Staff.objects.filter(email=request.session['email'])
        return render(request,'staffprofile.html',{'form':user})
   
# class clientRoom(View):
#     def get(self,request):
#         if request.session['name'] is not None:
#             customer=Room.objects.filter(name=request.session['name'])
#         return render(request,'client.html',{'form':customer})

# class clientRoom(View):
#     def get(self,request):
#         customer=Room.objects.all()
#         return render(request,'client.html',{'room':customer})