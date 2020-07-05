from youngun.apps.authentication.models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'password1', 'password2',
#                   'is_active', 'is_superuser')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     password = forms.CharField(
#         label='Password (only edit if you want to change)', widget=forms.PasswordInput, required=False)

#     class Meta:
#         model = User
#         fields = ('email', 'password',
#                   'is_active', 'is_staff', 'is_superuser', 'groups')

#     def clean_password(self):
#         print(self.initial)
#         return self.cleaned_data.get("password")

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         if not self.cleaned_data["password"] == "":
#             user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


class StaffUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',
                  'is_active', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user


class StaffUserChangeForm(forms.ModelForm):
    password = forms.CharField(
        label='Password (only edit if you want to change)', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_staff', 'is_superuser', 'groups')

    def clean_password(self):
        print(self.initial)
        return self.cleaned_data.get("password")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if not self.cleaned_data["password"] == "":
            user.set_password(self.cleaned_data["password"])
            user.is_staff = True
        if commit:
            user.save()
        return user


class ClientUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',
                  'is_active', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        if commit:
            user.save()
        return user


class ClientUserChangeForm(forms.ModelForm):
    password = forms.CharField(
        label='Password (only edit if you want to change)', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_staff', 'is_superuser', 'groups')

    def clean_password(self):
        print(self.initial)
        return self.cleaned_data.get("password")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        if not self.cleaned_data["password"] == "":
            user.set_password(self.cleaned_data["password"])
            user.is_staff = False
        if commit:
            user.save()
        return user
