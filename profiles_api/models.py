"""
Classe dos models

UserProfileManager --> herda da BaseUserManager:

    * Gerenciador do db UserProfile;
    * Cria usuários e superusuários;
    * O parâmetro using na função save indica em qual db serão salvos os dados;
    Exemplo:
    settings.py:
    DATABASES = {
        'default': {
            'NAME': 'app_data',
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'postgres_user',
            'PASSWORD': '****'
        },
        'new_users': {
            'NAME': 'user_data',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'mysql_user',
            'PASSWORD': '****'
        }
    }
    Caso eu queira salvar os dados no db default, uso self._db como parâmetro;
    Caso eu queira salvar os dados no db new_user, uso self.new_users como parâmetro;


UserProfile --> herda de AbstractBaseUser, PermissionsMixin:

    * Modelo do db para os usuários;
    * Campos:
        * Name: Nome do usuário, não é único
        * Email: Email do usuário, é único e também será utilizado como username;
        * is_active: Determina se o perfil do usuário é ativado, ou seja, pode efetuar algumas tarefas;
        * is_staff: Determina se o perfil do usuário pode acessar o django_admins

    * objects: Específica o gerenciador de usuários para o modelo, pelo fato do model
    ser customizado, é necessário criar também um gerenciador customizado

    * USERNAME: Define qual campo será utilizado como Username;
    * REQUIRED_FIELDS: ['name']

    * função get_full_name --> retornar o nome completo, no caso do nosso model ele só tem um campo nome,
    então a função retornará apenas o nome;
    * função get_short_name --> retornar o primeiro nome, no caso do nosso model, ele só tem um campo nome,
    então a função retornará apenas o nome;
    * função __str__ --> retornar as representação string do nosso modelo, esse será o valor retornado quando
    convertemos o perfil criado em uma string

    OBS: O modelo deve ser configurado como default nos settings.py criando uma constante:

        AUTH_USER_MODEL = 'profiles_api.UserProfile'
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
