from django import forms
from .models import PortfolioItem

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['asset', 'quantity']
        widgets = {
            'asset': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Asset
        self.fields['asset'].queryset = Asset.objects.all()
        self.fields['asset'].label_from_instance = lambda obj: f"{obj.name} ({obj.symbol})"
