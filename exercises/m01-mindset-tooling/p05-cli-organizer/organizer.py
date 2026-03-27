import os
import shutil

# Cập nhật map extension với các định dạng mới
EXTENSION_MAP = {
    'Installers': [
        '.exe', '.msi', '.pkg', '.dmg', '.whl', '.msix', '.deb'
    ],
    'Zip Files': [
        '.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.tar.xz'
    ],
    'Documents': [
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
        '.txt', '.ics', '.html'
    ],
    'Images': [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic',
        '.webp', '.jfif'
    ],
    'Video': [
        '.mp4', '.mov', '.avi', '.iso'
    ],
    'Code': [
        '.py', '.tsx', '.json', '.js', '.ipynb', '.pt', '.winmd', '.jar'
    ],
}

DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

def organize_downloads(download_dir=DOWNLOADS_DIR, extension_map=EXTENSION_MAP):
    # Tạo các thư mục đích
    for folder in extension_map.keys():
        dest = os.path.join(download_dir, folder)
        if not os.path.isdir(dest):
            os.makedirs(dest, exist_ok=True)

    # Quét thư mục Downloads
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            # Handle .tar.xz specifically since os.path.splitext splits just .xz
            if filename.lower().endswith('.tar.xz'):
                ext = '.tar.xz'
            # Xác định thư mục chứa file dựa trên extension
            for folder_name, ext_list in extension_map.items():
                if ext in ext_list:
                    dest_dir = os.path.join(download_dir, folder_name)
                    new_path = os.path.join(dest_dir, filename)
                    try:
                        shutil.move(file_path, new_path)
                        print(f"Moved: {filename} -> {folder_name}/")
                    except Exception as e:
                        print(f"Failed to move {filename}: {e}")
                    break

if __name__ == "__main__":
    organize_downloads()