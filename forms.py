from django import forms
from .models import Portfolio

class PortfolioPost(forms.Modelform):
    class Meta:
        model = Portfolio
        fields = ['title','image','description']