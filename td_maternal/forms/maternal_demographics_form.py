from ..models import MaternalDemographics

from .form_mixins import SubjectModelFormMixin


class MaternalDemographicsForm(SubjectModelFormMixin):

    class Meta:
        model = MaternalDemographics
        fields = '__all__'
