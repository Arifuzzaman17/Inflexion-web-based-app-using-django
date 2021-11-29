from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Images


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


# class ImageCreation(forms.ModelForm):
# 	class Meta:
# 		model = Images
# 		fields = ("title", 'image')
#
# 	def save(self, commit=True):
# 		image = self.cleaned_data['image']
# 		image_details = super(ImageCreation, self).save(commit=False)
# 		if commit:
# 			image_details.save()
#
# 		return image_details

class LoginForm(AuthenticationForm):

	class Meta:
		model = User
		fields = ("email", "password1")

