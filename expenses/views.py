from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.permissions import IsAuthenticated

from .serializer import ExpenseCreateSerializer, ExpenseListSerializer, ExpenseDeleteSerializer
from .models import Expense
from dotenv import load_dotenv
from django.conf import settings
import os
import google.generativeai as genai

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

        data = list(
            expenses.values(
                "category",
                "amount",
                "created_date",
                "note"
            )
        )

        prompt = f"""
        Analyse this expense data and give a short summary and advice.

        Expense Data:
        {data}

        Keep it simple and user friendly.
        """

        try:

            genai.configure(api_key=settings.GEMINI_API_KEY)

            model = genai.GenerativeModel("gemini-pro")

            response = model.generate_content(prompt)

            return Response(
                {"message": response.text},
                status=HTTP_200_OK
            )

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=500
            )