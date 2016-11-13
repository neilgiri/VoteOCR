from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Voter, GetImage
from PIL import *
from .register import main
#from .file import crawler

readValues = {}
def Thanks(request):
    return render(request, 'OCR/Thanks.html')
def VoterForm(request):
    if request.method == 'POST':
        f = Voter(request.POST)
        if f.is_valid():
            d = {}
            d['fName'] = f.cleaned_data['fname']
            d['mName'] = f.cleaned_data['mname']
            d['lName'] = f.cleaned_data['lname']
            d['DOB'] = f.cleaned_data['dob']
            d['SEX'] = f.cleaned_data['sex']
            d['aStreet'] = f.cleaned_data['adr1']
            d['aStreet2'] = f.cleaned_data['adr2']
            d['aCity'] = f.cleaned_data['city']
            d['aState'] = f.cleaned_data['state']
            d['aZip'] = f.cleaned_data['zip']
            d['numDL'] = f.cleaned_data['numdl']
            d['citizen'] = f.cleaned_data['citizen']
            d['email'] = f.cleaned_data['email']
            d['lang'] = f.cleaned_data['langpref']
            #d['county'] = getCounty()
            d['ppp'] = f.cleaned_data['ppp']
            #Script(d)
            return HttpResponseRedirect('/Thanks/')
    else:
        f = Voter(initial=readValues, label_suffix='')
    f.fields['fname'].label = "First Name"
    f.fields['mname'].label = "Middle Name (Optional)"
    f.fields['lname'].label = "Last Name"
    f.fields['dob'].label = "Date of Birth (DD/MM/YYYY)"
    f.fields['adr1'].label = "Address Line 1"
    f.fields['adr2'].label = "Address Line 2"
    f.fields['numdl'].label = "Drivers License Number"
    f.fields['numdl'].lab = "Are you a U.S. citizen?"
    f.fields['langpref'].label = "Language Preference"
    f.fields['ppp'].label = "Political Party Preference"
    return render(request, 'OCR/VoterForm.html', {'form' : f})

def ImageSubmit(request):
    global readValues
    if request.method == "POST":
        f = GetImage(request.POST, request.FILES)
        if f.is_valid():
            print(request.FILES['image'])
            out = main(request.FILES['image'])
            readValues = {'fname': out['fName'], 'mname': out['mName'], 'lname': out['lName'], 'dob': out['DOB'], 'sex': out['SEX'], 'adr1': out['aStreet'], 'city': out['aCity'], 'state': out['aState'], 'zip': out['aZip'], 'numdl': out['numDL']}
            return HttpResponseRedirect('/VoterForm/')
    else:
        f = GetImage(label_suffix='')
    return render(request, 'OCR/Main.html', {'form': f})
