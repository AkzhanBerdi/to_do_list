from django import forms

class TaskForm(forms.Form):
    title = forms.CharFIeld(label='Task', max_length=100)