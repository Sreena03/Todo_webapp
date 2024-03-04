from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from TodoApp.models import Task
from api.serializer import Task_serializer
from rest_framework import authentication,permissions


class Taskviewsetview(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializers = Task_serializer(qs,many=True)
        return Response(data=serializers.data)

    def create(self,request,*args,**kwargs):
        serializers=Task_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Task_serializer(qs)
        return Response(data=serializers.data)
    
    # check the user is already login or not,login cheytha user ano delete akunath nokan
    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response("Task deleted successfully")
        return Response("Login user doesn't match")
    
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Task_serializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)

    
    
    
    
    
    
    # # normal deletion

    # def destroy(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Task.objects.get(id=id).delete()
    #     return Response("Task deleted successfully")
    


    
    
