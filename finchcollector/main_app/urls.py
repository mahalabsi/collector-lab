from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('finches/', views.finch_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finch/<int:finch_id>/add_visit',views.add_visit, name='add_visit'),

        # CRUD for toys using CBV's
    path('homes/', views.HomeList.as_view(), name='homes_index'),
    path('homes/<int:pk>', views.HomeDetail.as_view(), name='homes_detail'),
    path('homes/create/', views.HomeCreate.as_view(), name='homes_create'),
    path('homes/<int:pk>/update/',views.HomeUpdate.as_view(), name='homes_update'),
    path('homes/<int:pk>/delete/',views.HomeDelete.as_view(), name='homes_delete'),
    # associate a toy w/ a cat (M:M)
    path('/finches/<int:finch_id>/assoc_home/<int:home_id>/', views.assoc_home, name='assoc_home'),
    # Unassociate a toy w/ a cat (M:M)
    path('/finches/<int:finch_id>/unassoc_home/<int:home_id>/', views.unassoc_home, name='unassoc_home'),

    path('/accounts/signup/', views.signup, name='signup'),
]