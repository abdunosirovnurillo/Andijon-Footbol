from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from datetime import datetime


@api_view(['GET'])
def get_info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    data = {
        "data":ser.data
    }
    return Response(data)



@api_view(['GET'])
def get_main(request):
    news = News.objects.filter(is_banner=True)
    news_ser = NewsSerializer(news, many=True)
    matchs = Match.objects.all()
    ser = MatchSerializer(matchs, many=True)
    data = {
        "data":news_ser.data,
        "matchs":ser.data
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
    data = {
        "data": ser_next.data
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




@api_view(['GET'])
def add_product(request):
    form = Shop(request.POST, request.FIELS)
    if form.is_valid():
        form.save()
    ser = ShopSerializer(Shop.objects.all)
    data = {
        "data":ser.data
    }
    return Response(data)








