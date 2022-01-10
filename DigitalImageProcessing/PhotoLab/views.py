from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import CommentSerializer
from .tests import Comment
import numpy as np
from PIL import Image
from .newtest import image_recognition
from django.http import HttpResponse, JsonResponse
from .models import User
from .models import Client
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import ClientSerializer
from deepface import DeepFace


@api_view(['GET','POST'])
def comment_view(request):
    # c = Client.objects.get(id = 1)
    # p = c.image
    # img = Image.open(p)
    # array = np.array(img)
    # print(array)
    # print(image_recognition(array))
    message_obj = Comment("abc","def","laptop.jpg")
    serializer_class = CommentSerializer(message_obj)
    return Response(serializer_class.data)

@api_view(['GET','POST'])
def users(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        # username = request.POST["username"]
        # email = request.POST["email"]
        # password = request.POST["password"]
        user = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid():
            # user_serializer.save()
            print(user_serializer.data)
            return JsonResponse({'status':'TRUE'}, safe=False)
        return JsonResponse({'status': 'FAIL'}, safe=False)


    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET','POST'])
def clients(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        c = request.FILES["image"]
        data = json.loads(request.data['data'])
        print(c)
        return JsonResponse({'status': 'TRUE '}, safe=False)
        # client = JSONParser().parse(request)
        # print(11111111111111111111111111111111111111111111111)
        # print(client)
        # client_serializer = ClientSerializer(data=client)
        # if client_serializer.is_valid():
        #     # user_serializer.save()
        #     print(client_serializer.data)
        #     return JsonResponse({'status':'TRUE '}, safe=False)
        # return JsonResponse({'status': 'FAIL'}, safe=False)