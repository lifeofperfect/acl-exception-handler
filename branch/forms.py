from django import forms
from acl.models import Alert


class CreateAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        exclude = ['role','age_analysis','Date_Uploaded','alias_name','CAMT_Reveiewer','Date_Regularised','alert_message', 'Count2']

        

