
from django.contrib import admin
from django.urls import path
from patient_list import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_view, name= 'formshow'),
    path('delete/<int:id>/',views.delete_data, name = "deletedata"),
    path('updatedata/<int:id>/', views.update_data, name = "updatedata"),
]
