from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, ModelChoiceField, Select

from .models import Author, Quote


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
    tags = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "tagsid"}))
    author = ModelChoiceField(queryset=Author.objects.all().values_list('fullname',flat=True),
                              widget=Select(attrs={"class": "form-select", "id": "authorselectid"}))

    class Meta:
        model = Quote
        fields = ['author', 'tags', 'author']
