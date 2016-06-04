from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from models import menu, cat







def detail(request, id=None):
	instance=get_object_or_404(menu,id=id)
	context= {
		"product":instance,
		"title":"detail",

	}
	return render(request,"detail.html",context)






def product_list(request):
	query=menu.objects.all()
	context= {
		"products":query,
		"title":"list",

	}
	return render(request,"product_list.html",context)









def edit(request, id):
	
	return render(request,"edit.html",context)


def delete(request, id):
	
	return render(request,"delete.html",context)

def create(request, id):
	
	return render(request,"create.html",context)




















