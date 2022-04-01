from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where nickname is the unique identifiers for authentication.
    """

    def create_user(self, nickname, email, password, **extra_fields):
        """
        Create and save a User with the given nickname and password.
        """

        if not nickname:
            raise ValueError('The nickname must be set')
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(nickname = nickname, email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nickname, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given nickname and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        return self.create_user(nickname, email, password, **extra_fields)

    def get_by_natural_key(self, nickname):
        """
        Retrieves a user instance using the contents of the field nominated by USERNAME_FIELD.
        """
        
        return self.get(nickname = nickname)