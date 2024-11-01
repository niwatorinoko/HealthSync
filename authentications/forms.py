from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'}
    ))

    email = forms.EmailField(label='Email Address', widget=forms.TextInput(
        attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'}
    ))

    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'}))
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'}))

    # Health survey fields
    age_range = forms.ChoiceField(
        choices=[('', 'Select your age range'), ('Under 18', 'Under 18'), ('18-25', '18-25'), ('26-35', '26-35'), 
                 ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65'), ('Over 65', 'Over 65')],
        required=True,
        label='Age Range',
        widget=forms.Select(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'})
    )
    health_condition = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=forms.RadioSelect(attrs={'style': 'margin-right: 10px;'}),
        required=True,
        label='Health Conditions'
    )
    specify_condition = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 300px;', 'placeholder': 'If yes, please specify'})
    )
    dietary_preferences = forms.ChoiceField(
        choices=[('', 'Select dietary preferences'), ('normal', 'Normal'), ('vegetarian', 'Vegetarian')],
        required=True,
        label='Dietary Preferences',
        widget=forms.Select(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'})
    )
    food_allergies = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=forms.RadioSelect(attrs={'style': 'display: flex; margin-left: 10px; align-items: center; justify-content: flex-start;'}),
        required=True,
        label='Food allergies'
    )
    specify_allergies = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 300px;', 'placeholder': 'If yes, please specify'})
    )
    fitness_level = forms.ChoiceField(
        choices=[('', 'Select fitness level'), ('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')],
        required=True,
        label='Fitness Level',
        widget=forms.Select(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'})
    )
    preferred_sports = forms.ChoiceField(
        choices=[('', 'Select sports preference'), ('gym', 'Gym'), ('running', 'Running'), ('swimming', 'Swimming'), ('yoga', 'Yoga')],
        required=True,
        label='Preferred Sports or Activities',
        widget=forms.Select(attrs={'style': 'margin-bottom: 30px; margin-left: 10px; width: 93%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'})
    )

    consent = forms.BooleanField(
        required=True, 
        widget=forms.CheckboxInput(attrs={'style': 'margin-right: 10px; margin-left: 40px;'})
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password does not match')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)  # パスワードをハッシュ化して設定

        # Save health survey fields to the user
        user.age_range = self.cleaned_data.get('age_range')
        user.health_condition = self.cleaned_data.get('health_condition')
        user.specify_condition = self.cleaned_data.get('specify_condition')
        user.dietary_preferences = self.cleaned_data.get('dietary_preferences')
        user.food_allergies = self.cleaned_data.get('food_allergies')
        user.specify_allergies = self.cleaned_data.get('specify_allergies')
        user.fitness_level = self.cleaned_data.get('fitness_level')
        user.preferred_sports = self.cleaned_data.get('preferred_sports')

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser', 'is_active')

    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='E-mail address', widget=forms.TextInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'E-mail address'
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'input mb-4',
            'placeholder': 'Password'
        }
    ))