"""quizbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .quiz.views import RandomQuestion
from .Score.views import UpdateScores

urlpatterns = [
    path('admin/', admin.site.urls),
    # point my bot to a url
    # bot sends the information to get data
    # this is where bot finds data for a new question
    path('api/random/',RandomQuestion.as_view(),name = 'random'),
    path('api/score/update/',UpdateScores.as_view(),name = 'score_update'),

]
