from django.db import models


from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    )

STATUS_CHOICES = [(1, 'Activo'), (0, 'Inactivo')]


class UserManager(BaseUserManager):

    """
    Método para crear un usuario
    model es el modelo de la clase Users
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    """
    Método para crear un superusuario
    """
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
class Users(AbstractBaseUser):
    """
    Modelo para la tabla de usuarios, se hereda de la clase AbstractBaseUser para poder usar sus métodos
    objects es el objeto UserManager para poder usar los métodos de la clase UserManager
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True) 
    last_name = models.CharField(max_length=100, blank=True, null=True) 
    email = models.EmailField(unique = True) 
    is_superuser = models.BooleanField(default=False) 
    status = models.BooleanField(default=1, choices=STATUS_CHOICES, blank=True, null=True) 
    image = models.ImageField(default='default.png', blank=True, null=True)
    identification = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email' 
    
    class Meta:
        db_table = 'users_users'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'