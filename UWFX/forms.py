from django import forms
from UWFX.models import Film

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