from django.urls import path
from api import views


#urlpatterns = [
     #path('companies/', views.company_list),
     #path('reviewers/', views.reviewer_list),
     #path('reviews/', views.review_list),
     #path('companies/<int:pk>/', views.company_detail),
     #path('companies/<int:pk>/reviews/', views.company_reviews)
#]

urlpatterns = [
     path('companies/', views.CompanyList.as_view()),
     #path('reviewers/', views.reviewer_list),
     #path('reviews/', views.review_list),
     path('companies/<int:pk>/', views.CompanyDetail.as_view()),
     path('users/', views.UserList.as_view())
     #path('companies/<int:pk>/reviews/', views.company_reviews)
]