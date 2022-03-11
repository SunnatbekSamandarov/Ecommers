from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2',]
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for key,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.PasswordInput) or \
                    isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({'placeholder':field.label})

    def save(self, commit=True):
        user = super(UserForm,self).save(commit=False)
        if commit:
            user.save()
        return user