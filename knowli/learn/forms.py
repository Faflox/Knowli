from django import forms

class AdditionTestForm(forms.Form):
    answer_1 = forms.IntegerField(label='1. 5 + 7 = ')
    answer_2 = forms.IntegerField(label='2. 6 + 2 = ')
    answer_3 = forms.IntegerField(label='3. 12 - 12 = ')
    answer_4 = forms.IntegerField(label='4. 0 - 7 = ')
    answer_5 = forms.IntegerField(label='5. -1 + 4 = ')
    answer_6 = forms.IntegerField(label='6. 10 - 8 = ')
    answer_7 = forms.IntegerField(label='7. 26 - 15 = ')
    answer_8 = forms.IntegerField(label='8. -18 - (-3) = ')
    answer_9 = forms.IntegerField(label='9. -4 + 6 = ')
    answer_10 = forms.IntegerField(label='10. 48 - (-7) = ')