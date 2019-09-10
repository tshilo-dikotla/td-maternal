from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import MaternalOffSchedule


class MaternalOffScheduleForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalOffSchedule
        fields = '__all__'
