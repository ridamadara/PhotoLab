from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import cv2
from rest_framework.response import Response
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_protect
import base64
from django.http import HttpResponse
from .serializers import CommentSerializer, ResizeSerializer
from .tests import Comment, ImageResizer
import numpy as np
from PIL import Image
from .newtest import image_recognition
from django.http import HttpResponse, JsonResponse
from .models import User
from .models import Client, ImageEditting
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import ClientSerializer
from deepface import DeepFace


@csrf_protect
def img_resize(request):
    if request.method == 'POST' and request.FILES['img']:
    # if request.POST.get('img'):
        image = request.FILES['img']
        print(image)
        width = int(request.POST['width'])
        height = int(request.POST['height'])
        img = Image.open(image)
        array = np.array(img)
        print("This is an array")
        print(array)
        print('Original Dimensions : ', array.shape)
        resized = cv2.resize(array, (width, height), interpolation=cv2.INTER_AREA)
        print('Resized Dimensions : ', resized.shape)
        edited_image = Image.fromarray(resized, 'RGB')
        #         resized_image.save('gfg_dummy_pic.png')
        edited_image.save("F:/Images/Resized Images" + '/' + str(image) )
        return render(request, "newImageResize.html")
    else:
        return render(request, "newImageResize.html")


@api_view(['GET', 'POST'])
def comment_view(request):
    # c = Client.objects.get(id = 1)
    # p = c.image
    # img = Image.open(p)
    # array = np.array(img)
    # print(array)
    # print(image_recognition(array))
    message_obj = Comment("abc", "def", "../media/pics/hamdan.jpeg")
    serializer_class = CommentSerializer(message_obj)
    return Response(serializer_class.data)


@api_view(['GET', 'POST'])
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
            return JsonResponse({'status': 'TRUE'}, safe=False)
        return JsonResponse({'status': 'FAIL'}, safe=False)

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
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
        # data = json.loads(request.data['data'])
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

# @api_view(['POSt'])
# def image_resize(request):
#     if request.method == 'POST':
#         p = request.FILES["image"]
#
#         img = Image.open(p)
#         array = np.array(img)
#         print("This is an array")
#         print(array)
#
#         print('Original Dimensions : ', array.shape)
#         # cv2.imshow("orignal image", array)
#         resized = cv2.resize(array, (100, 50), interpolation=cv2.INTER_AREA)
#         print('Resized Dimensions : ', resized.shape)
#         resized_image = Image.fromarray(resized, 'RGB')
#         resized_image.save('gfg_dummy_pic.png')
#         # client = Client(name = 'test',contact = '090',image = resized_image, doc = '2022-01-02' )
#         # client.save()
#         # u = Client
#         # u.save()
#         k = ImageEditting(img = "gfg_dummy_pic.png")
#         k.save()
#         return JsonResponse({'status': 'PASS'}, safe=False)
#         # message_obj = Comment("abc", "def", resized_image)
#         # # resized_image.save('gfg_dummy_pic.png')
#         # serializer_class = CommentSerializer(message_obj)
#         # return Response(serializer_class.data)
#         # cv2.imshow("Resized image", resized)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#         # return JsonResponse({'status': 'PASS','img':resized}, safe=False)


@csrf_protect
def gray_scale(request):
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        print(image)
        img = Image.open(image)
        array = np.array(img)

        ret, frame_buff = cv2.imencode('.jpg', array)  # could be png, update html as well
        frame_b64 = base64.b64encode(frame_buff)


        # gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        # cv2.imwrite("F:/Images/Grayscale Images" + '/' + str(image),gray_image)


        return render(request, "newImageEditing(gray).html",{'image':frame_b64})
    else:
        return render(request, "newImageEditing(gray).html")


@csrf_protect
def edge_detection(request):
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        img = Image.open(image)
        array = np.array(img)
        gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
        # edited_image = Image.fromarray(edges, 'RGB')
        # edited_image.save("F:/Images/Edge Detected Images" + '/' + str(image) )
        cv2.imwrite("F:/Images/Edge Detected Images" + '/' + str(image), edges)
        return render(request, "newImageEditing(edgedet).html")
    else:
        return render(request, "newImageEditing(edgedet).html")


@csrf_protect
def blur(request):   # not yet implemented
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        img = Image.open(image)
        array = np.array(img)

        ret, frame_buff = cv2.imencode('.jpg', array)  # could be png, update html as well
        frame_b64 = base64.b64encode(frame_buff)

        gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
        edited_image = Image.fromarray(edges, 'RGB')
        edited_image.save("F:/Images/Grayscale Images" + '/' + str(image) )
        return render(request, "newImageResize.html")
    else:
        return render(request, "newImageResize.html")

@csrf_protect
def filter(request):   # not yet implemented
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        img = Image.open(image)
        array = np.array(img)
        gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
        edited_image = Image.fromarray(edges, 'RGB')
        edited_image.save("F:/Images/Grayscale Images" + '/' + str(image) )
        return render(request, "newImageResize.html")
    else:
        return render(request, "newImageResize.html")

@csrf_protect
def brightness(request):   # not yet implemented
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        img = Image.open(image)
        array = np.array(img)
        gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
        edited_image = Image.fromarray(edges, 'RGB')
        edited_image.save("F:/Images/Grayscale Images" + '/' + str(image) )
        return render(request, "newImageResize.html")
    else:
        return render(request, "newImageResize.html")


@csrf_protect
def human_recognition(request):   # not yet implemented
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']       #posted image
        img = Image.open(image)       #posted image open
        array_image = np.array(img)       #posted image array
        image_to_be_passed = Image.fromarray(array_image, 'RGB')
        all_client = Client.objects.all()
        for client in all_client:
            print(client.name)
            client_image = client.image
            client_image_open = Image.open(client_image)
            client_image_array = np.array(client_image_open)
            verification = DeepFace.verify(array_image, client_image_array)
            print(verification)
            x = verification["distance"]
            if x <= 0.2:
                print("This Client is verified")
                print(client.name)
                print(client.contact)
                print(client.doc)
                return render(request, "newHumanRec.html",{"name":client.name, "contact":client.contact,
                                                           "doc":client.doc,"display_card_text":False,
                                                           "image":image_to_be_passed, 'display_details':True})
    else:
        return render(request, "newHumanRec.html",{"display_card_text":True, 'display_details':False})


@csrf_protect
def text_recognition(request):   # not yet implemented
    if request.method == 'POST' and request.FILES['img']:
        image = request.FILES['img']
        img = Image.open(image)
        array = np.array(img)
        image_to_be_saved = Image.fromarray(array,'RGB')
        image_to_be_saved.save("F:/rida data/SE project/DigitalImageProcessing/media/pics/text.jpg")
        # cv2.imwrite("../media/pics/"+"text",array)
        # gray_image = cv2.cvtColor(array,cv2.COLOR_BGR2GRAY)
        # edges = cv2.Canny(gray_image, threshold1=30, threshold2=100)
        # edited_image = Image.fromarray(edges, 'RGB')
        # edited_image.save("F:/Images/Grayscale Images" + '/' + str(image) )
        return render(request, "newTextRec.html")
    else:
        return render(request, "newTextRec.html")


@csrf_protect
def home(request):   #implementing
    return render(request, "newHome.html")


@csrf_protect
def login(request):   # not yet implemented  #implementing
    if 'username' in request.session:
        return home(request)
    if request.POST.get('username') and request.POST.get('password'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        print(request.session['username'],"this is username")
        print(username,password)
        try:
            user = User.objects.get(username = username)
            if user.password == password:
                print("valid credentials")
                return home(request)

            else:
                print('invalid password')

        except:
            print('invalid username')
    return render(request, "newLogin.html")





