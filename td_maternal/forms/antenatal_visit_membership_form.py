from django import forms

from ..models import AntenatalVisitMembership


class AntenatalVisitMembershipForm(forms.ModelForm):

    class Meta:
        model = AntenatalVisitMembership
        fields = '__all__'
