from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import registration

def home(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def webhook(request):

    # build a request object
    global fulfillmentText
    req = json.loads(request.body)
    # get action from json
    intent = req.get('queryResult').get('intent').get('displayName')
    # return a fulfillment message
    print('Entered webhook function')
    if intent == "Course Registration":
        #extract from database
        dept_name = req.get('queryResult').get('parameters').get('dept_name')
        registration_details =  registration.objects.filter(branch=dept_name).values('venue')
        print(registration_details)
        fulfillmentText = {'fulfillmentText': 'The venue of registration for '+ dept_name + ' is ' + registration_details[0]['venue'] + '.'}
    # return response
    return JsonResponse(fulfillmentText, safe=False)
