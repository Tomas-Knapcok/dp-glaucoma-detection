import os
import shutil
import pandas as pd


def create_folders_and_copy_images(csv_file, image_folder, output_folder):
    """
    Vytvorenie priečinkov na základe labelov a príslušné kopírovanie obrázkov zo súboru CSV do výstupného adresára.

    Args:
     - csv_file (str): Cesta k súboru CSV, ktorý obsahuje názvy súborov s obrázkami a lable.
     - image_folder (str): Adresár obsahujúci pôvodné obrázky.
     - output_folder (str): Adresár na uloženie skopírovaných obrázkov.

    Returns:
    None
    """

    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        image_id = row['Filename']
        label = row['Glaucoma']

        label_folder = os.path.join(output_folder, str(label))
        if not os.path.exists(label_folder):
            os.makedirs(label_folder)

        source_path = os.path.join(image_folder, image_id)
        destination_path = os.path.join(label_folder, image_id)
        shutil.copy(source_path, destination_path)


def main():
    # CSV pre aktuálny dataset
    csv_file = "3-in-1/ORIGA/OrigaList.csv"
    # Cesta k priečinku s fundus snímkami
    image_folder = "3-in-glaucoma/ORIGA/Images_Cropped"
    # Nový priečinok, ktorý obsahuje 2 podpriečinky normal a glaucoma
    out_folder = "ORIGA"
    create_folders_and_copy_images(csv_file, image_folder, out_folder)


if __name__ == "__main__":
    main()
