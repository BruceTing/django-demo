from django import forms
from demoapp.validators import validate_email, validate_even


class CommentForm(forms.Form):
    BIRTH_YEAR_CHOICES = ('1980','1981','1982')
    FAVORITE_COLORS_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    )
    SEX_CHOICES = (
        (1, 'man'),
        (2, 'woman'),
    )
    email = forms.EmailField(label='email',
            validators=[validate_email],
            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'abc@example.com'}))
    password = forms.CharField(label='password', required=False,
            widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='message',
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    birth_year = forms.DateField(label='year',
            widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(label='favoriteColors',
            widget=forms.CheckboxSelectMultiple,
            choices=FAVORITE_COLORS_CHOICES)
    best_colors = forms.ChoiceField(label='best_colors',
            widget=forms.RadioSelect,
            choices=FAVORITE_COLORS_CHOICES)
    select_colors = forms.ChoiceField(label='select_colors',
            widget=forms.Select(attrs={'class': 'form-control'}),
            choices=FAVORITE_COLORS_CHOICES)
    even_field = forms.IntegerField(label='even',
            widget=forms.NumberInput(attrs={'class': 'form-control'}),
            validators=[validate_even])


class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])

