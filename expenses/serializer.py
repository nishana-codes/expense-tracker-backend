from rest_framework import serializers


class ExpenseCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    note = serializers.CharField()
    category = serializers.CharField()


class ExpenseListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.FloatField()
    note = serializers.CharField()
    category = serializers.CharField()
    created_date = serializers.DateTimeField()


class ExpenseDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()