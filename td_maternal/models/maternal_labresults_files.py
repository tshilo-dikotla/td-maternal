from django.db import models
from django.utils.html import mark_safe
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from .model_mixins import CrfModelMixin


class MaternalLabResultsFiles(CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Lab Results Files'
        verbose_name_plural = 'Maternal Lab Results Files'


class LabResultsFile(BaseUuidModel):

    lab_results = models.ForeignKey(
        MaternalLabResultsFiles,
        on_delete=models.PROTECT,
        related_name='maternal_lab_results',)

    image = models.FileField(upload_to='maternal_lab_results/')

    user_uploaded = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='user uploaded',)

    datetime_captured = models.DateTimeField(
        default=get_utcnow)

    def lab_results_preview(self):
        return mark_safe(
            '<iframe src="%(url)s" style="border:none" height="120" width="120"'
            'title="lab results" scrolling="yes"></iframe>' % {'url': self.image.url})

    lab_results_preview.short_description = 'Preview'
    lab_results_preview.allow_tags = True
