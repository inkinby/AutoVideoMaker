import sqlite3

#############################
#   [gpu_name] TEXT,
#   [cpu_name] TEXT,
#   [game_name] TEXT,
#   [dpi] TEXT,
#   [quality] TEXT,
#   [fps_avg] TEXT,
#   [fps_min_1] TEXT,
#   [ray_tracing] TEXT,
#   [dlss20] TEXT,
#   [dlss30] TEXT);
##############################

db = sqlite3.connect('C:/Python_pro/Testbytest/111.db')
c = db.cursor()


#  РАБОЧИЙ   Добавление Теста в таблицу С проверкой
def Insertintest_list(gpu,cpu,game,dpi,quality,fps_avg,fps_min_1,ray_tracing,dlss20,dlss30,video_name):
    gpu_1 = gpu = gpu
    cpu_1 = cpu = cpu
    game_1 = game = game
    dpi_1 = dpi = dpi
    quality_1 = quality = quality
    fps_avg_1 = fps_avg = fps_avg
    fps_min_1_1 = fps_min_1 = fps_min_1
    ray_tracing_1 = ray_tracing = ray_tracing
    dlss20_1 = dlss20 = dlss20
    dlss30_1 = dlss30 = dlss30
    video_name_1 = video_name = video_name
    c.executemany("""
              INSERT INTO test_list (gpu_name,cpu_name,game_name,dpi,quality,fps_avg,fps_min_1,ray_tracing,dlss20,dlss30,video_name)
              SELECT * FROM (SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) AS tmp
              WHERE NOT EXISTS (SELECT * FROM test_list
              WHERE gpu_name = (?)
              AND cpu_name = (?)
              AND game_name = (?)
              AND dpi = (?)
              AND quality = (?)
              AND fps_avg = (?)
              AND fps_min_1 = (?)
              AND ray_tracing = (?)
              AND dlss20 = (?)
              AND dlss30 = (?)
              AND video_name = (?)) LIMIT 1;
              """,
              [(gpu,cpu,game,dpi,quality,fps_avg,fps_min_1,ray_tracing,dlss20,dlss30,video_name, gpu_1,cpu_1,game_1,dpi_1,quality_1,fps_avg_1,fps_min_1_1,ray_tracing_1,dlss20_1,dlss30_1,video_name_1)])

    db.commit()
    db.close

#  РАБОЧИЙ   Добавление Имени файла картинки с тестом (с проверкой)
def Insertinimages_list(image,game,dpi):
    image_1 = image = image
    game_1 = game = game
    dpi_1 = dpi = dpi
    c.executemany("""
              INSERT INTO images_list (image_name,game_name,dpi)
              SELECT * FROM (SELECT ?, ?, ?) AS tmp
              WHERE NOT EXISTS (SELECT * FROM images_list
              WHERE image_name = (?)
              AND game_name = (?)
              AND dpi = (?)) LIMIT 1;
              """,
              [(image,game,dpi,image_1,game_1,dpi_1)])

    db.commit()
    db.close




#  Поиск FPS_AVG и FPS_MIN_1% по GPU
def SearchFps(gpu,cpu,game,dpi):    # ,quality
    gpu = gpu
    cpu = cpu
    game = game
    dpi = dpi
    # quality = quality
    c.execute("""
            SELECT fps_avg, fps_min_1, video_name, quality  FROM test_list
            WHERE gpu_name = (?)
            AND cpu_name = (?)
            AND game_name = (?)
            AND dpi = (?)
            """,    # AND quality = (?)
            [gpu,cpu,game,dpi])      #,quality
    items = c.fetchall()
    # print(' в скрипте', '\n', 'FPS AVG =',items[0][0], '\n', 'FPS min 1%=',items[0][1])
    gpufpsavg = items[0][0]
    gpufpsmin1 = items[0][1]
    video_name = items[0][2]
    qualities = items[0][3]
    db.close
    return gpufpsavg, gpufpsmin1, video_name, qualities


#  Поиск всех игр протестированных на этой GPU
def SearchAllGamesWithGpu(gpu):
    gpu = gpu
    c.execute("""
            SELECT game_name, dpi FROM test_list
            WHERE gpu_name = (?)
            """,
            [gpu])
    items = c.fetchall()
    a = items
    return a
    db.close


#  Поиск всех названий картинок в БД return СРАЗУ СПИСКОМ
def SearchAllImageName():
    c.execute("""
            SELECT image_name FROM images_list
            """)
    image_name_list = [i[0] for i in c.fetchall()]
    return image_name_list
    db.close



#   Добавление теста в таблицу с проверкой
def InsertWithCheck3():

    c.execute("""
              INSERT INTO test (gpu_name, cpu_name, game_name)
              SELECT * FROM (SELECT 'RX 6950 XT BT2', 'Ryzen 7 5800X3D', 'Watch Dogs: Legion') AS tmp
              WHERE NOT EXISTS (SELECT * FROM test
              WHERE gpu_name = 'RX 6950 XT BT2'
              AND cpu_name = 'Ryzen 7 5800X3D'
              AND game_name = 'Watch Dogs: Legion') LIMIT 1;
              """)
    db.commit()
    db.close


#   Добавление теста в таблицу С проверкой с использованием передачи отдельных переменных
def InsertWithCheck4(gpu,cpu,game,dpi,quality,fps_avg,fps_min_1,ray_tracing,dlss20,dlss30):
    gpu = gpu
    cpu = cpu
    game = game
    dpi = dpi
    quality = quality
    fps_avg = fps_avg
    fps_min_1 = fps_min_1
    ray_tracing = ray_tracing
    dlss20 = dlss20
    dlss30 = dlss30
    c.execute("""
              INSERT INTO test (gpu_name,cpu_name,game_name,dpi,quality,fps_avg,fps_min_1,ray_tracing,dlss20,dlss30)
              SELECT * FROM (SELECT 'RX 6950 XT BT2', 'Ryzen 7 5800X3D', 'Watch Dogs: Legion') AS tmp
              WHERE NOT EXISTS (SELECT * FROM test
              WHERE gpu_name = 'RX 6950 XT BT2'
              AND cpu_name = 'Ryzen 7 5800X3D'
              AND game_name = 'Watch Dogs: Legion') LIMIT 1;
              """)
    db.commit()
    db.close


#   Добавление теста в таблицу БЕЗ проверки с использованием переменных в списке
def InsertWithCheck2():
    values = ['RX 6950999','Ryzen 7 5800X3D', 'Watch Dogs: Legion']
    c.execute("""
            INSERT INTO test
            (gpu_name, cpu_name, game_name)
            VALUES (?,?,?)""",
            values)
    db.commit()
    db.close


#   Добавление теста в таблицу БЕЗ проверки с использованием передачи отдельных переменных
def InsertWithCheck5(gpu,cpu,game):
    gpu = gpu
    cpu = cpu
    game = game
    c.execute("""
            INSERT INTO test
            (gpu_name, cpu_name, game_name)
            VALUES (?,?,?)""",
            [gpu, cpu, game])
    db.commit()
    db.close
