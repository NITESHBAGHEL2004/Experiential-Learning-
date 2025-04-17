
from django.db import models



class academic_year(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class school(models.Model):
    academic_year = models.ForeignKey(academic_year, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class program(models.Model):
    school = models.ForeignKey(school, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class branch(models.Model):
    program = models.ForeignKey(program, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class faculty(models.Model):
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class semester(models.Model):
    faculty = models.ForeignKey(faculty, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class section(models.Model):
    semester = models.ForeignKey(semester, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class subject(models.Model):
    section = models.ForeignKey(section, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class pbl(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class PBLActivity(models.Model):
    academic_year = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    program = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=100, blank=True, null=True)
    section = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    pbl = models.CharField(max_length=100, blank=True, null=True)
    other_activity = models.CharField(max_length=255, blank=True, null=True)
    description  = models.TextField( blank=True, null=True)
    activitydocument = models.FileField(upload_to='documents/', blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    closing_date = models.DateField(blank=True, null=True)
    document_upload_1 = models.FileField(upload_to='uploads/', blank=True, null=True)
    document_upload_2 = models.FileField(upload_to='uploads/', blank=True, null=True)
    document_upload_3 = models.FileField(upload_to='uploads/', blank=True, null=True)
    lms_links1 = models.URLField(null=True)
    lms_links2= models.URLField(null=True)
    lms_links3 = models.URLField(null=True)
    lms_links4 = models.URLField(null=True)
    lms_links5 = models.URLField(null=True)
    marks = models.CharField(max_length=100,default=list, blank=True,null=True)
      

    def __str__(self):
        return f"PBL Activity for {self.academic_year} - {self.subject}"
    
#part edit



