"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""


from django.contrib import admin
from django.urls import path,include
from medicine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",include("medicine.urls"))
    path('add/', views.add,name="add"),
    path('', views.show,name="show"),
    path('update/<int:Id>', views.update,name="update"),
    path('delete/<int:Id>', views.delete,name="delete"),
]

admin.site.site_header = "Medical Store"
admin.site.site_title = "Medicine Record Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"