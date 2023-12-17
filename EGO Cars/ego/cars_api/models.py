from django.db import models


TYPES = [
    ("Auto", "Auto"),
    ("Pickups y Comerciales", "Pickups y Comerciales"),
    ("SUVs y Crossovers", "SUVs y Crossovers"),
    ]
 # this can be modified to add new types of vehicles   


class Vehicle(models.Model):
    type = models.CharField(max_length=100, choices=TYPES)
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    tagline = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feature(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    primary_feature = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    

class Review(models.Model):

    #I asume the review is for a vehicle, if not this should be changed to fit the requirements

    vehicle = models.ForeignKey(Vehicle, related_name='reviews', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(null=True, blank=True)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Concessionaire(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class TestDrivePetition(models.Model):

    #I'm making a lot of assumptions on how the test drives are handeled, this should be changed to fit the requirements

    vehicle = models.ForeignKey(Vehicle, related_name='test_drive_petitions', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(null=True, blank=True)
    client_phone = models.CharField(max_length=100)
    requested_date = models.DateField(null=True, blank=True)
    requested_time = models.TimeField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    pricing_info = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    

class Accesory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField()
    def __str__(self):
        return self.name
   
    
class Activity(models.Model):

    #Asumo que las actividades tienen esta estructura.

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

#Imagino que 'contacto', 'innovacion', 'prensa', 'acerca de', 'toyota mobility service', etc.  son paginas estaticas o por fuera del scope de la api, por lo que no las incluyo en el modelo