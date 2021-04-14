from django.urls import path
from MyApp import views

app_name = "MyApp"


urlpatterns = [
    path('', views.view1, name="view1"),
    path('view2/<email>', views.view2, name="view2"),
    path('view3/<name>', views.view3, name="view3"),
    path('if/', views.if_demo, name="if_demo"),
    path('ifelse/', views.ifelse_demo, name="ifelse_demo"),
    path('for/', views.for_demo, name="for_demo"),
]




    