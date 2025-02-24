from django .urls import path
from .import views as v

urlpatterns=[
    path('',v.home,name='home'),
    path('register/',v.register,name='register'),
    path('userlogin/',v.userlogin,name='userlogin'),
    path('userlogout/',v.userlogout,name='userlogout'),
    
    path('packages/',v.viewpackage,name='viewpackage'),
    path('packages/create/',v.addpackage,name='addpackage'),
    path('packages/<int:package_id>/book/',v.bookpackage,name='bookpackage'),

    path('packages/edit/<int:package_id>',v.editpackage,name='editpackage'),
    path('packages/delete/<int:package_id>',v.deletepackage,name='deletepackage'),

    path('packages/pending/',v.pendingpackage,name='pendingpackage'),
    path('admin/packages/approve/<int:package_id>/',v.approvepackage,name='approvepackage'),
]


