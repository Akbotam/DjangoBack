import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Review
from api.serializers import CompanySerializer, CompanySerializer2, ReviewSerializer

@csrf_exempt
def company_list(request):
   if request.method == 'GET':
      companies = Company.objects.all()
      serializer = CompanySerializer2(companies, many=True)
      return JsonResponse(serializer.data, safe=False)
   elif request.method == 'POST':
       data = json.loads(request.body)
       serializer = CompanySerializer2(data=data)
       if serializer.is_valid():
          serializer.save()
          return JsonResponse(serializer.data)
       return JsonResponse(serializer.errors)
       #company = Company()
       #company.name = data.get('name', '')
       #company.save()
       #return JsonResponse(company.to_json())
   return JsonResponse({'error': 'bad request'})


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
      serializer = CompanySerializer(company)
      return JsonResponse(serializer.data)
   elif request.method == 'PUT':
      data = json.loads(request.body)
      serializer = CompanySerializer2(instance=company, data=data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data)
      return JsonResponse(serializer.errors)
      #company.name = data.get('name', company.name)
      #company.save()
      #return JsonResponse(company.to_json())
   elif request.method == 'DELETE':
      company.delete()
      return JsonResponse({})
   return  JsonResponse({'error': 'bad request'})


def company_reviews(request, pk):
   try:
      company = Company.objects.get(id=pk)
   except Company.DoesNotExist as e:
      return JsonResponse({'error': str(e)})

   reviews = company.review_set.all()
   serializer = ReviewSerializer(reviews, many=True)
   return JsonResponse(serializer.data, safe=False)
   #json_reviews = [r.to_json() for r in reviews]
   #return JsonResponse(json_reviews, safe=False)
