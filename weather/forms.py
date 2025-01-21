from django import forms

class SearchForCoordinatesByZip(forms.Form):
    zip = forms.CharField(label="Zip", max_length=5, min_length=5)