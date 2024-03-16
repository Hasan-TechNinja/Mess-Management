from django.contrib import admin

# Register your models here.
from . models import(
    Manager,
    Border,
    MonthlyReport,
    Meal,
    Income,
    Cost,
    TransactionType,
)

@admin.register(Manager)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name', 'phone', 'role', 'division', 'address', 'status', 'join_date', 'photo']

@admin.register(Border)
class BorderModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name', 'phone', 'role', 'division', 'address', 'status', 'join_date', 'photo']

@admin.register(MonthlyReport)
class MonthlyReportModelAdmin(admin.ModelAdmin):
    list_display=['id', 'date', 'totalIncome', 'mealRate', 'totalBorders']

@admin.register(Meal)
class MealModelAdmin(admin.ModelAdmin):
    list_display=['id', 'status', 'amount', 'date', 'period']

@admin.register(Income)
class IncomeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'type', 'amount', 'date']

@admin.register(Cost)
class CostModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'type', 'amount', 'date']

@admin.register(TransactionType)
class TransactionTypeModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description']