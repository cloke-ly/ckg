from django import forms

from User.models import User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname','sex','birthday','location']

class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = '__all__'

    def clean_max_dating_age(self):
        '''检查最大交友年龄'''
        cleaned = super().clean()
        max_dating_age = cleaned['max_dating_age']
        min_dating_age = cleaned['min_dating_age']
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age > max_dating_age')
        else:
            return max_dating_age

    def clean_max_dating_distance(self):
        '''检查最大交友距离'''
        cleaned = super().clean()
        max_dating_distance = cleaned['max_dating_distance']
        min_dating_distance = cleaned['min_dating_distance']
        if min_dating_distance > max_dating_distance:
            raise forms.ValidationError('min_dating_distance > max_dating_distance')
        else:
            return max_dating_distance