from django import forms
from Nutritionapp.models import TrackerData,FoodData

class FoodForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=FoodData.objects.all(),  
        empty_label="Select Food Item",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model  = TrackerData
        fields = ['name', 'quantity']