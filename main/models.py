from django.db import models



class Info(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="logo/")
    text = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()



class Social_Media(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="Social_Media/")
    link = models.URLField()




class Main(models.Model):
    title = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    text = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    des = models.CharField(max_length=255)
    is_banner = models.BooleanField(blank=True, null=True)


class Match(models.Model):
    tay1 = models.CharField(max_length=255)
    tay2 = models.CharField(max_length=255)
    quarter = models.IntegerField()
    time = models.DateField()



class Team(models.Model):
    name  = models.CharField(max_length=255)


class Academiy(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to='Acsdemiy/')
    text = models.TextField()
    name = models.CharField(max_length=255)


class Media(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="img/")
    vidio = models.FileField()
    date = models.DateTimeField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    goal = models.IntegerField()
    goal2 = models.IntegerField()




class About(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="img/")
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()






class Forma(models.Model):
    color = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo_T_short = models.ImageField(upload_to='T-short/')
    purchase = models.ImageField(upload_to='purchase/')
    cup = models.ImageField(upload_to='cup/')
    command = models.ForeignKey(Team, on_delete=models.CASCADE)





class Statistic(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    teams_vs = models.IntegerField()
    watch = models.DateField()
    table = models.IntegerField()

class Quarter(models.Model):
    number = models.CharField(max_length=255)


class Shop(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(blank=True, null=True, upload_to='Shop/')


class Players(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to="Players/")
    number =  models.CharField(max_length=255)
    game = models.IntegerField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)




