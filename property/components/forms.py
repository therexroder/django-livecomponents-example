from django import forms
from django.forms import ModelForm

from property.models import Property


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ["title", "price", "city"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm text-slate-900 shadow-sm transition focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50",
                    "placeholder": "Enter title",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm text-slate-900 shadow-sm transition focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50",
                    "placeholder": "Enter price",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "w-full rounded-xl border border-slate-200 bg-white px-4 py-2 text-sm text-slate-900 shadow-sm transition focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50",
                    "placeholder": "Enter city",
                }
            ),
        }
