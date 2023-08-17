from django.urls import path,include
from . import views
urlpatterns = [
    path('staffprofile',views.Staffprofile.as_view(),name="staffprofile"),
    # path('staffhome',views.Staffhome.as_view(),name="staffhome"),
    path('enquiry/',views.Enquiry.as_view(),name="enquiry"),
    path('client/',views.Clients.as_view(),name="clients"),
    # path('clientroom/',views.clientRoom.as_view(),name="clientroom"),
    # path('logout/',views.Logout.as_view(),name="logout"),
    # path('delete/',views.Delete.as_view(),name="delete"),
  
    # path('editprofile/',views.Editprofile.as_view(),name="editprofile"),
]