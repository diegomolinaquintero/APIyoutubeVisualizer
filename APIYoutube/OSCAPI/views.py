from django.shortcuts import render
from googleapiclient.discovery import build
from django.http import JsonResponse
from pythonosc import osc_message_builder
from pythonosc import udp_client
import json

from django.conf import settings


def obtener_datos_youtube(request):
    youtube = build('youtube', 'v3', developerKey=settings.GOOGLE_API_KEY)
    video_link = request.GET.get('link', '')
    video_id = video_link.split('=')[1]
    video = youtube.videos().list(part='snippet,statistics,topicDetails,contentDetails', id=video_id).execute()
    print(video)
    
    video_json = json.dumps(video)
    osc_msg = osc_message_builder.OscMessageBuilder(address='/youtube')
    osc_msg.add_arg(video_json)

    osc_client = udp_client.SimpleUDPClient(settings.OSC_ADDRESS, settings.OSC_PORT)
    osc_client.send(osc_msg.build())

    return render(request, 'youtube.html', {'video': video})

def form(request):
    return render(request, 'form.html')

