from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.permissions import IsAuthenticated

from .serializer import ExpenseCreateSerializer, ExpenseListSerializer, ExpenseDeleteSerializer
from .models import Expense
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

def home_ui(request):
    return render(request, "expenses/home_ui.html")

class ExpenseCreateAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExpenseCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expense = Expense(
            user=request.user,
            note=serializer.validated_data["note"],
            category=serializer.validated_data["category"],
            amount=serializer.validated_data["amount"],
        )
        expense.full_clean()
        expense.save()
        return Response("Expense Saved Successfully", status=HTTP_201_CREATED)


class ExpenseListAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user).order_by("-created_date")
        serializer = ExpenseListSerializer(expenses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class ExpenseDeleteAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExpenseDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        expense = Expense.objects.get(id=serializer.validated_data["id"])
        expense.delete()
        return Response("Expense Deleted Successfully", status=HTTP_201_CREATED)


class ExpenseAiOverviewAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        data = list(expenses.values("category", "amount", "created_date", "note"))
        prompt = f"""
            Analyse this expense data and give a short summary and advice

            {data}

            keep it simple and user friendly.
        """
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return Response(response.text, status=HTTP_200_OK)