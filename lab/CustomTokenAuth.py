"""Custom Token Authentication."""
from django.contrib.auth import mixins
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Taken from https://gist.github.com/jsmedmar/d846eee063fa23148f8a87313dd590a3
# and modified to suit my Token Authentication needs.

class TokenLoginRequiredMixin(mixins.LoginRequiredMixin):

    """A login required mixin that allows token authentication."""

    def dispatch(self, request, *args, **kwargs):
        """If token was provided, ignore authenticated status."""
        http_auth = request.META.get("HTTP_AUTHORIZATION")
        token_key = http_auth.split()[1]
        if http_auth and "Token" in http_auth:
            try:  # check if token matches an already existing user.
                token_obj = Token.objects.get(key=token_key)
                if(token_obj):
                    request.user = User.objects.get(auth_token=token_key)
            except:
                return self.handle_no_permission()

        elif not request.user.is_authenticated:
            return self.handle_no_permission()

        return super(mixins.LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)
