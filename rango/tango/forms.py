from django import forms
from .models import Category , Page

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length = 225 , help_text='Category Title')
    views = forms.IntegerField(widget = forms.HiddenInput() , initial = 0)
    slug  = forms.SlugField(widget = forms.HiddenInput() , required = False)

    class Meta:
        model = Category
        fields = ('title',)


class PageForm(forms.ModelForm):
    title    = forms.CharField(max_length=225 , help_text='Page Title')
    views    = forms.IntegerField(widget= forms.HiddenInput(), initial = 0)
    content  = forms.CharField(widget=forms.Textarea())

    class Meta:
        model   = Page
        exclude = ('category', 'slug',)