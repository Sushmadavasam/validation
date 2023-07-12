from typing import Any, Dict
from django import forms
def validate_for_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.ValidationError("First letter should not be a")

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('len is less than 5')
    
class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField()
    Remail=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    
    def clean(self) :
        e=self.cleaned_data['email']
        Re=self.cleaned_data['Remail']
        if e !=Re:
            raise forms.ValidationError('Both are not same')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')