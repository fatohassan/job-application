from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        #exclude=('first_name',)
        fields = '__all__'
        labels ={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter your email')
        }
        error_messages={
            'first_name':{
                'required':_('not')
            },
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid last name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False, label='Enter your first name:', help_text='Enter character only')
#     last_name = forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

#     def clean_first_name(self):
#         data = self.cleaned_data["first_name"]
#         if "," in data:
#             raise forms.ValidationError("Name invalid")
#         return data
