from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'age', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age