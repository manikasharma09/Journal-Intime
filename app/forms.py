from django.forms import ModelForm
from .models import *


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ('text',)
    