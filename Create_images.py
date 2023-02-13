from Mat import Getgrafic
from Script_DB import SearchFps
import time

start = time.time()

def Create_images():
    """  создаём картинки для всех ИГР и всех GPU из списка  """

    """" параметры для запроса """
    game_names_data = [
                       '''Tom Clancy's Rainbow Six: Extraction''',
                       '''Watch Dogs: Legion''',
                       '''Far Cry 6'''
                       ]
    # '''Far Cry 6'''
    # '''Tom Clancy's Rainbow Six: Extraction'''
    # '''Watch Dogs: Legion'''
    # '''Hitman 3'''
    # '''Hunt: Showdown'''
    # '''Assassin’s Creed Valhalla'''
    # '''Horizon Zero Dawn'''
    # '''Cyberpunk 2077'''
    # '''Dying Light 2: Stay Human'''
    # '''Halo Infinite'''
    # '''Shadow of the Tomb Raider DX12'''
    # '''F1 2021 DX12'''
    # '''Performance Summary: 12 Game Average'''

    gpu_names_data = [
                    'RTX 3070',
                    'RTX 3090',
                    'RTX 4090'
                     ]

    # RTX 3070    RTX 3070 Ti    RTX 3080 10 GB    RTX 3080 Ti    RTX 3090    RTX 3090 Ti    RTX 4080    RTX 4090
    # RX 6800     RX 6800 XT     RX 6900 XT        RX 6950 XT

    cpu_name_data = 'Ryzen 7 5800X3D'
    dpi_data = ['1440p']  ###  ['2160p','1440p','1080p']

    """" дополнительные надписи на картинке """
    some_data = ', RT Off'


    for game_name in game_names_data:

        def Create_image():
            ''' Создаём картинку'''
            try:
                all_fpsavg_temp = []
                all_fpsmin1_temp = []
                for x in range(len(dpi_data)):
                    number = int(x)
                    quality_temp = []
                    for gpu_name in gpu_names_data:
                        a, b, video_name, quality = SearchFps(
                            gpu_name,
                            cpu_name_data,
                            game_name,
                            dpi_data[number]
                            )
                        all_fpsavg_temp.append(int(a))
                        all_fpsmin1_temp.append(int(b))
                    quality_temp.append(str(quality))
                    graficname = video_name+dpi_data[number]+ ('.png')
                    Getgrafic(gpu_names_data, all_fpsavg_temp, all_fpsmin1_temp, game_name, dpi_data[number], quality_temp[x],
                              some_data,graficname)
                    all_fpsavg_temp.clear()
                    all_fpsmin1_temp.clear()
                print('Create_image():', game_name, ''' - ОК!''')
                quality_temp.clear()
            except IndexError:
                print('Create_image():', game_name,  'Что то не то!')

        Create_image()

Create_images()

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3 / 1000, "s")