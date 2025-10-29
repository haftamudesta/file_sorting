import os,shutil
from pathlib import Path

# PATH_DOWNLOADS="C:\Users\hafta\Downloads"

PATH_DOWNLOADS=Path.home() / "Downloads"

CATEGORIES = {
    '_Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    '_Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    '_Docs': ['.pdf', '.docx', '.txt', '.doc', '.pptx', '.ppt', '.odt'],
    '_ZIPs': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '_Installers': ['.exe', '.msi', '.dmg', '.pkg','.msix'],
    '_Code': ['.py', '.js', '.html', '.css', '.md', '.json', '.xml', '.java', '.cpp', '.c'],
    '_Data': ['.csv', '.xlsx', '.xls', '.tsv'],
    '_Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    '_Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    '_Design': ['.fig', '.psd', '.svg', '.dw'],
    '_Subtitle': ['.vtt'],
}

def get_file_cat(fileName):
    if fileName.startswith("_"):
        return None

    filepath=os.path.join(PATH_DOWNLOADS,fileName)
    if os.path.isdir(filepath):
        return ".Folders"
    else:
        file_extension= '.' + file.split('.')[-1]#Telegram Desktop Installer.exe take .exe 
        for cat,list_keywords in CATEGORIES.items():
            if file_extension.lower() in list_keywords:
                return cat
        return ".Others"
    

for file in os.listdir(PATH_DOWNLOADS):
    dir_name=get_file_cat(file)

    if dir_name:
        dir_filePath=os.path.join(PATH_DOWNLOADS,dir_name)
        if not os.path.exists(dir_filePath):
            os.makedirs(dir_filePath)
        old_path=PATH_DOWNLOADS / file
        new_path=os.path.join(PATH_DOWNLOADS,dir_name,file)
        shutil.move(old_path,new_path)