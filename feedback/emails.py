from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string
import youtube_dl
import cgi

def send_feedback_email(email,link):
    host = 'localhost'
    port = '8000'
    title = getVideoTitle(link)
    downloadLink = host + ':' + port+ "/media/" + title + ".mp3"
    message = downloadLink
    c = Context({'email': email, 'message': message})

    email_subject = render_to_string(
        'feedback/email/feedback_email_subject.txt', c).replace('\n', '')
    email_body = render_to_string('feedback/email/feedback_email_body.txt', c)

    email = EmailMessage(
        email_subject, email_body, email,
        [settings.DEFAULT_FROM_EMAIL], [],
        headers={'Reply-To': email}
    )
    return email.send(fail_silently=False)

def download_mp3(link):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/home/emli/mp3/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def getVideoTitle(link):
    
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(link, download=False)
    return meta['title']
