import os
import csv
import cv2
import pathlib, subprocess
from pyzbar.pyzbar import decode
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()

def unpack_file(file: str, name: str):
    """
    Unpack zip file to a folder
    file: path to the zip file
    name: name of the folder to be created
    return: None
    """
    # Criar pasta ramais
    pathlib.Path(f'./automate_prov/ramais/{name}').mkdir(parents=True, exist_ok=True)

    # exportar zip file para pasta ramais
    subprocess.run(['unzip', file, '-d', f'./automate_prov/ramais/{name}'])


def get_images(folder_name: str) -> list:
    """
    Get all images from a folder
    folder_name: name to the folder containing the images
    return: list of images
    """
    # Loop para identificar os ramais no diretorio.
    folder = []
    for filename in os.listdir(folder_name):
        # Verificar se é um arquivo de imagem. 
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            # Adiciona em uma lista
            folder.append(filename)
    # Retorna a lista com os ramais. 
    return folder


def get_barcode(path, name):
    """
    Get the barcode from an image
    path: path to the image
    name: name of the image
    return: dictionary with the results
    """
    path_image = path
        
    # Faz a leitura da imagem 
    img = cv2.imread(path_image)

    # Decodifica a imagem
    detectedBarcodes = decode(img) 
    result = {name: {'serial': None, 'mac': None}}
    # Faz a busca pelo codigo de barras.
    if not detectedBarcodes: 
        print("Barcode Not Detected or your barcode is blank/corrupted!") 
    else: 
      for barcode in detectedBarcodes:   
        (x, y, w, h) = barcode.rect 
        cv2.rectangle(img, (x-10, y-10), 
                    (x + w+10, y + h+10),  
                    (255, 0, 0), 2) 
        if barcode.data!="":
            if len(barcode.data.decode()) == 16:
                result[name]['serial'] = barcode.data.decode()
            elif len(barcode.data.decode()) == 12:
                result[name]['mac'] = barcode.data.decode()

    # # Abre a imagem para validar. 
    # cv2.imshow('Image', img) 
    # # Aguarda o usuario precionar uma tecla e destroi a imagem. 
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows() 

    # Retorna o dicionario.
    return result


def export_csv(results: dict, folder_path: str):
    """
    Export the results to a CSV file
    results: dictionary with the results
    folder_path: path to the folder containing the images
    return: None
    """
    # Salva o resultado em um CSV
    csv_path = os.path.join(folder_path, f'{os.path.basename(folder_path)}.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['ramal', 'serial', 'mac']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in results.keys():
            serial = results[key]['serial']
            mac = results[key]['mac']
            writer.writerow({'ramal': key, 'serial': serial, 'mac': mac})

def print_table(dict):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Ramal", style="dim", width=5)
    table.add_column("Serial", style="dim", width=17)
    table.add_column("MAC", style="dim", width=13)
    for key in dict.keys():
        serial = dict[key]['serial']
        mac = dict[key]['mac']
        table.add_row(key, serial, mac) 
    console.print(table)

@app.command()
def main(name: str, file: str):
    """
    Main function
    name: name of the folder to be created
    file: path to the zip file
    return: None
    """
    unpack_file(file, name)
    folder_path = f'automate_prov/ramais/{name}'
    images = get_images(folder_path)
    results = {}
    for ext in images:
        path = os.path.join(folder_path, ext)
        name = os.path.splitext(ext)[0]
        results.update(get_barcode(path, name))
    export_csv(results, folder_path)
    print_table(results)


if __name__ == "__main__": 
    app()

    

# Path: automate_prov/backend/server/main.py
# reference: https://acervolima.com/como-fazer-um-leitor-de-codigo-de-barras-em-python/#:~:text=pyzbar%20Fornece%20o%20m%C3%A9todo%20rect%20para%20localizar%20o,v%C3%A1rios%20c%C3%B3digos%20de%20barras%20inclu%C3%ADdos%20em%20uma%20imagem.
