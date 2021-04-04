from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import RegistrationDetails,student,course,TimeTable,RegisteredCourses

def home(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def webhook(request):
   # build a request object
   global fulfillmentText
   req = json.loads(request.body)
   # get intent from json
   intent = req.get('queryResult').get('intent').get('displayName')
   # return a fulfillment message
   print('Entered webhook function')
   if intent == "Course Registration":

       dept_name = req.get('queryResult').get('parameters').get('dept_name')
       registration_details =  RegistrationDetails.objects.filter(branch=dept_name).values('venue', 'start_time' , 'end_time')
       print(registration_details)
       fulfillmentText = {'fulfillmentText': 'Registration for '+ dept_name + ' is ' + ' from ' + registration_details[0]['start_time'].strftime("%H:%M") + ' to ' + registration_details[0]['end_time'].strftime("%H:%M") + ' on ' + registration_details[0]['end_time'].strftime("%d-%m-%Y") + ' at '  + registration_details[0]['venue'] }

   elif intent == "Student Details":

       roll = req.get('queryResult').get('parameters').get('rollno')
       student_details = student.objects.filter(roll_no=roll).values()
       print(student_details)
       stud_details = ""
       keys_values = student_details[0].items()
       for key,value in keys_values:
           stud_details += str(key) + ' : ' + str(value) + "\n"
       print(stud_details)
       fulfillmentText = {'fulfillmentText':  stud_details}

   elif intent == "TimeTable_RollNo_Course":

       code = req.get('queryResult').get('parameters').get('Course-Code')
       course_slot = course.objects.filter(course_code=code).values('slot')
       schedule = TimeTable.objects.filter(slot=course_slot[0]['slot']).values('day','start_time','end_time')
       timetable = ""
       for values in schedule:
           timetable+= (values['day'] + "     " +values['start_time'].strftime("%H:%M") + "-" + values['end_time'].strftime("%H:%M") + "\n")
       fulfillmentText = {'fulfillmentText': timetable}

   elif intent == "TimeTable_RollNo":

       roll = req.get('queryResult').get('parameters').get('RollNo')
       courses = RegisteredCourses.objects.filter(roll_no=roll).values('course_reg')
       s=""
       for values1 in courses:
           timetable = ""
           timetable = "Class schedule for " + values1['course_reg'] +": \n"
           course_slot = course.objects.filter(course_code=values1['course_reg']).values('slot')
           schedule = TimeTable.objects.filter(slot=course_slot[0]['slot']).values('day', 'start_time', 'end_time')
           for values2 in schedule:
               timetable += (values2['day'] + "     " + values2['start_time'].strftime("%H:%M") + "-" + values2['end_time'].strftime("%H:%M") + "\n")
           s+=timetable

       fulfillmentText = {'fulfillmentText': s}

   elif intent == "MyCourses":

       roll = req.get('queryResult').get('parameters').get('rollno')
       courses = RegisteredCourses.objects.filter(roll_no=roll).values('course_reg')
       if len(courses) == 0:
           s = roll + " did not register for any courses"

       else:
           s = "List of registered courses of " + roll + " are "

       for c in courses:
           s = s + ", " + (c['course_reg'])
       fulfillmentText = {'fulfillmentText': s}

   elif intent == "prerequisite":

       code = req.get('queryResult').get('parameters').get('course-code')
       pre = course.objects.filter(course_code=code).values('prerequisites')
       if len(pre) == 0:
           s = "There are no prerequisites for this course"

       else:
            s = "Prerequisites of this course are"

       for c in pre:
           s = s + " " + (c['prerequisites'])
       fulfillmentText = {'fulfillmentText': s}

   elif intent == "GradingScheme":

       code = req.get('queryResult').get('parameters').get('Course-Code')
       grading = course.objects.filter(course_code=code).values('grading_schema')
       print(grading)
       s=""
       if len(grading) == 0:
           s = "Grading scheme is not mentioned"
       else:
           s = grading[0]['grading_schema']
       fulfillmentText = {'fulfillmentText': s}

   elif intent == "AttendanceByCourse":

       code = req.get('queryResult').get('parameters').get('course-code')
       print(code)
       roll = req.get('queryResult').get('parameters').get('rollno')
       att = RegisteredCourses.objects.filter(roll_no=roll,course_reg=code).values()
       attendance = "Attendance of " + str(roll) + " in " + str(code) + " is " + str(att[0]['attendance'])
       fulfillmentText = {'fulfillmentText': attendance}


   elif intent == "AttendanceByRoll":

       roll = req.get('queryResult').get('parameters').get('rollno')
       att = RegisteredCourses.objects.filter(roll_no=roll).values()
       print(att)
       s = "Attendance for " + roll + "\n"
       for it in att:
           s += str(it['course_reg_id']) +" - " + str(it['attendance']) + "\n"
       fulfillmentText = {'fulfillmentText':s}

   elif intent == "CourseDetails":

       code = req.get('queryResult').get('parameters').get('course-code')
       content = course.objects.filter(course_code=code).values('course_name','course_code','course_instructor','slot_id','course_venue','course_credits')
       course_details = ""
       keys_values = content[0].items()
       for key, value in keys_values:
           course_details += str(key) + ' : ' + str(value) + " \n "
       print(course_details)
       fulfillmentText = {'fulfillmentText': course_details}

   elif intent == "CourseReferences":

       code = req.get('queryResult').get('parameters').get('course-code')
       ref = course.objects.filter(course_code=code).values('references')
       fulfillmentText = {'fulfillmentText': ref[0]['references']}

   elif intent == "CourseWebsite":

       code = req.get('queryResult').get('parameters').get('course-code')
       content = course.objects.filter(course_code=code).values('course_content')
       print(content)
       fulfillmentText = {'fulfillmentText': content[0]['course_content']}

   elif intent == 'CourseVenue':

       code = req.get('queryResult').get('parameters').get('course-code')
       venue = course.objects.filter(course_code=code).values('course_venue')
       print(venue)
       fulfillmentText = {'fulfillmentText': "Venue of " + code + " is   " + venue[0]['course_venue']}

   elif intent == 'CompulsoryCourses':

       dept = req.get('queryResult').get('parameters').get('dept_name')
       sem = req.get('queryResult').get('parameters').get('semester')
       compulsary = course.objects.filter(dept_name=dept,semester = sem,compulsary = 1).values('course_code')
       print(compulsary)
       compulsarycourses = ""
       if len(compulsary) == 0:
           compulsarycourses = "There are no compulsary courses in this semester"
       else:
           compulsarycourses = "List of compulsary courses in semester " + str(int(sem)) + " for " + str(dept) + " are "

       for c in compulsary:
           compulsarycourses = compulsarycourses + " "  + (c['course_code'])
       fulfillmentText = {'fulfillmentText': compulsarycourses}

   elif intent == 'SemesterCourses':

       dept = req.get('queryResult').get('parameters').get('dept_name')
       sem = req.get('queryResult').get('parameters').get('semester')
       list = course.objects.filter(dept_name=dept,semester=sem).values('course_code')
       print(list)
       semcourses = "List of courses available in semester " + str(int(sem)) + " for " + str(dept) + " are "
       for c in list:
           semcourses = semcourses + " " + (c['course_code'])
       fulfillmentText = {'fulfillmentText': semcourses}

   return JsonResponse(fulfillmentText, safe=False)

