from django import forms


PRODUCET_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddPlanet(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCET_QUANTITY_CHOICES,
                                      coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    