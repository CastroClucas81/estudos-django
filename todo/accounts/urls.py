from django.urls import path

from . import views

'''
    é importante colocar o views. pra informar de onde está vindo
'''
urlpatterns = [
    #as_view é do proprio django
  path('register/', views.SignUp.as_view(), name="signup")
]