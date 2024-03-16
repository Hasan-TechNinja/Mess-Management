from django.contrib import admin

# Register your models here.
from . models import(
    User_status,
    MealType,
    MonthlyReport,
    Meal,
    Income,
    Cost,
    TransactionType,
    User_roll,
    Period,
    User,
)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name', 'phone', 'role', 'division', 'address', 'status', 'join_date', 'photo_name', 'photo']

@admin.register(MonthlyReport)
class MonthlyReportModelAdmin(admin.ModelAdmin):
    list_display=['id', 'date', 'totalIncome', 'totalCost', 'mealRate', 'totalBorders']

@admin.register(Meal)
class MealModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user_id', 'status', 'amount', 'date', 'period']

@admin.register(Income)
class IncomeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'type', 'amount', 'date']

@admin.register(Cost)
class CostModelAdmin(admin.ModelAdmin):
    list_display=['id', 'type', 'amount', 'date']

@admin.register(TransactionType)
class TransactionTypeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description']

@admin.register(MealType)
class MealTypeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

@admin.register(User_status)
class User_statusModelAdmin(admin.ModelAdmin):
    list_display=['id', 'status']

@admin.register(User_roll)
class User_rollModelAdmin(admin.ModelAdmin):
    list_display=['id', 'roll']

@admin.register(Period)
class PeriodModelAdmin(admin.ModelAdmin):
    list_display=['id', 'period']