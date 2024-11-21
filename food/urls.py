from . import views
from django.urls import path
app_name = "food"
urlpatterns = [
    #/food/ 
    path('', views.ItemListView.as_view(),name="index"),
    # /food/1/
    path("<int:pk>/",views.FoodDetail.as_view(),name="detail"),
    # add item
    path("add/",views.CreateItem.as_view( ),name="create_item"),
    # edit item
    path("edit/<int:id>/",views.edit_item,name="edit_item"),
    # delete item
    path("delete/<int:id>/",views.delete_item,name="delete_item"),
    path('clear_alert/', views.clear_alert, name='clear_alert'),

] 