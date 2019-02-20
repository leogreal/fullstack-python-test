from store.authentication.models import Profile


class AuthBackend(object):

    def authenticate(self, username=None, password=None, **kwargs):

        user = Profile.objects.get(username=username)
        if user.check_password(password):
            return user

        return None

    def get_user(self):
        try:
            return Profile.objects.get(username=username)
        except:
            return None
