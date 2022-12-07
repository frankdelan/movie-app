from django import forms


class AddForm(forms.Form):
    title = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': "form-field",
                                                                                    'placeholder': "Title"}))
