from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	username = forms.CharField(max_length=512,required=True)

	class Meta:
		model = User
		fields = ("username", "first_name","last_name", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user