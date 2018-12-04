from django import forms
from ..models import DeathReport


class MaternalDeathReportForm(forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'
