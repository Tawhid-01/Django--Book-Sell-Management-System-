from django import forms
from .models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['full_name', 'occupation', 'address', 'image']

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['book_name', 'total_pages']

class SellBookForm(forms.ModelForm):
    class Meta:
        model = SellBookModel
        fields = '__all__'
        exclude = ['sell_by', 'total']