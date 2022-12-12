from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profileapp.models import Profile
from .forms import TwittForm
from .models import Twitt
from .serializers import ProfileSerializer, TwittReserializer, TwittSerializer, TwittActionSerializer

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home_view(request, *arg, **kwargs):
    return render(request, "pages/home.html", context = {}, status = 200)

def popular_view(request, *arg, **kwargs):
    return render(request, "pages/home.html", context = {}, status = 200)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def twitt_create_view(request, *args, **kwargs):
    serializer = TwittSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def twitt_list_view(request, *arg, **kwargs):
    queryset = Twitt.objects.all()
    serializer = TwittSerializer(queryset, many=True)
    
    return Response(serializer.data, status=200)

@api_view(['GET'])
def twitt_detailed_view(request, twitt_id, *arg, **kwargs):
    queryset = Twitt.objects.filter(id=twitt_id)
    if not queryset.exists():
        return Response({}, status=404)
    obj = queryset.first()
    serializer = TwittSerializer(obj)
    
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def twitt_delete_view(request, twitt_id, *arg, **kwargs):
    queryset = Twitt.objects.filter(id=twitt_id)
    if not queryset.exists():
        return Response({}, status=404)
    queryset = queryset.filter(user=request.user)
    if not queryset.exists():
        return Response({"message" : "You cannot delete this twitt."}, status=401)
    obj = queryset.first()
    obj.delete()
    
    return Response({"message" : "Twitt successfully deleted."}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def twitt_like_view(request, *args, **kwargs):
    serializer = TwittActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        twitt_id = data.get('id')
        action = data.get('action')

        queryset = Twitt.objects.filter(id=twitt_id)
        if not queryset.exists():
            return Response({}, status=404)
        obj = queryset.first()
        if action == "like":
            obj.likes += 1
            obj.save()
            serializer = TwittSerializer(obj)
            return Response(serializer.data, status=200)

    return Response({"message" : "Twitt liked!"}, status=200)

@api_view(['GET'])
def twitt_profile_view(request, *arg, **kwargs):
    queryset = Profile.objects.filter(user=request.user)
    serializer = ProfileSerializer(queryset, many=True)
    
    return Response(serializer.data, status=200)

@api_view(['GET'])
def twitt_owner_view(request, twitt_id, *arg, **kwargs):
    queryset = Twitt.objects.filter(id=twitt_id)
    serializer = TwittReserializer(queryset, many=True)
    
    return Response(serializer.data, status=200)

@api_view(['GET'])
def twitt_profile_lookup_view(request, user_id, *arg, **kwargs):
    queryset = Profile.objects.filter(id=user_id)
    serializer = ProfileSerializer(queryset, many=True)
    
    return Response(serializer.data, status=200)

def DEPRACATED_twitt_create_view(request, *arg, **kwargs):
    user = request.user
    if not user.is_authenticated:
        if is_ajax(request):
            return JsonResponse({}, status=401)
        return redirect('/login')
    form = TwittForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if is_ajax(request):
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None:
            return redirect(next_url)
        form = TwittForm()
    if form.errors:
        if is_ajax(request):
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form" : form})

def DEPRACATED_twitt_list_view(request, *arg, **kwargs):
    queryset = Twitt.objects.all()
    twitt_list = [x.serialize() for x in queryset]
    data = {
        "isUser" : False,
        "response" : twitt_list
    }
    
    return JsonResponse(data)

def DEPRACATED_twitt_detailed_view(request, twitt_id, *args, **kwargs):
    data = {
        "id" : twitt_id
    }
    status = 200
    try:
        obj = Twitt.objects.get(id = twitt_id)
        data['content'] = obj.content
    except:
        data['message'] = "content doest not exist."
        status = 404
    
    return JsonResponse(data, status = status)
