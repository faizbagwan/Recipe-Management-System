from django.shortcuts import redirect, render
from .models import *

# Create your views here.


def receipe_list(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')


        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        return redirect('receipe_list')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(receipe_name__icontains=search)


    context = {
            'receipe_list': queryset
        } 
       # print(receipe_description)
       #print(receipe_name)

    return render(request, 'receipe_list.html', context)


def delete_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('receipe_list')

def update_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    context = {
        'receipe': receipe }
    
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description
        if receipe_image:
            receipe.receipe_image = receipe_image

        receipe.save()

        return redirect('receipe_list')
    
    return render(request, 'update_receipe.html', context)