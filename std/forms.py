from django import forms 


class RgistrationForm(forms.Form):
    fname=forms.CharField(label="FirstName", max_length=50)
    mname=forms.CharField(label="MiddleName", max_length=50)
    lname=forms.CharField(label="LastName", max_length=50)
    age=forms.IntegerField(label="Age")