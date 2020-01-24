from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from api.models import Company, Review, Reviewer

def company_list(request):
   companies = Company.objects.all()
   json_companies = [c.to_json() for c in companies]
   return JsonResponse(json_companies, safe=False)

def reviewer_list(request):
   reviewers = Reviewer.objects.all()
   json_reviewers = [rev.to_json() for rev in reviewers]
   return JsonResponse(json_reviewers, safe=False)

def review_list(request):
   reviews = Review.objects.all()
   json_reviews = [re.to_json() for re in reviews]
   return JsonResponse(json_reviews, safe=False)

def company_detail(request, pk):
   try:
      company = Company.objects.get(id=pk)
   except Company.DoesNotExist as e:
         return JsonResponse({'error': str(e)}, safe=False)

   return JsonResponse(company.to_json())

def company_reviews(request, pk):
   try:
      company = Company.objects.get(id=pk)
   except Company.DoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False)

   reviews = company.review_set.all()
   json_reviews = [r.to_json() for r in reviews]
   return JsonResponse(json_reviews, safe=False)
