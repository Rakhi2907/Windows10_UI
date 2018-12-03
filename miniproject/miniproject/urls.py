"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from project import views as mview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mview.table),
    path('apps',mview.index),
    path('PC',mview.PC),
    path('alarms',mview.alarms_clock),
    path('calc',mview.calc),
    path('cam',mview.camera),
    path('cortana',mview.cortana),
    path('docs',mview.documents),
    path('fb',mview.facebook),
    path('fd_hub',mview.fd_hub),
    path('get_help',mview.Get_help),
    path('chrome',mview.chrome),
    path('c_drive',mview.C_drive),
    path('maps',mview.maps),
    path('solitaire',mview.solitaire),
    path('movies',mview.movies),
    path('notepad',mview.notepad),
    path('Notepad',mview.Notepad),
    path('photos',mview.photos),
    path('paint',mview.paint),
    path('explorer',mview.explorer),
    path('skype',mview.skype),
    path('sticky',mview.sticky),
    path('tips',mview.tips),
    path('voicerecorder',mview.vRecorder),
    path('wordpad',mview.wordpad),
    path('weather',mview.weather),
    path('wmplayer',mview.wmplayer),
]