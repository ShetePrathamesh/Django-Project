from django.conf.urls import url

from medicine import views

urlpatterns = [
    url('add/', views.add,name="add"),
    url('', views.show,name="show"),
    url('update/<int:Id>', views.update,name="update"),
    url('delete/<int:Id>', views.delete,name="delete"),
]
