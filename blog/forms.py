from django import forms
from .models import *

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body','name', 'email',)
        
        widgets = {
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'دیدگاه', 'style': 'width: 200%;'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید...'}),
        }
        
        
class UserReplyCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body','name',)
        
        widgets = {
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'پاسخ دیدگاه', 'style': 'height: 70px'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
