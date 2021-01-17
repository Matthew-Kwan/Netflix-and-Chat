from django.http.response import Http404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import generics
from .models import Show, Message
from .serializers import ShowSerializer, MessageSerializer


# Create your views here.
class ShowIdentifier(APIView):
  """
  Get Episode, or Post Episode
  """
  def get(self, request, pk, format=None):
    """ Get a specific Episode """

    print(request)
    print("PK:", pk)

    try:
      show = Show.objects.get(unique_id=pk)
      messages = show.message_set.all()
      data = serializers.serialize('json', messages)
      return HttpResponse(data, status=200)

    except Show.DoesNotExist:
      raise Http404

class ShowList(APIView):

  def post(self, request, format=None):
    """ Create a new show """

    data = request.data

    # Serializer
    serializer = ShowSerializer(data=data)

    if serializer.is_valid():
      serializer.save()

      return Response(status=201)

    else:
      return Response(status=400)

class MessageList(APIView):

  def post(self, request, format=None):
    """ Create a message """

    data = request.data

    message = {
      'content': data['content'],
      'time': data['time'],
      'username': data['username'],
      'show': data['unique_id']
    }

    # Serializer
    serializer = MessageSerializer(data=message)

    serializer.is_valid()
    print(serializer)
    print("Serializer: ", serializer.errors)


    if serializer.is_valid():
      serializer.save()
      return Response(status=201)

    else:
      return Response(status=400)


