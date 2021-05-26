from django import forms

class Question(forms.Form):
    answer = forms.IntegerField()