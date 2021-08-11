from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Extends the UserCreationForm amd specify swapping in our 
    CustomUser model and displaying the field email and username.
    """

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    """
    Extends the UserChangeForm and specify swapping in our CustomUser
    model and dispalying email and username.
    """

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

