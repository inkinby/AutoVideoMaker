import numpy as np
import matplotlib.pyplot as plt


def Getgrafic(gpu_names_data,all_fpsavg,all_fpsmin1,game_name_data,dpi_data,quality_temp,ray_tracing_data,graficname):
    gpu_name = gpu_names_data
    fpsavg = all_fpsavg
    fpsmin1 = all_fpsmin1
    game_name = game_name_data
    dpi = dpi_data
    quality = str(quality_temp)
    ray_tracing = ray_tracing_data
    grafic_name = graficname

    x = np.arange(len(gpu_name))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()

    rects1 = ax.barh(x + width / 2, fpsavg, width, label='AVG')  # , color='#355b9f')
    rects2 = ax.barh(x - width / 2, fpsmin1, width, label='1%')  # , color='#738fd1')

    ax.set_title(str(game_name)+'\n'+str(dpi) +', '+ quality+ray_tracing, fontsize=18, color='w')
    ax.set_yticks(x, gpu_name, fontsize=14, color='w')
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.ylabel('Frames Per Second', fontsize=12, color='w')
    ax.yaxis.set_label_position("right")
    ax.legend(markerfirst=False)

    ax.bar_label(rects2, padding=-30, fontsize=14, color='w')
    ax.bar_label(rects1, padding=-30, fontsize=14, color='w')

    plt.tight_layout()
    images_directory = "images/"
    plt.savefig(images_directory+str(grafic_name), dpi=480,  transparent=True, bbox_inches='tight')
    # plt.show()


###################################################################
# """ Not use  """
# labels = ['GTX 1660 super', 'RTX 3070', 'RTX 4090']
# men_means = [21, 38, 65]
# women_means = [25, 42, 75]
#
# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars
# fig, ax = plt.subplots()
#
# rects1 = ax.barh(x + width/2, women_means, width, label='AVG') #, color='#355b9f')
# rects2 = ax.barh(x - width/2, men_means, width, label='1%') #, color='#738fd1')
#
# ax.set_title('Shadow of the Tomb Raider \n (1440p, Very High Quality, TAA)', fontsize=20, color='w')
# ax.set_yticks(x, labels, fontsize=14, color='w')
# plt.setp(ax.get_xticklabels(), visible=False)
# plt.ylabel('Frames Per Second', fontsize=12, color='w')
# ax.yaxis.set_label_position("right")
# ax.legend(markerfirst=False)
#
# ax.bar_label(rects2, padding=-23, fontsize=14, color='w')
# ax.bar_label(rects1, padding=-23, fontsize=14, color='w')
#
# plt.tight_layout()
# # plt.savefig('foo17.png', dpi=480,  transparent=True, bbox_inches='tight')
# plt.show()

################################################################