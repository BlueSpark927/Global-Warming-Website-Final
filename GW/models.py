from django.db import models
from django.utils.translation import gettext as _
from numpy import mod

class Months(models.Model):
    State = models.CharField(_("State"), max_length=225)
    S_C = models.CharField(_("State Code"), max_length =225)
    Year = models.CharField(_("Year"), max_length =225)
    Month = models.CharField(_("Month"), max_length =225)
    Max = models.FloatField(_("Avg Daily Max Air Temperature (F)"))
    Min = models.FloatField(_("Avg Daily Min Air Temperature (F)"))


class Year(models.Model):
    State = models.CharField(_("State"), max_length=225)
    S_C = models.CharField(_("State Code"), max_length =225)
    Year = models.CharField(_("Year"), max_length =225)
    Max = models.FloatField(_("Avg Daily Max Air Temperature (F)"))
    Min = models.FloatField(_("Avg Daily Min Air Temperature (F)"))