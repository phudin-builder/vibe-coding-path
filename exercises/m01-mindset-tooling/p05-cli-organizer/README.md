# Downloads Organizer (Python)

Script Python đơn giản để tự động phân loại file trong thư mục `Downloads` theo phần mở rộng (extension).

## Muc tieu

- Giu thu muc `Downloads` gon gang, de tim file hon.
- Tu dong tao cac thu muc danh muc neu chua ton tai.
- Di chuyen file vao dung nhom dua tren extension.

## Tinh nang hien tai

- Nhom `Installers`: `.exe`, `.msi`, `.pkg`, `.dmg`, `.whl`, `.msix`, `.deb`
- Nhom `Zip Files`: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.tgz`, `.tar.xz`
- Nhom `Documents`: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`, `.ics`, `.html`
- Nhom `Images`: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.heic`, `.webp`, `.jfif`
- Nhom `Video`: `.mp4`, `.mov`, `.avi`, `.iso`
- Nhom `Code`: `.py`, `.tsx`, `.json`, `.js`, `.ipynb`, `.pt`, `.winmd`, `.jar`

Luu y:
- Script co xu ly rieng `.tar.xz` de phan loai dung.
- File khong khop extension nao se duoc giu nguyen tai cho.

## Cau truc du an

```text
Exercies_M1P5/
|- organizer.py
|- README.md
|- requirements.txt
`- .gitignore
```

## Yeu cau he thong

- Python 3.10+ (khuyen nghi 3.12)
- Khong can thu vien ben thu 3 (chi dung `os`, `shutil` cua Python standard library)

## Cai dat

```powershell
cd E:\Cursor\Exercies_M1P5
python --version
```

Neu may ban dung Python launcher:

```powershell
py --version
```

## Cach chay

Tu thu muc du an:

```powershell
python organizer.py
```

hoac:

```powershell
py organizer.py
```

## Ket qua sau khi chay

Trong `Downloads`, script se tao (neu chua co):

- `Installers`
- `Zip Files`
- `Documents`
- `Images`
- `Video`
- `Code`

Va in log ra terminal:

- `Moved: <filename> -> <folder>/`
- `Failed to move <filename>: <error>`

## Tuy chinh nhanh

Ban co the sua map extension trong `organizer.py`:

- Bien `EXTENSION_MAP` de them/bot extension.
- Tham so `download_dir` trong ham `organize_downloads(...)` de test voi thu muc khac.

Vi du goi ham voi thu muc test:

```python
organize_downloads(download_dir=r"E:\Cursor\test_downloads")
```

## Huong dan debug co ban

1. Dat breakpoint tai:
   - Dau ham `organize_downloads`
   - Dong lay `ext = os.path.splitext(...)`
   - Dong `shutil.move(...)`
2. Chay debug bang `F5`.
3. Theo doi bien:
   - `filename`, `ext`, `dest_dir`, `new_path`
4. Dung `F10` de step qua tung dong.

## Loi thuong gap

- `python is not recognized`: Python chua cai hoac chua add PATH.
- `PermissionError`: file dang duoc mo boi ung dung khac.
- File khong duoc di chuyen: extension khong nam trong `EXTENSION_MAP`.

## Bao mat va an toan du lieu

- Nen test truoc voi mot thu muc mau.
- Khong nen chay truc tiep lan dau tren `Downloads` neu co du lieu quan trong.

## Huong phat trien tiep

- Xu ly file trung ten (tu dong doi ten).
- Them che do dry-run (chi in du kien, khong move file).
- Them logging ra file.
- Them unit test.

