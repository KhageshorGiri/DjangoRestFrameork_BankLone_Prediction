from django.shortcuts import render
from bankapi.models import BankLone
from bankapi.serialiers import BankLoneSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bankapi import BnkMdl

# Create your views here.
class bankloneApi(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            ob = BankLone.objects.get(id=id)
            serializer = BankLoneSerializer(ob)
            return Response(serializer.data, status=status.HTTP_200_OK)
        ob = BankLone.objects.all()
        serializer = BankLoneSerializer(ob, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BankLoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ob = BankLone.objects.latest('id')
            approve = BnkMdl.predict_result(ob)
            if approve == 1:
                return Response({'mgs':"Lone Approved."}, status=status.HTTP_201_CREATED)
            else:
                return Response({'mgs':"Lone Approved."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)