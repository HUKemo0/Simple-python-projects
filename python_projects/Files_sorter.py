import os
import shutil

cwd = input('Please enter your folder location: ')

music = os.path.join(cwd,'Music')
videos = os.path.join(cwd,'Videos')
apps = os.path.join(cwd,'Apps')
documents = os.path.join(cwd,'Documents')
photos = os.path.join(cwd,'Photos')
# other = os.path.join(cwd, "other")

if not os.path.exists(music) :
    os.mkdir(music)
if not os.path.exists(videos) :
   os.makedirs(videos)
if not os.path.exists(documents) :
    os.makedirs(documents)
if not os.path.exists(photos) :
    os.makedirs(photos)
if not os.path.exists(apps) :
    os.makedirs(apps)
# if not os.path.exists(other):
#     os.makedirs(other)

for n in os.listdir(cwd):
    if n.endswith(".txt") or n.endswith(".docx") or n.endswith('.dot') or n.endswith('.docm') or n.endswith('.doc') or n.endswith('.html') or n.endswith('.dotx') or n.endswith('.eml') or n.endswith('.pdf') or n.endswith('.pot') or n.endswith('.potm') or n.endswith('.potx') or n.endswith('.ppam') or n.endswith('.pps') or n.endswith('.ppt') or n.endswith('.pptm') or n.endswith('.pptx') or n.endswith('.rar') or n.endswith('.rtf') or n.endswith('.sldm') or n.endswith('.sldx') or n.endswith('.xla') or n.endswith('.xlam') or n.endswith('.xll') or n.endswith('.xlm') or n.endswith('.xls') or n.endswith('.xlsm') or n.endswith('.xlsx') or n.endswith('.xlt') or n.endswith('.xltm') or n.endswith('.xltx') or n.endswith('.zip') or n.endswith('7z'):
        current_file = os.path.join(cwd, n)
        shutil.move(current_file, documents)

    elif n.endswith('.aac') or n.endswith('.adt') or n.endswith('.adts') or n.endswith('.aif') or n.endswith('.aifc') or n.endswith('.aiff') or n.endswith('.m4a') or n.endswith('.mp3'):
        current_file = os.path.join(cwd, n)
        shutil.move(current_file, music)

    elif n.endswith('.exe') or n.endswith('.iso') or n.endswith('.apk') or n.endswith('.cmd'):
        current_file = os.path.join(cwd, n)
        shutil.move(current_file, apps)

    elif n.endswith('.mp4') or n.endswith('.mkv'):
        current_file = os.path.join(cwd, n)
        shutil.move(current_file, videos)

    elif n.endswith('.gif') or n.endswith('.jpg') or n.endswith('.jpeg') or n.endswith('.png') or n.endswith('.psd'):
        current_file = os.path.join(cwd, n)
        shutil.move(current_file, photos)

    # elif n.endswith():
    #     current_file = os.path.join(cwd, n)
    #     shutil.move(current_file, other)
