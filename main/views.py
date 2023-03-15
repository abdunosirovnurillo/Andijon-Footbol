from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from datetime import datetime


@api_view(['GET'])
def get_info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    social_med = Social_Media.objects.all()
    social_ser = Social_MediaSerializer(social_med, many=True)
    data = {
        "data":ser.data,
        "social_media":social_ser.data
    }
    return Response(data)



@api_view(['GET'])
def get_main(request):
    news = News.objects.filter(is_banner=True)
    news_ser = NewsSerializer(news, many=True)
    
    data = {
        "data":news_ser.data,
    }
    return Response(data)



@api_view(['GET'])
def get_media(request):
    media = Media.objects.all()
    ser = MediaSerializer(media, many=True)
    data =  {
        "data":ser.data
    }
    return Response(data)



@api_view(['GET'])
def get_news(request):
    new = News.objects.all()
    ser = NewsSerializer(new, many=True)
    data = {
        "data":ser.data
    } 
    return Response(ser)

@api_view(['GET'])
def get_shop(request):
    shop = Shop.objects.all()
    ser = ShopSerializer(shop, many=True)
    data = {
        "data":ser.data
    }
    return Response(data)





@api_view(['GET'])
def get_academiy(request):
    academiy = Academiy.objects.last()
    ser = AcademiySerializer(academiy, many=True)
    data = {
        "data":ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_about(request):
    about = About.objects.last()
    ser = AboutSerializer(about, many=True)
    data = {
        "data":ser.data
    }
    return Response(data)


@api_view(['GET'])
def get_statistic(request):
    match_next = Match.objects.all()
    ser_next = MatchSerializer(match_next, many=True)
    qurt = Quarter.objects.all()
    ser = QuarterSerializer(qurt, many=True)
    data = {
        "data": ser_next.data,
        "quart":ser.data
    }
    return Response(data)



@api_view(['GET'])
def get_players(request):
    palayer = Players.objects.all()
    ser = PlayersSerializer(palayer, many=True)
    data = {
        "data":ser.data
    }
    return Response(data)






