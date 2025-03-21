# 🅰️ Convert TTF fonts to WOFF2

## 📌 Description 

This project is a Python script that converts **TTF** fonts to **WOFF2**, a format that's more optimized for faster website loading. It uses the `fontTools` library to perform the conversion easily and efficiently.

## 📝 Requirements

- Python 3.x
- The **fontTools** library for font manipulation. You can install it using pip:
```bash
pip install fonttools
```
## 🛠️ Technologies Used
- Python

## 📥 Installation

The script performs the following actions:

1. Prompts the user for the path to the folder where the .ttf fonts are located.
2. Checks if the provided path is valid and contains .ttf files.
3. Converts each .ttf file in the folder to .woff2.
4. Deletes the .ttf files after successful conversion.

## 📥 use
1. Make sure you have Python installed on your machine.
2. Install the necessary dependencies:
```bash
pip install fonttools
```
3. Run the script: `python convert_fonts.py`.
4. Enter the path to the folder containing the `.ttf` files when prompted. The script will convert all `.ttf` files in that folder to `.woff2` and delete the original `.ttf` files.
   
### 📟 Output example
  ```bash
  Ingresa la ruta de la carpeta con las fuentes .ttf: /ruta/a/mi/carpeta
  Convertido fuente1.ttf a fuente1.woff2
  Archivo eliminado: fuente1.ttf
  Convertido fuente2.ttf a fuente2.woff2
  Archivo eliminado: fuente2.ttf
```


## 🔍 considerations

- This script only converts .ttf files located in the specified folder.
- The generated .woff2 files are stored in the same folder as the .ttf files.
- The .ttf files are deleted after successful conversion. If you prefer to keep the .ttf files, you can delete or modify the line os.remove(ttf_file) .

## 📝 Contributions

If you'd like to improve this project, any contribution is welcome!

1. Fork the repository.
2. Create a new branch:
```bash
   git checkout -b mi-nueva-funcionalidad
```
3. Make your improvements and commit:
```bash
   git commit -m "Agregada nueva funcionalidad"
```
4.Upgrade the gears:
```bash
  git push origin mi-nueva-funcionalidad
```
5. Create a pull request explaining your changes.
