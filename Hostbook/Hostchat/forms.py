from django import forms
from .models import ChatMessage, HostMessage


class Chat1Message(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class Host1Message(forms.ModelForm):
    class Meta:
        model = HostMessage
        fields = '__all__'
