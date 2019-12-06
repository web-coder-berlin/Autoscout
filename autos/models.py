# Create your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class autos(models.Model):
    autos_TYPES = [
        ('G', 'Good news'),  # Wert und lesbare Form
        ('B', 'Bad news'),
        ('F', 'Fake news'),
        ('A', 'Aliens news !?!?'),
    ]

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100,
                                blank=True)
    author = models.CharField(max_length=50)

    date_published = models.DateTimeField(blank=True,
                                      default=datetime.now)
    type = models.CharField(max_length=1,
                            choices=autos_TYPES,
                            )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             #related_name='users',
                             #related_query_name='user',
                             )

    class Meta:
        ordering = ['date_published']
        verbose_name = 'auto'
        verbose_name_plural = 'autos'

    def get_full_title(self):
        return_string = self.title
        if self.text:  # if text is not empty
            return_string = self.title + ': ' + self.text
        return return_string

    def spamercheck(username):


        user = User.objects.get(username=username)

        pt = autos.objects.filter(user=user)
        print("############",len(pt))
        for i in range( 0, len(pt)-1):
            v=i+1
            print("************ vor check")
            j = pt[v].date_published - pt[i].date_published
            if j.seconds  < 60 :
               print("*********** im test")
               return True
        print("************** nach check")
        return False








    def __str__(self):
        return self.title + ' (' + self.author + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.author + ' / ' + self.type
