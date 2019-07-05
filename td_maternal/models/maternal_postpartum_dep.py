from django.db import models

from ..choices import ANXIOUS, SAD, PANICK, TOP, CRYING, HARM
from ..choices import LAUGH, ENJOYMENT, BLAME, UNHAPPY
from .model_mixins import CrfModelMixin


class MaternalPostPartumDep(CrfModelMixin):

    laugh = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have been able to laugh "
        "and see the funny side of things?",
        choices=LAUGH,
    )

    enjoyment = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I looked forward with enjoyment"
        " of things?",
        choices=ENJOYMENT,
    )

    blame = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have blamed myself unnecessarily "
        "when things went wrong",
        choices=BLAME,
    )

    anxious = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have anxious or worried for no"
        " good reason",
        choices=ANXIOUS,
    )

    panick = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have felt scared or panicky for"
        " no good reason",
        choices=PANICK,
    )

    top = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, things have been getting"
        " on top of me",
        choices=TOP,
    )

    unhappy = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have been so unhappy that I have"
        " had difficulty sleeping",
        choices=UNHAPPY,
    )

    sad = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have felt sad or miserable",
        choices=SAD,
    )

    crying = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, I have been so unhappy that I have"
        " been crying",
        choices=CRYING,
    )

    self_harm = models.CharField(
        max_length=75,
        verbose_name="In the past 7 days, the thought of harming myself has"
        " occured to me",
        choices=HARM,
    )

    total_score = models.IntegerField(
        verbose_name="Total score",
        default="",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.total_score = self.calculate_depression_score()
        super().save(*args, **kwargs)

    def calculate_depression_score(self):
        score = 0
        pos = {'laugh': LAUGH,
               'enjoyment': ENJOYMENT,
               'anxious': ANXIOUS}

        neg = {'blame': BLAME, 'panick': PANICK, 'top': TOP,
               'unhappy': UNHAPPY, 'sad': SAD,
               'crying': CRYING, 'self_harm': HARM}
        for f in self._meta.get_fields():
            if f.name in ['laugh', 'enjoyment', 'anxious']:
                choice_list = (getattr(self, f.name), getattr(self, f.name))
                score += pos.get(f.name).index(choice_list)
            elif f.name in ['blame', 'panick', 'top',
                            'unhappy', 'sad', 'crying', 'self_harm']:
                choice_list = (getattr(self, f.name), getattr(self, f.name))
                score += tuple(reversed(neg.get(f.name))).index(choice_list)
        return score

    class Meta(CrfModelMixin.Meta):
        app_label = 'td_maternal'
        verbose_name = "Maternal Post Partum: Depression"
