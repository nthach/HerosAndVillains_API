# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mt+n-kn3re=ov2^pq43o5iaxtypu=wl_=%f$z=^*fxa%nbkt!+'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'herosandvillains_project',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}