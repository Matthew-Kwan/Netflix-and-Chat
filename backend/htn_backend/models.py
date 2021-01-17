from django.db import models

# Create your models here.

class Show(models.Model):
  """ This model will contain data on each Episode on Netflix """
  unique_id = models.IntegerField(primary_key=True)
  description = models.CharField(max_length=3000)

  def get_id(self):
    """ Getter function for returning the id """
    return self.id

  def get_description(self):
    """ Getter funciton for returning the title """
    return self.description

class Message(models.Model):
  """ This model will contain data on each message """
  content = models.CharField(max_length=500)
  time = models.FloatField()
  username = models.CharField(max_length=100)
  show = models.ForeignKey(Show, on_delete=models.CASCADE)

  def get_content(self):
    """ Getter function for returning the message content """
    return self.content

  def get_time(self):
    """ Getter function for returning the time """
    return self.time

  def get_show(self):
    """ Getter function for returning the show """
    return self.show

