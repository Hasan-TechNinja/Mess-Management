from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.TextField()
    role = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    status = models.CharField(max_length=50)
    join_date = models.DateTimeField()
    photo_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='Manager-Image')

    def __str__(self):
        return str(self.id)
    
class MonthlyReport(models.Model):
    date = models.DateField()
    totalIncome = models.IntegerField() 
    totalCost = models.IntegerField()
    mealRate = models.IntegerField()
    totalBorders = models.IntegerField()
    
    def __str__(self):
        return str(self.id) 

class Meal(models.Model):
    user_id = models.IntegerField()
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateTimeField()
    period = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50) #id, title, description
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
    
class Cost(models.Model):
    type = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class TransactionType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return str(self.id)
    
class MealType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
class User_status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
class User_roll(models.Model):
    roll = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
class Period(models.Model):
    period = models.CharField(max_length= 50)

    def __str__(self):
        return str(self.id)
    
