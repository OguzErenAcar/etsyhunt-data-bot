import asyncio
import glob
import os
import time
from time import sleep

from download_dataset import export, isDownload
from edit_datafiles import open_newDir, moveDataFile, changeDataFileName, saveData, xlsxTocsv, csvToxlsx
from parse_etsy import select_Country, select_ProductType, select_Category, unselect_ProductType, select_label, \
    select_time
from start_etsy import open_etsy


def main():
    Catagories = [
        "Home & Living",
        "Craft Supplies & Tools",
        "Jewelry",
        "Art & Collectibles",
        "Clothing",
        "Paper & Party Supplies",
        "Accessories",
        "Bath & Beauty",
        "Weddings",
        "Bags & Purses",
        "Toys & Games",
        "Books, Movies & Music",
        "Electronics & Accessories",
        "Pet Supplies",
        "Shoes"]

    ProductTypes = [
        "Handmade",
        "Vintage",
        "Digital",
        "Customizable",
        "Others",
        "Select All"
    ]

    Country = "United States"
    driver = open_etsy(giris=True, url="https://etsyhunt.com/etsy-product-research")
    select_label(driver, "BestSeller")
    sleep(1)
    select_time(driver, "1 Year")
    sleep(1)
    select_Country(driver, Country)
    sleep(1)
    for Category in Catagories:
        select_Category(driver, Category)
        sleep(2)
        for ProductType in ProductTypes:
            baslangic_zamani = time.time()
            if (ProductType != ProductTypes[0]):
                unselect_ProductType(driver, ProductType)
            sleep(2)
            select_ProductType(driver, ProductType)
            sleep(3)
            DownloadUrl = "/Users/oguz/Downloads"
            initial_file_count = len(os.listdir(DownloadUrl))
            export(driver, "All Page")
            isDownload_ = isDownload(driver,initial_file_count, 1)
            if (isDownload_):
                dosya_listesi = glob.glob(os.path.join(DownloadUrl, "*"))
                en_son_dosya = max(dosya_listesi, key=os.path.getctime)
                fileName = os.path.basename(en_son_dosya)
                asyncio.run(saveData(ProductType, Category, fileName))
            else:
                print(f"data yok :{Category}_{ProductType}")
            bitis_zamani = time.time()
            sure = bitis_zamani - baslangic_zamani
            print(f"{sure}sn sürdü")



def util():
    dir = "Dataset/Products_30Days_BestSeller"
    list =os.listdir(dir)
    for category in list:
        print(category,"-----")
        try:
            categorydir=os.listdir(dir+"/"+category)
            for item in categorydir:
                    dosya_adi,uzanti = os.path.splitext(item)  # CSV uzantısını kaldır
                    print(dosya_adi)
                    if not dosya_adi.startswith("~") and uzanti==".csv":
                        print(item)
                        try:
                            csvToxlsx(f"{dir}/{category}/{item}")
                        except:
                            try:
                                changeDataFileName(f"{dir}/{category}/{item}", dosya_adi, ".xlsx")
                            except:
                                break
                        xlsxTocsv(f"{dir}/{category}/{dosya_adi}.xlsx")
                        os.remove(f"{dir}/{category}/{dosya_adi}.xlsx")
        except:
            pass



if __name__ == '__main__':
    main()
