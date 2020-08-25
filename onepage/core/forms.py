from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))
    
class ContactForm2(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)