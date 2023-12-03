from .models import Reservoirs, TextFile
from django.forms import ModelForm, TextInput, Select

class ReservoirsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
    class Meta:
        model = Reservoirs
        fields = ["title", "category"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название",
                'type': 'text',
            }),
            "category": Select(attrs={
                'class': 'form-select',
                'placeholder': 'Категория'
            }),
        }

class TextFileForm(ModelForm):

    class Meta:
        model = TextFile
        fields = ["file", "reservoir"]
        widgets = {
            "file": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название",
                'type': 'file',
                "accept": ".txt",
                "required": True,
            }),
            "reservoir": Select(attrs={
                'class': 'form-select',
                "required": True,
            }),
        }