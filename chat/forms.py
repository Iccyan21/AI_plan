from django import forms

class ServiceForm(forms.Form):
    service_details = forms.CharField(widget=forms.Textarea, label='サービスの詳細')
