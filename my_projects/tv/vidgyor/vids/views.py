# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
import os
from django.db import connection
# Create your views here.
from django.shortcuts import render
from .models import Video, VideoMetadata,TempVal
#from .forms import VideoForm
from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from vidgyor import helpers

def showvideo(request):
    if request.method =='POST':
        video=Video()
        video.title=request.POST.get('title')
        video.name=request.POST.get('title')
        video.description=request.POST.get('description')
        video.tags=request.POST.get('tags')
        video.categories=request.POST.get('categories')
        video.videofile=request.FILES['videofile']
        filename ="%s"% (video.videofile)
        filename = filename.replace("videos/",'')
        video.save()
        meta_video=VideoMetadata()
        meta_video.meta_title_id=video.title
        filename = "/home/priyanka/my_projects/tv/vidgyor/media/videos/%s"%(filename)
        filename=filename.replace(" ","_")
        filename, realname = filename, filename.encode('utf-8')
        parser = createParser(filename, realname)
        metadata = extractMetadata(parser)
        text = metadata.exportPlaintext()
        for item in text:
            if 'Duration' in item:
                dur, dur_val = item.split(": ")
                dur=dur[2:]
                meta_video.duration=dur_val
            elif 'Creation ' in item:
                cre, cre_date = item.split(": ")
                cre=cre[2:]
                meta_video.created_on=cre_date
        meta_video.save()


    #lastvideo= Video.objects.last()

    #videofile= lastvideo.videofile


    #form= VideoForm(reqiuest.POST or None, request.FILES or None)
    #if form.is_valid():
     #   form.save()


    #context= {'videofile': videofile,
    #          'form': form
    #          }


    return render(request,'main_page.html')# 'videos.html')#, context)

def showlist(request):
    main_dic = {}
    result = None
    if request.GET.get('edit'):
        temp = TempVal.objects.get(pk=1)
        temp = temp.temp_val
        #video = Video.objects.get(title= temp)
        name = request.GET.get('name')
        tags = request.GET.get('tags')
        categories = request.GET.get('categories')
        description = request.GET.get('description')
        cursor = connection.cursor()
        cursor.execute("update vids_video set name = %s,tags=%s,description=%s,categories=%s where title=%s",[name,tags,description,categories,temp])
        #video.save()

    if request.POST.get('create_video'):
        showvideo(request)
    if request.GET.get('search'):
        search_title = request.GET.get('search')
        result = VideoMetadata.objects.raw("select * from vids_videometadata a inner join vids_video b ON a.meta_title_id = b.title where b.name='%s'"%(search_title))
    else:
        result = VideoMetadata.objects.raw("select * from vids_videometadata a inner join vids_video b ON a.meta_title_id = b.title")
    result = helpers.pg_records(request, list(result), 2)
    main_dic['video']=result
    return render(request,'main_page.html',main_dic)

def edit(request):
    if request.GET.get('id'):
        temp = TempVal.objects.get(pk=1)
        temp.temp_val=request.GET.get('id')
        temp.save()

    return render(request,'edit.html')   

