from django.forms import ModelForm
from .models import Months

class MonthsForm(ModelForm):
	class Meta:
		model = Months
		fields = ['State', 'Year', ]