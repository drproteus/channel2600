from django import forms
from chan.models import Post
from captcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError

class ThreadForm(forms.Form):
    subject = forms.CharField(max_length=80)
    author = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.FileField(required=False)
    captcha = ReCaptchaField()

    def clean(self):
        if not (self.cleaned_data.get('body') or self.cleaned_data.get('image')):
            raise ValidationError('Post requires either body or image')
        return self.cleaned_data

class PostForm(forms.Form):
    author = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.FileField(required=False)
    captcha = ReCaptchaField()

    def clean(self):
        if not (self.cleaned_data.get('body') or self.cleaned_data.get('image')):
            raise ValidationError('Post requires either body or image')
        return self.cleaned_data
