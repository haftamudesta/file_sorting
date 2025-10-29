import os,shutil
import time
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

def get_file_cat(file_name):  
    if file_name.startswith("_"):
        return None

    filepath = os.path.join(PATH_DOWNLOADS, file_name)
    if os.path.isdir(filepath):
        return "_Folders"  
    else:
        
        if '.' in file_name:
            file_extension = '.' + file_name.split('.')[-1].lower()  
        else:
            file_extension = ''  
        
        for cat, list_keywords in CATEGORIES.items():
            if file_extension in list_keywords:  
                return cat
        return "_Others" 
def sort_downloads():
    all_files = os.listdir(PATH_DOWNLOADS)
    folders = [f for f in all_files if os.path.isdir(os.path.join(PATH_DOWNLOADS, f)) and not f.startswith("_")]
    files = [f for f in all_files if not os.path.isdir(os.path.join(PATH_DOWNLOADS, f))]

    print("*" * 40)
    print("Scanning Downloads Folder...")

    time.sleep(10)
    
    print(f'Folders Found: {len(folders)}')  

    if files:
        print(f'Files Found: {len(files)}') 
        print(f'....... Sorting .......')
    else:
        print(f'Files Found: 0') 
        print(f'Nothing to sort here...')
    for file in os.listdir(PATH_DOWNLOADS):
        dir_name = get_file_cat(file)
        
        if dir_name:
            dir_filePath = os.path.join(PATH_DOWNLOADS, dir_name)
            if not os.path.exists(dir_filePath):
                os.makedirs(dir_filePath)
            old_path = PATH_DOWNLOADS / file
            new_path = os.path.join(PATH_DOWNLOADS, dir_name, file)
            try:
                shutil.move(str(old_path), new_path)  # Fixed: convert Path to string
                print(f'Moved: {file} -> {dir_name}/')
            except Exception as e:
                print(f'{dir_name}/{file} - {e}')
if __name__ == "__main__":
    sort_downloads()