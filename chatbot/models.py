from django.db import models


class department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=15)
    dept_code = models.CharField(max_length=2)
    dept_core = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.dept_name


class student(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=9)
    stud_name = models.CharField(max_length=25)
    mail_id = models.EmailField()
    dept_name = models.ForeignKey(department, on_delete=models.CASCADE)
    hostel = models.CharField(max_length=12)
    room_no = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.roll_no


class RegistrationDetails(models.Model):
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    venue = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Registration Details"

    def __str__(self):
        return self.dept.dept_name


class Slot(models.Model):
    slot = models.CharField(primary_key=True, max_length=2)

    class Meta:
        verbose_name_plural = "Slot"

    def __str__(self):
        return self.slot

class Professor(models.Model):
    prof_name = models.TextField(primary_key=True)
    room_no = models.CharField(max_length=7)
    research_area = models.CharField(max_length=50)
    dept_name = models.ForeignKey(department, on_delete=models.CASCADE)
    website = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "Professor"

    def __str__(self):
        return self.prof_name


class course(models.Model):
    dept_name = models.ForeignKey(department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(primary_key=True, max_length=5)
    course_instructor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    course_venue = models.CharField(max_length=8)
    course_content = models.URLField()
    grading_schema = models.CharField(max_length=300)
    prerequisites = models.CharField(max_length=10)
    course_credits = models.IntegerField()
    references = models.TextField(max_length=500)
    compulsary = models.BooleanField()
    semester = models.IntegerField()
    elective = models.BooleanField()
    lab = models.BooleanField()

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_code


class TimeTable(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = "Timetable"

    def __str__(self):
        return self.slot.slot + "-" + self.day


class RegisteredCourses(models.Model):
    roll_no = models.ForeignKey(student, on_delete=models.CASCADE)
    course_reg = models.ForeignKey(course, on_delete=models.CASCADE)
    attendance = models.IntegerField()

    class Meta:
        verbose_name_plural = "Registered Courses"

    def __str__(self):
        return self.roll_no.roll_no + "-" + self.course_reg.course_code
