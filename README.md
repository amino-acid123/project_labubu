# [Українська] Транскриптоміка як навігатор для підвищення відповідності органоїдів до нативних органів

Органоїди - це моделі органів, створені в пробірці. Вони корисні для біомедичних досліджень і випробувань ліків, однак вимагають дуже ретельного розроблення. Цей проєкт має на меті висвітлити проблему невідповідності органоїдів органам і тканинам у сучасних дослідженнях та надати інструменти для її ефективної оцінки та усунення.

~Проект був реалізований в рамках програми ScienceMentoring від YO UkrTeenScience, яка об'єднує наставників із учнями середніх шкіл для поглиблення знань про наукову діяльність.~

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
- Завантажте один робочий процес і підпроцеси з workflows/ та імпортуйте їх у Galaxy;
- Завантажте файли референтного геному, перелічені в описі довідки робочого процесу, за допомогою функції Galaxy «Paste/Fetch data» (Вставити/Завантажити дані);
- Завантажте файл(и) зі списком зразків з data/ для однієї статті та імпортуйте їх у Galaxy;
- Завантажте зразки за допомогою інструменту Galaxy «Download and Extract Reads in FASTQ» (Завантажити та витягти дані у форматі FASTQ);
- Запустіть робочий процес у Galaxy, введіть завантажені файли та параметри, перелічені в описі довідки робочого процесу;
- Запустіть код з notebooks/, налаштувавши шлях до вихідних файлів Galaxy.

## Короткий опис проаналізованих статей
...

# [English] Transcriptomics as navigator towards organoids fidelity

Organoids are the in vitro models of organs. They are useful for biomedical studies and drug tests, however require very careful development. This project aims to highlight the problem of organoids non-fidelity to organs and tissues in modern studies and provide tools to assess and troubleshoot it efficiently.

~The project was done under ScienceMentoring program of YO UkrTeenScience, which connects mentors with high-school students to learn more about science activities.~

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
- Download one workflow and subworkflows from workflows/ and import them into Galaxy;
- Download reference genome files, listed in workflow help description, through Galaxy upload of "Paste/Fetch data";
- Download sample list file(s) from data/ for one paper and import them into Galaxy;
- Download samples with Galaxy tool "Download and Extract Reads in FASTQ";
- Run the workflow in Galaxy, input downloaded files and parameters listed in workflow help description;
- Run code from notebooks/ adjusting Galaxy output files path.

## Short description of analyzed papers

TBA

