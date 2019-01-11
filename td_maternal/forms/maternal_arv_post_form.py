from django import forms
from td_maternal_validators.form_validators import MarternalArvPostFormValidator

from ..models import MaternalArvPost, MaternalArvPostMed, MaternalArvPostAdh

from .form_mixins import SubjectModelFormMixin


class MaternalArvPostForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MarternalArvPostFormValidator

    class Meta:
        model = MaternalArvPost
        fields = '__all__'


class MaternalArvPostMedForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPostMed
        fields = '__all__'


class MaternalArvPostAdhForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MaternalArvPostAdh
        fields = '__all__'
