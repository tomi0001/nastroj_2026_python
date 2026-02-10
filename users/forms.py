from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    start_day = forms.IntegerField(label="Dzień startu")

    def save(self, request):
        user = super().save(request)

        # from .models import User
        # User, created = User.objects.get_or_create(user=user)
        user.start_day = self.cleaned_data["start_day"]
        user.save()

        return user