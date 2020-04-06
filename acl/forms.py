from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Alert



class CreateAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['Exception_Category', 'Affiliate_Code', 'Affiliate_Name','Initiating_Branch', 'Zone', 'Region', 'Trn_Ref_no','Acccount_Number','Account_Name','msisdn','ACCOUNT_CLASS','account_tier','DRCR_IND','ACY_CURR_BALANCE','AcctPND','TnxCount','DrMeanMaxAmt','CrMeanMaxAmt', 'Currency','LCY_USD_RATE','Amount_Involved_LCY', 'Amount_at_Risk_LCY', 'Inputter', 'Authoriser', 'USERID_Inputter','USERID_Authoriser','Month','Count2','role']


class CreateUserForm(UserCreationForm):
    #group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2',]





class Alert_update_form(forms.ModelForm):
    class Meta:
        model = Alert
        fields = [
            'Exception_By_Category_Type',
            'Summary_Of_Incidence_and_CAMT_observation_during_Investigation',
            'OPERATORS_RESPONSE',
            'Root_Cause_Tag',
            'OPERATORS_RESPONSE',
            'Category_By_Root_Cause',
            'Status_REGULARIZED_UNREGULARIZED',
            'Loss_prevented_LCY',
            'Loss_prevented_USD',
            'Amount_at_Risk_LCY',
            'Activity',
            'Loss_Category',
            'camtDecision',
            'statusCheck',
        ]


class SearchForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['id','Exception_Category', 'Affiliate_Code','Affiliate_Name','USERID_Inputter']



class UpdateFalsePositive(forms.ModelForm):
    class Meta:
        model = Alert
        fields = [
            
            'Summary_Of_Incidence_and_CAMT_observation_during_Investigation',
            #'statusCheck'
            
        ]

class UpdateTruePositive(forms.ModelForm):
    class Meta:
        model = Alert
        fields = [
            'Exception_By_Category_Type',
            'Summary_Of_Incidence_and_CAMT_observation_during_Investigation',
            'OPERATORS_RESPONSE',
            'Root_Cause_Tag',
            'OPERATORS_RESPONSE',
            'Category_By_Root_Cause',
            'Status_REGULARIZED_UNREGULARIZED',
            'Loss_prevented_LCY',
            'Loss_prevented_USD',
            'Amount_at_Risk_LCY',
            'Activity',
            'statusCheck',
        ]

