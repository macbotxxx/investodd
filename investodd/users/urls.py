from django.urls import path

from investodd.users import views
urlpatterns = [
    path("my-account/", views.UserHomeView.as_view(), name="my_account"),
    
]
