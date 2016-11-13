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
    sex = forms.CharField(
        max_length=6,
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
    YN = (
        ('true', "Yes"),
        ('false', "No")
    )
    citizen = forms.ChoiceField(
        choices = YN,
    )
    ssn = forms.CharField(
        max_length=4,
    )
    bbm = forms.ChoiceField(
        choices = YN,
    )
    LANG = (
        ('english', 'English'),
        ('chinese', 'Chinese'),
        ('hindi', 'Hindi'),
        ('janapese', 'Japanese'),
        ('khmer', 'Khmer'),
        ('korean', 'Korean'),
        ('spanish', 'Spanish'),
        ('tagalog', 'Tagalog'),
        ('thai', 'Thai'),
        ('vietnamese', 'Vietnamese'),
    )
    langpref = forms.ChoiceField(
        choices=LANG
    )
    PARTIES = (
        ('AmericanIn02', 'American Independent'),
        ('Democratic04', 'Democratic'),
        ('Green05', 'Green'),
        ('Libertarian06', 'Libertarian'),
        ('PeaceandFr07', 'Peace and Freedom'),
        ('Republican08', 'Republican'),
    )
    ppp = forms.ChoiceField(
        choices=PARTIES,
    )
