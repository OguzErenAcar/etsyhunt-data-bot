import os
import shutil

import pandas as pd


def open_newDir(dir: str, name: str):
    dizin_adi = f"Dataset{dir}/{name}"
    try:
        os.mkdir(dizin_adi)
        print(f"{dizin_adi} adında bir dizin oluşturuldu.")
    except FileExistsError:
        print(f"{dizin_adi} adında bir dizin zaten mevcut.")
    except Exception as e:
        print(f"Dizin oluşturulurken bir hata oluştu: {str(e)}")


def moveDataFile(filepath: str, finalpath: str):
    try:
        # Dosyayı taşı
        shutil.move(filepath, finalpath)
        print(f"{filepath} başarıyla {finalpath} konumuna taşındı.")
    except Exception as e:
        print(f"Taşıma işlemi sırasında bir hata oluştu: {str(e)}")


def changeDataFileName(filepath: str, new_name: str,file_extension:str):
    try:
        # Dosyanın adını değiştir
        new_filepath = os.path.join(os.path.dirname(filepath), new_name + file_extension)
        try:
            os.remove(new_filepath)
            print("silindi ", new_filepath )
        except:
            pass
        os.rename(filepath, new_filepath)

        print(f"{filepath} dosyasının adı {new_name} olarak değiştirildi.")

        return new_filepath  # Yeni dosya yolunu döndür
    except Exception as e:
        print(f"Dosya adı değiştirme sırasında bir hata oluştu: {str(e)}")
        return None


async  def saveData(ProductType: str, Category: str, filename: str):
    open_newDir("/", "Products")
    open_newDir("/Products", f"{ProductType}")
    #open_newDir(f"/Products_AllTime_noLoabel/{ProductType}", f"{Category}")
    moveDataFile(f"/Users/oguz/Downloads/{filename}", f"Dataset/Products/{ProductType}/")
    changeDataFileName(f"Dataset/Products/{ProductType}/{filename}", f"{Category}_{ProductType}",".csv")

def xlsxTocsv(path:str):
    dosya_adi = os.path.splitext(path)[0]
    # CSV dosyasının adını ve yolu
    csv_file_path = dosya_adi+'.csv'

    # XLSX dosyasını bir DataFrame'e yükle
    df = pd.read_excel(path)

    # DataFrame'i CSV dosyasına kaydet
    df.to_csv(csv_file_path, index=False)


def csvToxlsx(path:str):
    # CSV dosyasını oku
    veri = pd.read_csv(path)
    dosyaadi,uzanti=os.path.splitext(path)
    # XLSX dosyasının adı ve yolu
    xlsx_dosya_yolu = dosyaadi+".xlsx"

    # Veriyi XLSX dosyasına yaz
    veri.to_excel(xlsx_dosya_yolu, index=False)
    os.remove(path)

