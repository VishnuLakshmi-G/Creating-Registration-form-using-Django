from django.db import models
from django.contrib.auth.hashers import make_password  # For hashing the password

class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super(UserRegistration, self).save(*args, **kwargs)

    def _str_(self):
        return self.username  # Return username for better readability