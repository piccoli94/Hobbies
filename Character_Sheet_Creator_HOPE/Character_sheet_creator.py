import tkinter as tk
import csv
import os
import re
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName
import pdfrw as pdfrw
import math
# Funzione per chiudere la prima finestra e aprire la seconda
def apri_seconda_finestra(nome):
    root.destroy()  # Chiude la prima finestra
    character_sheet.append(nome)
    seconda_finestra(nome)

# Funzione per chiudere la seconda finestra e aprire la terza
def apri_terza_finestra():
    quasi_seconda_root.destroy()  # Chiude la seconda finestra
    terza_finestra()

def apri_quarta_finestra(nome):
    third_root.destroy()
    character_sheet.append(nome)
    quarta_finestra(nome)

def apri_quasi_terza_finestra(nome):
    seconda_root.destroy()
    quasi_terza_finestra(nome)


# Prima finestra
def prima_finestra():
    global root

    istart = 0
    iend = len(nuovo_dizionario.keys()) // 2

    root = tk.Tk()
    root.title("Prima Finestra")

    label = tk.Label(root, text="Questa è la prima finestra")
    label.pack(pady=20)


    for nome in list(nuovo_dizionario.keys())[int(istart):int(iend)]:
        checkbutton = tk.Button(root, text=nome, command=lambda n=nome: apri_seconda_finestra(n))
        checkbutton.pack(pady=5)

    
    #ok_button = tk.Button(root, text="OK", command=apri_seconda_finestra)
    #ok_button.pack(pady=20)

    root.mainloop()

# Seconda finestra
def seconda_finestra(nome):
    global seconda_root
    seconda_root = tk.Tk()
    seconda_root.title("Seconda Finestra")

    label = tk.Label(seconda_root, text="Seleziona le abilità")
    label.pack(pady=20)
    opzioni=nuovo_dizionario[nome]
    variabili_opzioni = []

    for opzione in opzioni[:-1]:
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(seconda_root, text=opzione, variable=var)
        checkbutton.pack(pady=5)
        variabili_opzioni.append(var)

    def check():
        selezioni = []
        
        flag_abilita_unica = False
        for i, var in enumerate(variabili_opzioni):
            if i == 0 and var.get() != 1:
                flag_abilita_unica = True
            
            if var.get() == 1:
                selezioni.append(opzioni[i])      

        if (len(selezioni) > 4):
            errore_label.config(text="Devi selezionare solo 4 abilità! Di cui una unica")
            return

        if (len(selezioni) < 4):
            errore_label.config(text="Devi selezionare ancora "+str(4-len(selezioni))+" abilità tra cui una unica")
            return

        if (len(selezioni) == 4 and flag_abilita_unica):
            errore_label.config(text="Devi selezionare una abilità unica!")
            return
        
        print(f"Hai selezionato: {selezioni}")
        character_sheet.append(selezioni)
        apri_quasi_terza_finestra(nome)

    ok_button = tk.Button(seconda_root, text="OK", command=check)
    ok_button.pack(pady=20)

    errore_label = tk.Label(seconda_root, text="", fg="red")
    errore_label.pack(pady=5)

    seconda_root.mainloop()


def quasi_terza_finestra(nome):
    global quasi_seconda_root
    quasi_seconda_root = tk.Tk()
    quasi_seconda_root.title("Seconda Finestra")

    label = tk.Label(quasi_seconda_root, text="Seleziona le abilità")
    label.pack(pady=20)
    opzioni=nuovo_dizionario[nome][-1].split("-")
    variabili_opzioni = []

    for opzione in opzioni:
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(quasi_seconda_root, text=opzione, variable=var)
        checkbutton.pack(pady=5)
        variabili_opzioni.append(var)

    def check():
        selezioni = []
        for i, var in enumerate(variabili_opzioni):
          
            if var.get() == 1:
                selezioni.append(opzioni[i])      

        if (len(selezioni) > 2):
            errore_label.config(text="Devi selezionare solo 2 oggetti!")
            return

        if (len(selezioni) < 2):
            errore_label.config(text="Devi selezionare ancora "+str(2-len(selezioni))+" oggetti")
            return
        
        print(f"Hai selezionato: {selezioni}")
        character_sheet.append(selezioni)
        apri_terza_finestra()

    ok_button = tk.Button(quasi_seconda_root, text="OK", command=check)
    ok_button.pack(pady=20)

    errore_label = tk.Label(quasi_seconda_root, text="", fg="red")
    errore_label.pack(pady=5)

    quasi_seconda_root.mainloop()


# Terza finestra
def terza_finestra():

    global third_root
    third_root = tk.Tk()
    third_root.title("Terza Finestra")

    label = tk.Label(third_root, text="Questa è la terza finestra")
    label.pack(pady=20)


    istart = len(nuovo_dizionario.keys()) // 2 
    iend = len(nuovo_dizionario.keys())

    for nome in list(nuovo_dizionario.keys())[int(istart):int(iend)]:
        checkbutton = tk.Button(third_root, text=nome, command=lambda n=nome: apri_quarta_finestra(n))
        checkbutton.pack(pady=5)

    third_root.mainloop()

def quarta_finestra(nome):
    global quarta_root
    quarta_root = tk.Tk()
    quarta_root.title("Quarta Finestra")

    label = tk.Label(quarta_root, text="Seleziona le abilità")
    label.pack(pady=20)
    opzioni=nuovo_dizionario[nome]
    variabili_opzioni = []

    for opzione in opzioni:
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(quarta_root, text=opzione, variable=var)
        checkbutton.pack(pady=5)
        variabili_opzioni.append(var)
        
    def check():
        selezioni = []
        
        flag_abilita_unica = False
        for i, var in enumerate(variabili_opzioni):
            if i == 0 and var.get() != 1:
                flag_abilita_unica = True
            
            if var.get() == 1:
                selezioni.append(opzioni[i])      

        if (len(selezioni) > 3):
            errore_label.config(text="Devi selezionare solo 3 abilità! Di cui una unica")
            return

        if (len(selezioni) < 3):
            errore_label.config(text="Devi selezionare ancora "+str(3-len(selezioni))+" abilità tra cui una unica")
            return

        if (len(selezioni) == 3 and flag_abilita_unica):
            errore_label.config(text="Devi selezionare una abilità unica!")
            return

        print(f"Hai selezionato: {selezioni}")
        character_sheet.append(selezioni)
        quarta_root.destroy()

    ok_button = tk.Button(quarta_root, text="OK", command=check)
    ok_button.pack(pady=20)

    errore_label = tk.Label(quarta_root, text="", fg="red")
    errore_label.pack(pady=5)

    quarta_root.mainloop()



def read_matching_files(csv_path, config_folder):
    if not os.path.exists(config_folder):
        print(f"La cartella {config_folder} non esiste.")
        return {}

    if not os.path.exists(csv_path):
        print(f"Il file CSV {csv_path} non esiste.")
        return {}

    nomi = []
    try:
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row:
                    nomi.append(row[0])
    except Exception as e:
        print(f"Errore nella lettura del file CSV: {e}")
        return {}

    print(f"Nomi trovati nel CSV: {nomi}")

    risultati = {}
    for nome in nomi:
        file_path = os.path.join(config_folder, f"{nome}.txt")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    contenuto = file.read()
                    risultati[nome] = contenuto
                    print(f"Letto il file: {file_path}")
            except Exception as e:
                print(f"Errore nella lettura del file {file_path}: {e}")
        else:
            print(f"File {file_path} non trovato.")
    
    return risultati

def estrai_blocchi_simboli(risultati):
    nuovo_dizionario = {}

    for nome, contenuto in risultati.items():
        pattern = r"(★|❖|Equipaggiamento di base)(.*?)(?=(★|❖|Equipaggiamento di base|Abilità di specializzazione|$))"        
        blocchi = re.findall(pattern, contenuto, re.DOTALL)

        blocchi_estratti = [bloc[0] + bloc[1].strip() for bloc in blocchi]
        
        nuovo_dizionario[nome] = blocchi_estratti

    return nuovo_dizionario

def print_sheet(character_sheet):
    try:
        with open(txt_path, 'w', encoding='utf-8') as file:
            file.write(f"{character_sheet[0]}\n\n")
            file.write("Classi\n\n")
            file.write(f"{character_sheet[1]}, {character_sheet[4]}\n\n")
            file.write("Abilità Unica:\n\n")
            file.write(f"{character_sheet[2][0]}\n\n")
            file.write(f"{character_sheet[5][0]}\n\n")
            file.write("Abilità Scelte:\n\n")
            lista_abilita = [character_sheet[2][1:],character_sheet[5][1:]]
            for element in lista_abilita:
                for abilita in element:
                    file.write(f"{abilita}\n\n")
            file.write("Equipaggiamento:\n\n") 
            for equipaggiamento in character_sheet[3]:
                file.write(f"{equipaggiamento}\n")         

    except FileNotFoundError:
        print('{file_path} not found')
    except Exception as e:
        print('An error occurred: {e}')    
    
# Nuova funzione per l'interfaccia di input del nome
def input_nome():
    def salva_nome():
        nome = entry.get()
        character_sheet.append(nome)
        input_root.destroy()
        prima_finestra()

    input_root = tk.Tk()
    input_root.title("Inserisci Nome")

    label = tk.Label(input_root, text="Inserisci il tuo nome:")
    label.pack(pady=20)

    entry = tk.Entry(input_root)
    entry.pack(pady=10)

    save_button = tk.Button(input_root, text="Salva", command=salva_nome)
    save_button.pack(pady=20)

    input_root.mainloop()

def read_dizionario(csv_path):
    if not os.path.exists(csv_path):
        print(f"Il file CSV {csv_path} non esiste.")
        return {}   
     
    convertitore = {}
    try:
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row:
                    convertitore[row[0]]=row[1]
    except Exception as e:
        print(f"Errore nella lettura del file CSV: {e}")
        return {}

    return convertitore

def get_max_chars_in_box(box_width, char_width):
    # Calculate the maximum number of characters that fit in the box
    max_chars = int(box_width / char_width)
    return max_chars

def print_pdf(dizionario_pdf_code, input_pdf_path, output_pdf_path, character_sheet):
    template_pdf = PdfReader(input_pdf_path)
    for key in dizionario_pdf_code.keys():
        dizionario_pdf_code[key] = ""

    dizionario_pdf_code['(Text1)'] = character_sheet[0]
    dizionario_pdf_code['(Text3)'] = character_sheet[3][0]
    dizionario_pdf_code['(eq2)'] = character_sheet[3][1]
    dizionario_pdf_code['(comp)'] = character_sheet[1]
    dizionario_pdf_code['(esp)'] = character_sheet[4]

    # Define the box width and average character width
    box_width = 150  # Example box width in points
    char_width = 1  # Increased average character width in points (approximation)

    # Calculate the maximum number of characters that fit in the box
    max_len = get_max_chars_in_box(box_width, char_width)
    len_str=len(character_sheet[2][0])
    num_row=int(math.ceil(len_str/max_len))
    mid_line=int(len(character_sheet[2][0])/2)
    if num_row<=1:
        dizionario_pdf_code['(r1)'] = character_sheet[2][0]
    elif num_row>1:
        dizionario_pdf_code['(r1)'] = character_sheet[2][0][:mid_line]
        dizionario_pdf_code['(r2)'] = (character_sheet[2][0])[mid_line:]

#    if len(character_sheet[2][0]) < max_len:
#        dizionario_pdf_code['(r1)'] = character_sheet[2][0]
#    else:
#        dizionario_pdf_code['(r1)'] = (character_sheet[2][0])[:max_len]
#        dizionario_pdf_code['(r2)'] = (character_sheet[2][0])[max_len:]

    num_row=int(math.ceil(len(character_sheet[5][0])/max_len))
    len_str=len(character_sheet[5][0])
    mid_line=int(len_str/2)
    if num_row<=1:
        dizionario_pdf_code['(r11)'] = character_sheet[5][0]
    elif num_row>1:
        dizionario_pdf_code['(r11)'] = character_sheet[5][0][:mid_line]
        dizionario_pdf_code['(r12)'] = (character_sheet[5][0])[mid_line:]

#    if len(character_sheet[5][0]) < max_len:
#        dizionario_pdf_code['(r11)'] = character_sheet[5][0]
#    else:
#        dizionario_pdf_code['(r11)'] = (character_sheet[5][0])[:max_len]
#        dizionario_pdf_code['(r12)'] = (character_sheet[5][0])[max_len:]
    num_row=0
    for i in range(1,4):
        len_str=len(character_sheet[2][i])
        tmp=int(math.ceil(len_str/max_len))
        num_row+=tmp

    iter = [(1, 4), (2, 6), (3, 8)] 
       
    if num_row>8:

        for i, j in iter:
            k = j - 1
            if len(character_sheet[2][i]) < max_len:
                dizionario_pdf_code[f'(r{k})'] = character_sheet[2][i]
            else:
                dizionario_pdf_code[f'(r{k})'] = (character_sheet[2][i])[:max_len]
                dizionario_pdf_code[f'(r{j})'] = (character_sheet[2][i])[max_len:]
    else:
        k=3
        for i in range(1,4):
                num_row=int(math.ceil(len(character_sheet[2][i])/max_len))
                for j in range(1,num_row+1):
                    if j==(num_row+1):
                        dizionario_pdf_code[f'(r{k})'] = character_sheet[2][i][(j-1)*max_len:]
                    else:
                        dizionario_pdf_code[f'(r{k})'] = character_sheet[2][i][(j-1)*max_len:j*max_len]
                    k+=1

    num_row=0
    for i in range(1,3):
        len_str=len(character_sheet[5][i])
        tmp=int(math.ceil(len_str/max_len))
        num_row+=tmp

    iter = [(1, 14), (2, 16)]
       
    if num_row>8:

        for i, j in iter:
            k = j - 1
            if len(character_sheet[5][i]) < max_len:
                dizionario_pdf_code[f'(r{k})'] = character_sheet[5][i]
            else:
                dizionario_pdf_code[f'(r{k})'] = (character_sheet[5][i])[:max_len]
                dizionario_pdf_code[f'(r{j})'] = (character_sheet[5][i])[max_len:]
    else:
        k=13
        for i in range(1,3):
                num_row=int(math.ceil(len(character_sheet[5][i])/max_len))
                for j in range(1,num_row+1):
                    if j==(num_row+1):
                        dizionario_pdf_code[f'(r{k})'] = character_sheet[5][i][(j-1)*max_len:]
                    else:
                        dizionario_pdf_code[f'(r{k})'] = character_sheet[5][i][(j-1)*max_len:j*max_len]
                    k+=1
        
#    iter = [(1, 14), (2, 16)]
#    for i, j in iter:
#        k = j - 1
#        if len(character_sheet[5][i]) < max_len:
#            dizionario_pdf_code[f'(r{k})'] = character_sheet[5][i]
#        else:
#            dizionario_pdf_code[f'(r{k})'] = (character_sheet[5][i])[:max_len]
#            dizionario_pdf_code[f'(r{j})'] = (character_sheet[5][i])[max_len:]

    # Iterate through the pages and fill the form fields
    for page in template_pdf.pages:
        annotations = page.Annots
        if annotations:
            for annotation in annotations:
                field = annotation
                field_name = field.T
                if field_name in dizionario_pdf_code.keys():
                    field.update(
                        PdfDict(V=dizionario_pdf_code[field_name], AP=PdfDict(N=PdfName('')), DA="/Helv 12 Tf 0 g")
                    )

    # Write the filled PDF to the output file
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject("true")))
    PdfWriter().write(output_pdf_path, template_pdf)

# Avvia il programma con la prima finestra
if __name__ == "__main__":
    csv_path = "classi_e_skill.csv"
    csv_path = os.path.abspath(csv_path)
    txt_path = "character_sheet.txt"
    txt_path = os.path.abspath(txt_path)
    config_folder = "config"
    config_folder = os.path.abspath(config_folder)
    global nuovo_dizionario
    risultati = read_matching_files(csv_path, config_folder)
    nuovo_dizionario = estrai_blocchi_simboli(risultati)
    character_sheet = []
    input_nome()
    print_sheet(character_sheet)
    csv_path = "dictionary_pdf_code.csv"
    csv_path = os.path.abspath(csv_path)
    dizionario_pdf_code = read_dizionario(csv_path)
    input_pdf_path = 'Scheda Hope v.2 edit.pdf'
    output_pdf_path = 'output.pdf'
    print_pdf(dizionario_pdf_code, input_pdf_path, output_pdf_path, character_sheet)


