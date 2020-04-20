
from .models import CustomUser


def save_user(backend, user, response, *args, **kwargs):
    try:
        print('saving user')
        CustomUser.objects.get_or_create(user=user,username=user.username, meta_data={'login_source': backend.name})
        print(response)
    except Exception as e:
        print('Exception in saving user')
        print(e)
