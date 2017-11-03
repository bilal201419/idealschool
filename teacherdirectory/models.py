# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
	tchr_ID = models.AutoField(primary_key=True)
	tchr_First_Name = models.CharField(max_length=30)
	tchr_Last_Name = models.CharField(max_length=30)
	tchr_Father_Name = models.CharField(max_length=30)
	tchr_Email = models.CharField(max_length=100) # check length and datatype
	tchr_NID = models.CharField(max_length=30) # can be IntegerField, but some uses Jold Number and Safha Number
	tchr_Nationality = models.CharField(max_length=30)
	tchr_Business_Ph = models.IntegerField(default=0)
	tchr_Home_Ph = models.IntegerField(default=0)
	tchr_Mobile_No = models.IntegerField(default=0)
	tchr_Cur_Add_VillorDist = models.CharField(max_length=30)
	tchr_Cur_Add_Province = models.CharField(max_length=30)
	tchr_Cur_Add_Country = models.CharField(max_length=30)
	tchr_Prmnt_Add_VillorDist = models.CharField(max_length=30)
	tchr_Prmnt_Add_Province = models.CharField(max_length=30)
	tchr_Prmnt_Add_Country = models.CharField(max_length=30)
	tchr_Faculty_ID = models.IntegerField(default=0) # using number will be okay?
	tchr_Faculty_Type = models.CharField(max_length=30)
	tchr_Department = models.CharField(max_length=30)
	tchr_Office = models.CharField(max_length=30)
	tchr_DOB = models.DateField(null=True)
	tchr_DOH = models.DateField(null=True)
	tchr_Salary = models.DecimalField(max_digits=7, decimal_places=2) # check datatype 
	tchr_Level_Degree = models.CharField(max_length=50)
	tchr_Focus_Area = models.CharField(max_length=200)
	tchr_School_ProgName = models.CharField(max_length=100)
	tchr_Emg_C_Name = models.CharField(max_length=30)
	tchr_Emg_C_PhNo1 = models.IntegerField(default=0)
	tchr_Emg_C_PhNo2 = models.IntegerField(default=0)
	tchr_Emg_C_Relationship = models.CharField(max_length=30)
	tchr_MI_Blood_Group = models.CharField(max_length=3)
	tchr_MI_Allergies = models.CharField(max_length=200)
	tchr_Leave_Date = models.DateField(null=True)
	tchr_Leave_Reason = models.CharField(max_length=200)
	tchr_Leave_ChkLiabilites = models.CharField(max_length=200)