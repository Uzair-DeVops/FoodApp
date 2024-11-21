from django.shortcuts import render,redirect 
from django.http import  HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView

# from django.views.generic import DeleteView
# from django import reverse

# Create your views here.
# def index(request):
#     items = Item.objects.all()
#     context  = {
#         "items" : items,

#     }
#     return render(request, 'food/index.html',context)

class ItemListView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'



# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         "item" : item,
#     }
#     return render(request, 'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'




def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})
from django.urls import reverse_lazy

from django.urls import reverse_lazy
from django.contrib import messages

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'price', 'item_image']
    template_name = 'food/item-form.html'
    context_object_name = 'item'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        response = super().form_valid(form)
        # Add a success message
        messages.success(self.request, f"Item '{form.instance.item_name}' has been successfully added!")
        return response

    def get_success_url(self):
        # Redirect to the index page
        return reverse_lazy('food:index')


def edit_item(request,id):
    item = Item.objects.get(id=id)
    form =  ItemForm(request.POST or None , instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/edit-item.html', {'form': form , 'id': id})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete-item.html', {'item': item})

# class DeleteItem(DeleteView):
#     model = Item
#     def get_success_url(self):
#         return reverse('food:index')
#     template_name = 'food/delete-item.html'
#     context_object_name = 'item'

    

 
from django.http import JsonResponse

def clear_alert(request):
    if 'username' in request.session:
        del request.session['username']
    return JsonResponse({'status': 'success'})
