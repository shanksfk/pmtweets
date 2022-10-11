
from re import template
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Tweet
from django.http import HttpResponse, JsonResponse

@csrf_exempt
@api_view(['GET', 'POST'])
def Tweet_list(request):
    """
    List all Tweets, or create a new Tweet.
    """
    if request.method == 'GET':
        Tweets = Tweet.objects.all()
        serializer = TweetSerializer(Tweets, many=True)
        import json
        from rest_framework.renderers import JSONRenderer

        # context = JSONRenderer().render(serializer.data)
        # context=serializer.data
        return render (request, 'home.html', {'tweets':serializer.data}) 
        # JsonResponse(serializer.data,safe=False)
        # return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TweetList(ModelViewSet):
    serializer_class=TweetSerializer
    queryset=Tweet.objects.all()
    """
    List all Tweets, or create a new Tweet.



    """
def index(request):
    tweets=[]
    for tweet in Tweet.objects.all():
        tweets.append({
            'name':tweets.name,
            'message':tweets.message,
            # 'created_at':tweets.created_at
        })

    return JsonResponse(tweets, safe=False)

    
    # template_name='home.html'

    # def get(self, request, format=None):
    #     Tweets = Tweet.objects.all()
    #     serializer = TweetSerializer(Tweets, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = TweetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
