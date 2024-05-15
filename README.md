# Detekcia glaukómu pomocou strojového učenia

Cieľom tohto projektu je detekcia glaukómu pomocou techník strojového učenia. V poskytnutej používateľskej príručke sú uvedené kroky na využitie súboru údajov, požadované knižnice a proces implemetácie.

## Dataset

- [ORIGA, G1020 (Orezané fundus obrazy)](https://www.kaggle.com/datasets/arnavjain1/glaucoma-datasets)
- [RIM-ONE, ACRIMA (Orezané fundus obrazy)](https://www.kaggle.com/datasets/ayush02102001/glaucoma-classification-datasets)
- [Celé fundus obrazy](https://www.kaggle.com/code/banddaniel/glaucoma-classification-w-vit-f1-score-0-91/input)

| Dataset (orezané) | Zdravé (normal) | Glaukóm (glaucoma) |
|-------------------|-----------------|-------------------|
| ACRIMA            | 309             | 396 |
| ORIGA             | 482             | 168 |
| G1020             | 724             | 296 |
| RIM-ONE           | 313             | 172 |
| Spolu             | 1828            | 1032 |

| Dataset (celé) | Zdravé (normal) | Glaukóm (glaucoma) |
|----------------|-----------------|--------------------|
| BEH            | 108             | 46                 |
| DRISTHI-GS1    | 12              | 15                 |
| FIVES          | 56              | 40                 |
| G1020          | 177             | 68                 |
| JSIEC          | 8               | 3                  |
| EyePACS        | 2               | 767                |
| CRFO           | 4               | 9                  |
| LES-AV         | 4               | 3                  |
| OIA-ODIR       | 969             | 69                 |
| ORIGA          | 111             | 37                 |
| PAPILA         | 66              | 18                 |
| HRF            | 168             | 20                 |
| REFUGE         | 69              | 25                 |
| Spolu          | 1754            | 1120               |

## Požiadavky a inicializácia

Uistite sa, že máte nainštalované nasledujúce knižnice Pythonu:

- os
  - `pip install os`
- shutil
  - `pip install shutil`
- pandas
  - `pip install pandas`
- opencv
  - `pip install opencv-python`
- sklearn
  - `pip install scikit-learn`
- skimage
  - `pip install scikit-image`
- numpy
  - `pip install numpy`
- matplotlib
  - `pip install matplotlib`
- seaborn
  - `pip install seaborn`
- pathlib
  - `pip install pathlib`
- tensorflow
  - `pip install tensorflow`
- PIL
  - `pip install Pillow`
- tqdm
  - `pip install tqdm`
- jupyter server
  - `pip install jupyter-server`

## Implementácia

1. **Priradenie správnych označení**
   - Použite skript `assign_labels.py`.
   - Uveďte tri cesty:
     - `image_folder` - cesta k priečinku so zdrojovým obrázkom
     - `csv_file` - Zdrojový súbor CSV
     - `out_folder` - výstupná cesta
   - Algoritmus vytvorí dva podpriečinky: `glaucoma` a `normal`, pričom obrázky priradí podľa štítku CSV (0: normálny, 1: glaukóm).

2. **Predspracovanie**
   - Spustite skript `preprocessing_clahe.ipynb`.
   - `dir` - zdrojová cesta, cesta k predtým vytvorenému adresáru s rozdelenými podpriečinkami (`glaucoma` a `normal`).
   - `apply_clahe` -  Názov výstupného adresára ako druhý argument pre metódu `apply_clahe()` .
   - Obrázky s aplikovanými krokmi predspracovania sa uložia do výstupného adresára.

3. **Klasifikácia pomocou extrakcie príznakov použitím ResNet50 (Metóda 1)**
   - Využite skript na klasifikáciu `classification_model_full_fundus.ipynb` pre celé obrazy.
   - Využite skript na klasifikáciu `classification_model_cropped_fundus.ipynb` pre orezané obrazy.
   - `train_dir` - cesta k predspracovanému adresáru.
   - Algoritmus skontroluje, či je súbor údajov vyvážený, ak nie, vytvorí vyvážený súbor údajov.
   - Extrakcia príznakov sa vykonáva pomocou predtrénovaného ResNet50.
   - V prípade potreby sa na zníženie dimenzionality použije PCA (Principal component analysis).
   - Trénovacia a testovacia množina sa rozdelia v pomere `80 %` ku `20 %`.
   - Klasifikácia sa vykonáva pomocou algoritmov strojového učenia: SVM, Random Forest, logistická regresia, KNN a AdaBoost.

4. **Klasifikácia pomocou extrakcie príznakov použitím GLCM (Metóda 2)**
   - Využite skript na klasifikáciu `grey_level_matrix_classification.ipynb`.
   - `train_dir` - cesta k predspracovanému adresáru.
   - Algoritmus skontroluje, či je súbor údajov vyvážený, ak nie, vytvorí vyvážený súbor údajov.
   - Zo vstupných obrázkov sa extrahujú príznaky pomocou GLCM (matica koincidencie úrovní sivej), ako sú `kontrast`, `energia`, `homogenita` a `korelácia`.
   - V prípade potreby sa na zníženie dimenzionality použije PCA (Principal component analysis).
   - Trénovacia a testovacia množina sa rozdelia v pomere 80 % ku 20 %.
   - Klasifikácia sa vykonáva pomocou algoritmov strojového učenia: SVM, Random Forest, logistická regresia, kNN a AdaBoost.
   
5. **Vyhodnotenie**
   - Vypočítavajú sa hodnotiace ukazovatele vrátane `presnosti` (accuracy), `precíznosti` (precision), `citlivosti` (sensitivity), `F1-skóre` (f1-score) a `ROC-AUC`.
   - Na vizualizáciu sú vykreslené konfúzne matice.

**Metóda 1 - výsledky**

| Model               | Presnosť (%) | Precíznosť (%) | Citlivosť (%) | F1-skóre (%) |
|---------------------|---------------|---------------|---------------|---------------|
| SVM                 | 93,25           | 93,28           |93,21           |93,24           |
| Random forest       | 91,12           | 91,20           |91,22           |91,12           |
| Logistická regresia | 78,87           | 78,96           |78,97           |78,87           |
| KNN                 | 91           | 91,16           |91,13           |91           |
| AdaBoost            | 91,38          | 91,61          |91,53           |91,37           |

**Metóda 2 - výsledky**

| Model               | Presnosť (%) | Precíznosť (%) | Citlivosť (%) | F1-skóre (%) |
|---------------------|---------------|--------------|--------------|-----------|
| SVM                 | 68,62           | 69,23           |68,48         |68,27       |
| Random forest       | 74,12         | 75,15         |73,93        |73,77      |
| Logistická regresia | 56,75         | 56,73         |56,72        |56,72        |
| KNN                 | 73,5        | 73,73          |73,42         |73,39       |
| AdaBoost            | 74,12          | 74,90         |73,99         |73,84     |


Dodržiavaním týchto krokov môžete efektívne využívať model strojového učenia na detekciu glaukómu.