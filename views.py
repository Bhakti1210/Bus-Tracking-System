from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


visit = False 

# Create your views here.
def home(request):
   print("IN HOME")
    if (visit == True):
    	data1 = request.POS['psw']
    	data2 = request.POST['psw-repeat']
    	print(data1)
    		if(data1 == data2):
				return render(request,'action.html')
			else:
				visit=False
				return render(request,'login.html')
	else:
		return render(request,'login.html')
					





def second(request):
	print("IN Secondd")
	data='You Have Logged In Successfully'
	return render(request,'secondslide.html', {'data':data})

	name1 = request.POST['name1']
	passs = request.POST['mb']



def action(request):
	visit = True
	print("IN ACtiojn")
	return render(request,'action.html')
	
		

	
