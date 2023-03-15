from rest_framework.serializers import ModelSerializer
from .models import *



class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__" 


class Social_MediaSerializer(ModelSerializer):
    class Meta:
        model = Social_Media
        fields = "__all__" 



class MainSerializer(ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__" 

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__" 


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__" 






class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        field = "__all__" 

class PlayersSerializer(ModelSerializer):
    class Meta:
        model = Players
        field = "__all__" 

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        field = "__all__" 

class AcademiySerializer(ModelSerializer):
    class Meta:
        model = Academiy
        field = "__all__" 


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        field = "__all__" 




class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        field = "__all__" 





class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        field = "__all__" 


class FormaSerializer(ModelSerializer):
    class Meta:
        model = Forma
        field = "__all__" 




class StatisticSerializer(ModelSerializer):
    class Meta:
        model = Statistic
        field = "__all__" 
