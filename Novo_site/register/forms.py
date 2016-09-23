from django import forms

class register(forms.Form):
    title = forms.CharField(max_length=5)
    fname= forms.CharField(max_length=30)
    lname = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    phoneNo = forms.CharField(max_length=15)
    diet = forms.CharField(max_length=10)
    medNo = forms.CharField(max_length=10)
    practAd = forms.CharField(max_length=50)
    #image = forms.FileField()
