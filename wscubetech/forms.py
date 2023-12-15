from django import forms
 
class userForm(forms.Form):
    num1=forms.CharField(label='Name',required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label='Message',required=True,widget=forms.Textarea(attrs={'class':"form-control"}))