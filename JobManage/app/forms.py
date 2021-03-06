from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
  class Meta: 
    model = Item
    fields = ('name', 'age', 'sex', 'memo')
    widgets = {
      'name': forms.TextInput(attrs={'placeholder': '名前を入力してください'}),
      'age': forms.NumberInput(attrs={'min':1}),
      'sex': forms.RadioSelect(),
      'memo': forms.Textarea(attrs={'rows':4}),
    }