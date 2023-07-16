from django import forms
from django.core.exceptions import ValidationError

from book_app.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ('authors',)

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        }
    ))

    state = forms.ChoiceField(choices=Book.State.choices, widget=forms.Select(
        attrs={
            'class': 'custom-select',
            'placeholder': 'State'
        }
    ))

    # crispyforms ... librarie stilizari clase python
    def clean_title(self):
        if self.cleaned_data['title'].islower():
            raise ValidationError("Please enter capitalized title")
        return self.cleaned_data['title']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    first_name = forms.CharField(label="Author first name")
