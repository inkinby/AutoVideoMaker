from Script_DB import Insertintest_list, SearchAllGamesWithGpu, Insertinimages_list, SearchAllImageName
import moviepy.editor as mp
from moviepy.editor import vfx, concatenate_videoclips,TextClip
import os
from random import randint
import sys
import time
from time import gmtime

#==============     <<<   Movi   >>>    ====================
start = time.time()

images_directory = "images/"    #  папка с картинками
videos_directory = "videos/"    #  папка с видео
final_filename = "my_stack16.mp4"    # имя финального файла
clip = mp.VideoFileClip("1920x1080.mp4")   #  имя файла для образца ширина, высота
(w, h) = clip.size

start_times_images = [2,18,35]  #  время появления картинок
time_videos = 16  #  длина показа одного видео
time_images = 10  #  длина показа одной картинки
images_hash = []
text_hash = []
videos_hash_concatenate = []
images_list = []          #  Список картинок для финала
selected_video_list = []  #  Список видео с играми для финала


def Create_images_and_videos_lists():
    """ Создание списка картинок images_list и списка видео selected_video_list """

    """ создание списка картинок для подбора видео """
    images_list_for_select_video_temp = []
    all_images_in_path = os.listdir(images_directory)
    all_images_in_path.sort()
    all_images_in_path.remove('_background.png')
    all_images_in_path.remove('_logo.png')
    for image_in in all_images_in_path:
        images_list_for_select_video_temp.append(image_in)

    """ для всех картинок подобрать видео в папке """
    all_videos_in_path = os.listdir(videos_directory)
    for images_in, video_in in zip(images_list_for_select_video_temp,all_videos_in_path):
        for video_in in all_videos_in_path:
            if images_in[:-9] == video_in[:-4]:
                selected_video_list.append(video_in)
    if len(selected_video_list) < len(images_list_for_select_video_temp):
        sys.exit("  Картинок БОЛЬШЕ чем роликов!\n ---------  ОТКАЗ СИСТЕМЫ  ----------")
    elif len(selected_video_list) > len(images_list_for_select_video_temp):
        print("  Картинок МЕНЬШЕ чем роликов!\n ---------  НО МЫ ПРОДОЛЖАЕМ  ----------")
    else:
        print("Картинок и роликов для монтажа одинаково. Всё ок.")

    """" набиваем список картинок для монтажа +background на задний фон для каждой"""
    for image in all_images_in_path:
        images_list.append("_background.png")
        images_list.append(image)


def Moviepy_text_processing():
    """ обработка текста """
    text = "Please like and subscribe"
    text_clip_one2 = TextClip(text, font="Arial", fontsize=70, color='white').set_duration(20)
    text_clip_one1 = text_clip_one2.set_start(5)
    # text_clip_one = text_clip_one1.set_pos('center')
    text_clip_one = text_clip_one1.set_pos((40, clip.h -144))
    text_hash.append(text_clip_one)


def Moviepy_video_processing():
    '''  обработка видео из списка selected_video_list '''
    videos_hash_temp = []
    for video in selected_video_list:
        rand_first = randint(0, 60)
        rand_second = rand_first + time_videos
        print('Рандомные секунды для ',video, ' : ',rand_first,rand_second)
        """ применение эффектов к видео и аудио """
        video_clip = mp.VideoFileClip(videos_directory+video).subclip(rand_first, rand_second)
        video_fadein = video_clip.fadein(1.0)                       # эффект появления видео
        video_fadeout = video_fadein.fadeout(1.0)                   # эффект исчезания видео
        video_audio_fadein = video_fadeout.audio_fadein(3)          # эффект появления аудио
        video_audio_fadeout = video_audio_fadein.audio_fadeout(3)   # эффект исчезания аудио
        videos_hash_temp.append(video_audio_fadeout)
    concatenate = concatenate_videoclips(videos_hash_temp)
    videos_hash_concatenate.append(concatenate)


def Moviepy_image_processing():
    ''' время появления картинок и background'а одновременно '''
    timeslist_temp = []
    for time in start_times_images:
        timeslist_temp.append(time)
        timeslist_temp.append(time)
    ''' применение эффектов для всех картинок в списке images_list '''
    for x,y in zip(timeslist_temp, images_list):
        if y == "_background.png":                            # Обработка _background.png
            # print("_background.png")
            name = mp.ImageClip(images_directory + y)
            resize = name.resize(height=h * 0.8, width=w * 0.8) # размер
            opacity = resize.set_opacity(0.7)                   # прозрачность
            position = opacity.set_position("center")           # расположение
            duration = position.set_duration(time_images)       # продолжительность времени показа
            crossfadein = duration.crossfadein(1.0)             # эффект появления
            crossfadeout = crossfadein.crossfadeout(1.0)        # эффект исчезания
            Bargraph = crossfadeout.set_start(x)                # время начала показа
            images_hash.append(Bargraph)
        else:                                                 # Обработка всех остальных картинок
            name = mp.ImageClip(images_directory+y)
            resize = name.resize(height=h * 0.8, width=w * 0.8) #  размер
            opacity = resize.set_opacity(1)                     #  прозрачность
            position = opacity.set_position("center")           #  расположение
            duration = position.set_duration(time_images)       #  продолжительность времени показа
            crossfadein = duration.crossfadein(1.0)             #  эффект появления
            crossfadeout = crossfadein.crossfadeout(1.0)        #  эффект исчезания
            Bargraph = crossfadeout.set_start(x)                #  время начала показа
            images_hash.append(Bargraph)


def Final():
    ''' Финалим монтаж, создаём итоговый видеофайл '''
    videos_and_images = videos_hash_concatenate + images_hash + text_hash
    # print(f"videos_and_images: {videos_and_images}")
    final = mp.CompositeVideoClip(videos_and_images, size=clip.size)
    # final.write_videofile(filename=final_filename,  ffmpeg_params=['-c:v', 'libx265', '-cq:v', '21', '-rc:v', 'vbr', '-preset:v', 'fast'])
    final.write_videofile(filename=final_filename,
                          ffmpeg_params=['-c:v', 'hevc_nvenc', '-gpu:v', '0', '-cq:v', '21', '-rc:v', 'vbr',
                                         '-preset:v', 'fast'])
    # moviepy.video.io.ffmpeg_tools.ffmpeg_merge_video_audio(final.write_videofile(filename="my_stack11.mp4", ffmpeg_params='-c:v libx265' ))
    # H.264 / AVC (encoders: libx264 libx264rgb h264_amf h264_nvenc h264_qsv )
    # H.265 / HEVC (encoders: libx265 hevc_amf hevc_nvenc hevc_qsv)  , preset='ultrafast'



# tym = time.localtime()
# opt = time.strftime("%H:%M:%S",tym)
# print(opt)
Create_images_and_videos_lists()  #1
Moviepy_video_processing()        #2
Moviepy_image_processing()        #3
# Moviepy_text_processing()         #4
Final()                           #Last
# print(opt)

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3 / 1000, "s")



def All_Test_GPU():
    a = SearchAllGamesWithGpu('RX 6800')
    sum = 0
    for i in a:
        print(i)
        sum = sum+1
    print(sum)


# All_Test_GPU()

# Insertintest_list(
#     'RTX 4080',
#     'Ryzen 7 5800X3D',
#     '''Shadow of the Tomb Raider DX12''',
#     '2160p',
#     'Highest Quality / TAA',
#     '116',
#     '109',
#     'Off',
#     'Off',
#     'Off',
#     'ShadowoftheTombRaider'
#      )

###########################################################################

 # имена всех файлов папки в список
# print('\n'.join(_list_name_files)) # выводим список имен файлов

# print(i,Bargraphs[i])  ### ={'aaa':'15','bbb':'35','ccc':'50'}
# print(x, y) #, sep='\t\t')   ###  =[15,35,50] = "foo2.png","foo3.png","foo4.png"]

# print('fetchmany', c.fetchall())
# print('fetchmany',  c.fetchmany(2))
# print('fetchone',  c.fetchone()[0:4])
