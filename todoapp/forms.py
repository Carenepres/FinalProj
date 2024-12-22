from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "myinput", "placeholder": "Enter Todo"}))
    custom_error_message = ""

    class Meta:
        model = Task
        fields = ["title"]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.isdigit():
            self.custom_error_message = "Task title cannot be only numbers."
        return title