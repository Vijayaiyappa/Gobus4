from django import forms

class userdatain(forms.Form):
   source= forms.CharField(max_length=100)
   destination= forms.CharField(max_length=100)
   middleroot= forms.CharField(max_length=100)
   arrive_t= forms.CharField(max_length=100)
   busname= forms.CharField(max_length=100)

