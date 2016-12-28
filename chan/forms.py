from django import forms

class ThreadForm(forms.Form):
    subject = forms.CharField(max_length=80)
    author = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea)

class PostForm(forms.Form):
    author = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea)
