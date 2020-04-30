from django import forms
from django.forms import ModelForm
from .models import *
import decimal
from functools import partial

class AddProjectRatingForm(forms.ModelForm):   
    class Meta:
        model = Project_Ratings
        fields = ('rating',)

class UserDonationsModelForm(forms.ModelForm):   

    class Meta:
        model=User_Donations
        fields = ['amount']
  
    def clean_amount(self):             
        amount = self.cleaned_data.get('amount')        
        if amount <= 0:
            raise forms.ValidationError("Amount is invalid")
        return amount
    
class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
        ]

class DateInput(forms.DateInput):
    input_type = 'date'

class new_project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'details',
            'total_target',
            'start_date',
            'end_date',
            'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'style':'width:500px'}),
            'details': forms.TextInput(attrs={'class':'form-control'}),
            'total_target': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': DateInput(attrs={'class':'form-control'}),
            'end_date': DateInput(attrs={'class':'form-control'}),
            }

class NewProjectPicturesForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=Project_Pictures
        fields = ['picture',]
        widgets = {'project': forms.HiddenInput()}

class ReportForm(ModelForm):
    class Meta:
        model = Project_Reports
        fields = ['report',]

class CommentReportForm(ModelForm):
    class Meta:
        model = Comment_Reports
        fields = ['report',]

class reply_form(ModelForm):
    class Meta:
        model = Comment_Replies
        fields = ['content']