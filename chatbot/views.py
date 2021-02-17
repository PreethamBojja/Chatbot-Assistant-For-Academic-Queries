from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import registration,student

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
        dept_name = req.get('queryResult').get('parameters').get('dept_name')
        registration_details =  registration.objects.filter(branch=dept_name).values('venue', 'start_time' , 'end_time')
        print(registration_details)
        fulfillmentText = {'fulfillmentText': 'Registration for '+ dept_name + ' is ' + ' from ' + registration_details[0]['start_time'].strftime("%H:%M") + ' to ' + registration_details[0]['end_time'].strftime("%H:%M") + ' on ' + registration_details[0]['end_time'].strftime("%d-%m-%Y") + ' at '  + registration_details[0]['venue'] }
    elif intent == "Student Details":
        roll = req.get('queryResult').get('parameters').get('rollno')
        student_details = student.objects.filter(Roll_No=roll).values()
        stud_details = ""
        keys_values = student_details[0].items()
        for key,value in keys_values:
            stud_details += str(key) + ' : ' + str(value) + "\n"
        print(stud_details)
        fulfillmentText = {'fulfillmentText':  stud_details}
    return JsonResponse(fulfillmentText, safe=False)
