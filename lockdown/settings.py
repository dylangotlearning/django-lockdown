from django.conf import settings

URL_EXCEPTIONS = getattr(settings, 'LOCKDOWN_URL_EXCEPTIONS', ())
PASSWORDS = getattr(settings, 'LOCKDOWN_PASSWORDS', ())
FORM = getattr(settings, 'LOCKDOWN_FORM', 'lockdown.forms.LockdownForm')
SESSION_KEY = getattr(settings, 'LOCKDOWN_SESSION_KEY', 'lockdown-allow')
LOGOUT_KEY = getattr(settings, 'LOCKDOWN_LOGOUT_KEY', 'preview-logout')

if not isinstance(PASSWORDS, (tuple, list)):
    PASSWORDS = PASSWORDS and (PASSWORDS,) or ()
