from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Task', max_length=100)
    description = forms.CharField(label='Text',max_length=200 )