from random import choices
from django import forms
# from .models import Psychic

# psy1 = Psychic('Psychic - 1')
# psy2 = Psychic('Psychic - 2')

# CHOICES = [
#     psy1.psy_number,
#     psy2.psy_number
# ]

class UserNumberForm(forms.Form):
    user_num = forms.CharField(label='Введите двузначное число загаданное ранее', max_length=2, min_length=2)