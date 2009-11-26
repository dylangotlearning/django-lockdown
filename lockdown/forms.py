from django import forms

from lockdown import settings


class BaseLockdownForm(forms.Form):
    def generate_token(self):
        """
        Generate a token which can be used to authenticate the user for future
        requests.
        
        """
        return True

    def authenticate(self, token_value):
        """
        Authenticate the user from a stored token value. If the ``token_value``
        is ``None``, then no token was retrieved.
         
        """
        return token_value is True


class LockdownForm(BaseLockdownForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def clean_password(self):
        """
        Check that the password appears the LOCKDOWN_PASSWORDS setting.
        
        """
        value = self.cleaned_data.get('password')
        if not value in settings.PASSWORDS:
            raise forms.ValidationError('Incorrect password.')
        return value

    def generate_token(self):
        """
        Save the password as the authentication token.
        
        It's acceptable to store the password raw, as it is stored server-side
        in the user's session.
        
        """
        return self.cleaned_data['password']

    def authenticate(self, token_value):
        """
        Check that the password is still in the LOCKDOWN_PASSWORDS setting.
        
        This allows for revoking of a user's preview rights by changing the
        passwords.
        
        """
        return token_value in settings.PASSWORDS
