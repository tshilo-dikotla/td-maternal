from django.db import models
from django.utils.html import mark_safe
from edc_base.model_mixins import BaseUuidModel
from .model_mixins import CrfModelMixin


class ClinicianNotes(CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = 'Maternal Clinician Notes'
        verbose_name_plural = 'Maternal Clinician Notes'


class ClinicianNotesImage(BaseUuidModel):

    clinician_notes = models.ForeignKey(
        ClinicianNotes,
        on_delete=models.PROTECT,
        related_name='maternal_clinician_notes',)
    image = models.ImageField(upload_to='media/')

    def clinician_notes_image(self):
        return mark_safe(
            '<a href="%(url)s">'
            '<img src="%(url)s" style="padding-right:150px" width="150" height="100" />'
            '</a>' % {'url': self.image.url})

    clinician_notes_image.short_description = 'Clinician Notes Image'
    clinician_notes_image.allow_tags = True
