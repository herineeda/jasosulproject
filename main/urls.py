
from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name ="index"),
    path('my_index', my_index, name="my_index"),
    path('create/', create, name ="create"),
    path('detail/<int:jss_id>', detail, name ="detail"),
    path('delete/<int:jss_id>', delete, name ="delete"),
    path('update/<int:jss_id>', update, name ="update"),

    #comment#
    path('create_comment/<int:jss_id>/', create_comment, name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>/', delete_comment, name="delete_comment"),
]