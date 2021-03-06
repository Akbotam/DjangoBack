from django.urls import path
from api import views


#urlpatterns = [
     #path('companies/', views.company_list),
     #path('reviews/', views.review_list),
     #path('companies/<int:pk>/', views.company_detail),
     #path('companies/<int:pk>/reviews/', views.company_reviews)
#]

urlpatterns = [
     path('companies/', views.CompanyList.as_view()),
     path('reviews/', views.ReviewList.as_view(), name = 'review.views.ReviewList'),
     path('companies/<int:pk>/', views.CompanyDetail.as_view()),
     path('users/', views.UserList.as_view()),
     path('login/', views.login),
     path('logout/', views.logout),
     path('companies/<int:pk>/reviews/', views.company_reviews)
]