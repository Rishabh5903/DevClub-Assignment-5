from django.urls import path,include
from . import views
# from Documents import views as document_view
urlpatterns = [
    # path('',views.Documents,name="home"),
    path('view',views.show_file,name="view")

]