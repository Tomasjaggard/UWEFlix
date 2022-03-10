from django import forms
from UWFX.models import Film, Showing
from UWFX.models import Screen
from django.contrib.admin.widgets import AdminTimeWidget

class addFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"

class deleteFilmForm(forms.Form):
    delete_film = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=Film.objects.all(),
        initial=0
        )

class addScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = "__all__"

class addShowingForm(forms.ModelForm):
    class Meta:
        model = Showing
        fields = "__all__"
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'time': forms.TimeInput(format=('%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a time', 'type':'time'}),
        }