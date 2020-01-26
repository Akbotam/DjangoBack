import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Review, Reviewer

@csrf_exempt
def company_list(request):
   if request.method == 'GET':
      companies = Company.objects.all()
      json_companies = [c.to_json() for c in companies]
      return JsonResponse(json_companies, safe=False)
   elif request.method == 'POST':
       data = json.loads(request.body)
       company = Company()
       company.name = data.get('name', '')
       company.save()
       return JsonResponse(company.to_json())
   return JsonResponse({'error': 'bad request'})


def reviewer_list(request):
   reviewers = Reviewer.objects.all()
   json_reviewers = [rev.to_json() for rev in reviewers]
   return JsonResponse(json_reviewers, safe=False)

def review_list(request):
   reviews = Review.objects.all()
   json_reviews = [re.to_json() for re in reviews]
   return JsonResponse(json_reviews, safe=False)

@csrf_exempt
def company_detail(request, pk):
   try:
      company = Company.objects.get(id=pk)
   except Company.DoesNotExist as e:
         return JsonResponse({'error': str(e)})

   if request.method == 'GET':
      return JsonResponse(company.to_json())
   elif request.method == 'PUT':
      data = json.loads(request.body)
      company.name = data.get('name', company.name)
      company.save()
      return JsonResponse(company.to_json())
   elif request.method == 'DELETE':
      company.delete()
      return JsonResponse({})
   return  JsonResponse({'error': 'bad request'})


def company_reviews(request, pk):
   try:
      company = Company.objects.get(id=pk)
   except Company.DoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False)

   reviews = company.review_set.all()
   json_reviews = [r.to_json() for r in reviews]
   return JsonResponse(json_reviews, safe=False)
