from django import forms

from .models import Item #importing DB items

INPUT_CLASS='w-full py-2 px-2 rounded-l border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','image','descrip','price')

        widgets={
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'descrip': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','image','descrip','price','is_sold')

        widgets={
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'descrip': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
        }