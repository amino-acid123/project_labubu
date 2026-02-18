"""
This code downloads datasets from online Galaxy.
Input:
 - The Excel file should contain columns 'Source Name', 'New Name', 'Link'
   and optionally 'Subfolder'.
 - Sheet name of Excel file.
 - Full path to directory for download destination (should not end on /).
"""
"""
Цей код завантажує набори даних з онлайн-платформи Galaxy.
Вхідні дані:
 - Excel-файл повинен містити стовпці 'Source Name', 'New Name', 'Link'
   та за потреби 'Subfolder'.
 - Назва аркуша Excel-файлу.
 - Повний шлях до директорії для завантаження (не повинен закінчуватися на /).

"""

import argparse
import os
import subprocess as sb
import pandas as pd
import logging
from datetime import datetime


def main():
    # -----------------------------
    # Parse arguments
    # Розбір аргументів командного рядка
    # -----------------------------
    parser = argparse.ArgumentParser(
        description="Download datasets from online Galaxy"
    )
    parser.add_argument("-f", required=True, help="Excel file with dataset links and names.")
    parser.add_argument("-s", required=True, help="Sheet name.")
    parser.add_argument("-o", required=True, help="Output directory.")

    args = parser.parse_args()

    # -----------------------------
    # Validate output directory
    # Перевірка вихідної директорії
    # -----------------------------
    if not os.path.exists(args.o):
        parser.error(f"{args.o} does not exist")
    if not os.path.isdir(args.o):
        parser.error(f"{args.o} is not a directory")

    data_file = args.f
    sheet_name = args.s
    out_dir = args.o

    # -----------------------------
    # Read Excel file
    # Зчитування Excel-файлу
    # -----------------------------
    data = pd.read_excel(data_file, sheet_name=sheet_name)

    # -----------------------------
    # Check required columns
    # Перевірка наявності обов’язкових стовпців
    # -----------------------------
    expected_columns = ['Source Name', 'New Name', 'Link']
    missing_columns = [col for col in expected_columns if col not in data.columns]

    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

    # -----------------------------
    # Create subfolders if needed
    # Створення підпапок за потреби
    # -----------------------------
    create_subfolders = 'Subfolder' in data.columns

    if create_subfolders:
        subfolders = (
            data.loc[~data['Subfolder'].isna(), 'Subfolder']
            .astype(str)
            .unique()
        )

        print(f"Creating subfolders {', '.join(subfolders)} in {out_dir}")
        for subf in subfolders:
            new_folder = os.path.join(out_dir, subf)
            os.makedirs(new_folder, exist_ok=True)
    else:
        print("Subfolders were not requested.")

    # -----------------------------
    # Setup logging
    # Налаштування логування
    # -----------------------------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(
        out_dir,
        f"download_log_{timestamp}.log"
    )
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    logging.info("Started dataset download")
    logging.info(f"Input file: {data_file}")
    logging.info(f"Sheet name: {sheet_name}")

    # -----------------------------
    # Download datasets
    # Завантаження наборів даних
    # -----------------------------
    data_download = data[
        ~(data['Source Name'].isna() | data['Link'].isna())
    ]

    print(
        f"Table contains {len(data)} rows. "
        f"Start download of {len(data_download)} datasets."
    )

    for _, row in data_download.iterrows():
        dataset_name = (
            row['Source Name']
            if pd.isna(row['New Name'])
            else row['New Name']
        )

        subf = row['Subfolder'] if create_subfolders else ""
        link = row['Link']

        logging.info(
            f"Row {_} | "
            f"Source Name='{row['Source Name']}' | "
            f"New Name='{row['New Name']}' | "
            f"Link='{link}' | "
            f"Subfolder='{subf}'"
        )

        dataset_dir = (
            os.path.join(out_dir, subf)
            if subf
            else out_dir
        )

        try:
            sb.run(
                ["wget", link, "-O", dataset_name],
                cwd=dataset_dir,
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Download succeeded: {dataset_name}")
            logging.info(f"SUCCESS | {dataset_name}")
        except sb.CalledProcessError as e:
            print(f"Download failed for {dataset_name}")
            logging.error(f"FAILED | {dataset_name}")
            print(e.stderr)


if __name__ == "__main__":
    main()
