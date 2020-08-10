from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self,*args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith('.ru'):
            raise forms.ValidationError("This is bad email!")
        return email
