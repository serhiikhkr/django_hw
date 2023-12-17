from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, ModelChoiceField, Select, \
    ModelMultipleChoiceField, SelectMultiple

from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": 'fulnameid'}))
    born_date = DateField(
        widget=DateInput(attrs={"class": "form-control", "id": 'borndateid', 'type': 'date'}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control", "id": 'bornlocation'}))
    description = CharField(widget=TextInput(attrs={"class": "form-control", "id": 'descriptionauthorid'}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": 'qouteid'}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))
    author = ModelChoiceField(queryset=Author.objects.all(),
                              widget=Select(attrs={"class": "form-select", "id": "authorselectid"}))

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']

    def clean_quote(self):
        quote = self.cleaned_data['quote']
        quoted_text = f'"{quote}"'
        return quoted_text