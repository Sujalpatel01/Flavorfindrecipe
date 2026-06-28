from django.db import models

# Create your models here.
from django.db import models


class Role(models.Model):
    user_typename = models.CharField(max_length=20)

    def __str__(self):
        return self.user_typename


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class UserDetail(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    u_name = models.CharField(max_length=100)
    u_dp = models.ImageField(upload_to='users/')
    u_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    u_email = models.EmailField()
    u_phone = models.CharField(max_length=15)

    u_type = models.ForeignKey(Role, on_delete=models.CASCADE)

    u_status = models.BooleanField(default=True)

    def __str__(self):
        return self.u_name


class UserAddress(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    building_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return self.building_name


class GadgetCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_picture = models.ImageField(upload_to='gadgets/')
    cat_description = models.TextField()

    category_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name


class FeedbackDetails(models.Model):
    f_title = models.CharField(max_length=100)
    f_description = models.TextField()

    f_by = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    f_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_title


class ComplaintDetails(models.Model):
    c_name = models.CharField(max_length=100)
    c_detail = models.TextField()

    c_photo = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )

    c_by = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    c_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.c_name
    
    