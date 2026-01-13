# [Українська] Транскриптоміка як навігатор для підвищення відповідності органоїдів до нативних органів

Органоїди - це моделі органів, створені в пробірці. Вони корисні для біомедичних досліджень і випробувань ліків, однак вимагають дуже ретельного розроблення. Цей проєкт має на меті висвітлити проблему невідповідності органоїдів органам і тканинам у сучасних дослідженнях та надати інструменти для її ефективної оцінки та усунення.

_Проект був реалізований в рамках програми ScienceMentoring від YO UkrTeenScience, яка об'єднує наставників із учнями старших класів для поглиблення знань про наукову діяльність._

## Автори (Authors)
- Ангеліна (Angelina @amino-acid123) - виконавиця
- Валерія (Valeriia @vvsbiocode) - керівниця

## Опис репозиторію

| Назва папки | Опис |
|-------------|------|
| workflows | робочі процеси та підпроцеси Galaxy, що використовуються для аналізу необроблених даних секвенування |
| data | приклади вхідних даних для робочих процесів Galaxy |
| notebooks | аналіз даних та візуалізація на виході з робочих процесів Galaxy |

## Як відтворити проект
### Необхідні компоненти
- Обліковий запис у Galaxy https://usegalaxy.org/
- Обліковий запис у Google Colab або Python і Jupyter, встановлені на комп'ютері або сервері
### Інструкції
1. Завантажте один робочий процес і підпроцеси з workflows/ та імпортуйте їх у Galaxy;
2. Завантажте файли референтного геному, перелічені в описі довідки робочого процесу, за допомогою функції Galaxy «Paste/Fetch data» (Вставити/Завантажити дані);
3. Завантажте файл(и) зі списком зразків з data/ для однієї статті та імпортуйте їх у Galaxy;
4. Завантажте зразки за допомогою інструменту Galaxy «Download and Extract Reads in FASTQ» (Завантажити та витягти дані у форматі FASTQ);
5. Запустіть робочий процес у Galaxy, введіть завантажені файли та параметри, перелічені в описі довідки робочого процесу;
6. Запустіть код з notebooks/, налаштувавши шлях до вихідних файлів Galaxy.

## Короткий опис проаналізованих статей

| Номер SRA* | DOI статті | Вид | Орган/тканина | Органоїд |
|---------------|-----------|---------|----------------------|----------|
| SRP561920 | https://doi.org/10.3390/cells14040252 | _Mus musculus_ | ретина | органоїд стовбурових клітин ретини |
| ERP142256 | https://doi.org/10.1186/s13046-022-02591-z | _Homo sapiens_ | колоректальний рак | тумороїд |
| ERP111852 | https://doi.org/10.1016/j.stemcr.2017.11.012 | _Homo sapiens_ | кінчик легеневої бруньки плода | органоїд-попередник легенів плода |

*_Sequence Read Archive (SRA) - база даних необроблених даних секвенування_

# [English] Transcriptomics as navigator towards organoids fidelity

Organoids are the in vitro models of organs. They are useful for biomedical studies and drug tests, however require very careful development. This project aims to highlight the problem of organoids non-fidelity to organs and tissues in modern studies and provide tools to assess and troubleshoot it efficiently.

_The project was done under ScienceMentoring program of YO UkrTeenScience, which connects mentors with high-school students to learn more about science activities._

## Authors
- Angelina @amino-acid123 - executer
- Valeriia @vvsbiocode - supervisor

## Description of repository

| Folder name | Contents |
|-------------|------|
| workflows | The Galaxy workflows and sub workflows used to analyze raw sequencing data |
| data | The input files to Galaxy workflows sorted by articles |
| notebooks | Data analysis and visualization downstream to Galaxy workflows |

## How to reproduce the project
### Dependencies
- Account in Galaxy https://usegalaxy.org/
- Account in Google Colab or Python and Jupyter installed on computer or on server
### Instructions
1. Download one workflow and subworkflows from workflows/ and import them into Galaxy;
2. Download reference genome files, listed in workflow help description, through Galaxy upload of "Paste/Fetch data";
3. Download sample list file(s) from data/ for one paper and import them into Galaxy;
4. Download samples with Galaxy tool "Download and Extract Reads in FASTQ";
5. Run the workflow in Galaxy, input downloaded files and parameters listed in workflow help description;
6. Run code from notebooks/ adjusting Galaxy output files path.

## Short description of analyzed papers

| SRA* accession | Paper DOI | Species | Organ/ tissue | Organoid |
|---------------|-----------|---------|----------------------|----------|
| SRP561920 | https://doi.org/10.3390/cells14040252 | _Mus musculus_ | retina | retina stem cells organoid |
| ERP142256 | https://doi.org/10.1186/s13046-022-02591-z | _Homo sapiens_ | colorectal cancer | tumoroid |
| ERP111852 | https://doi.org/10.1016/j.stemcr.2017.11.012 | _Homo sapiens_ | isolated fetal lung buds | fetal lung progenitor organoid |

*_Sequence Read Archive (SRA) - database of raw sequencing data_

