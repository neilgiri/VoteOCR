from django import forms

class GetImage(forms.Form):
    image = forms.ImageField()
class Voter(forms.Form):
    fname = forms.CharField(
        max_length=30,
    )
    mname = forms.CharField(
        max_length=30,
    )
    lname = forms.CharField(
        max_length=30,
    )
    dob = forms.CharField(

    )
    email = forms.EmailField(

    )
    adr1 = forms.CharField(
        max_length=100,
    )
    adr2 = forms.CharField(
        max_length=100,
        required=False,
    )
    city = forms.CharField(
        max_length = 50,
    )
    state = forms.CharField(
        max_length=12,
    )
    zip = forms.CharField(
        min_length=5,
        max_length=9,
    )
    numdl = forms.CharField(
        max_length=15,
    )
    citizen = forms.CharField(
        max_length=3,
    )
    langpref = forms.CharField(
        max_length=30,
    )
    ppp = forms.CharField(
        max_length=30,
    )
