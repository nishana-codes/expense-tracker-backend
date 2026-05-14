from django.db import models
from django.contrib.auth.models import User

class ExpenseCategories(models.TextChoices):
    FOOD = "FOOD", "Food"
    TRAVEL = "TRAVEL", "Travel"
    BILLS = "BILLS", "Bills"
    SHOPPING = "SHOPPING", "Shopping"
    HEALTH = "HEALTH", "Health"
    OTHER = "OTHER", "Other"


class Expense(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=ExpenseCategories.choices)
    note = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.note