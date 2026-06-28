from django.db import models

# PART A

class Role(models.Model):
    user_typename = models.CharField(max_length=20)

    def __str__(self):
        return self.user_typename


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class UserDetail(models.Model):
    u_name = models.CharField(max_length=100)
    u_dp = models.ImageField(upload_to='users/')
    u_gender = models.CharField(max_length=20)
    u_email = models.EmailField()
    u_phone = models.CharField(max_length=15)

    u_type = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )

    u_status = models.BooleanField(default=True)

    def __str__(self):
        return self.u_name


class UserAddress(models.Model):
    user = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    building_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )

    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return self.building_name


class FurnitureCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_picture = models.ImageField(upload_to='category/')
    cat_description = models.TextField()

    category_added = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.cat_name


class FeedbackDetails(models.Model):
    f_title = models.CharField(max_length=100)
    f_description = models.TextField()

    f_by = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    f_on = models.DateTimeField(
        auto_now_add=True
    )

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

    c_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.c_name


# PART B

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_description = models.TextField()

    brand_logo = models.ImageField(
        upload_to='brands/'
    )

    def __str__(self):
        return self.brand_name


class NewFurniture(models.Model):
    model_name = models.CharField(max_length=100)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='new_furniture/'
    )

    furniture_type = models.ForeignKey(
        FurnitureCategory,
        on_delete=models.CASCADE
    )

    available_quantity = models.IntegerField()

    def __str__(self):
        return self.model_name


class OldFurniture(models.Model):
    old_furniture_name = models.CharField(max_length=100)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='old_furniture/'
    )

    furniture_type = models.ForeignKey(
        FurnitureCategory,
        on_delete=models.CASCADE
    )

    available_quantity = models.IntegerField()

    def __str__(self):
        return self.old_furniture_name


class RentFurniture(models.Model):
    rent_furniture_name = models.CharField(max_length=100)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='rent_furniture/'
    )

    furniture_type = models.ForeignKey(
        FurnitureCategory,
        on_delete=models.CASCADE
    )

    available_quantity = models.IntegerField()

    def __str__(self):
        return self.rent_furniture_name


class NewFurnitureBuying(models.Model):
    furniture = models.ForeignKey(
        NewFurniture,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    booking_datetime = models.DateTimeField(
        auto_now_add=True
    )


class OldFurnitureBuying(models.Model):
    old_furniture = models.ForeignKey(
        OldFurniture,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    booking_datetime = models.DateTimeField(
        auto_now_add=True
    )


class RentFurnitureOrder(models.Model):
    rent_furniture = models.ForeignKey(
        RentFurniture,
        on_delete=models.CASCADE
    )

    rent_user = models.ForeignKey(
        UserDetail,
        on_delete=models.CASCADE
    )

    rent_startdate = models.DateField()
    rent_enddate = models.DateField()

    rent_bookdatetime = models.DateTimeField(
        auto_now_add=True
    )