from django import forms



class TestForm(forms.Form):
    pushups = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)


class WorkoutForm(forms.Form):
    set1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    set2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    set3 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    set4 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    set5 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)


