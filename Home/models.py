from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROLE_CHOICES = (
    ('Manageer', 'Manager'),
    ('Border', 'Border')
)
STATUS_CHOICES = (
    ('On', 'On'),
    ('Off', 'Off')
)
DIVISION_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Rangpur', 'Rangpur'),
    ('Rahshahi', 'Rajshahi'),
    ('Khulna', 'Khulna'),
    ('Barishal', 'Barishal'),
    ('Chattogram', 'Chattogram'),
    ('Mymensingh', 'Mymensingh'),
    ('Sylhet', 'Sylhet')
)
class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    address = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    join_date = models.DateField()
    photo = models.ImageField(upload_to='Manager-Image')

    def __str__(self):
        return str(self.id)
    
class Border(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    address = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    join_date = models.DateField()
    photo = models.ImageField(upload_to='Border-Image') 
    
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
    

PERIOD_CHOICES = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner')
)
class Meal(models.Model):
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    amount = models.IntegerField()
    date = models.DateField()
    period = models.CharField(choices=PERIOD_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)
    
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
    
class Cost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class TransactionType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return str(self.id)