

import PySimpleGUI as sg
import os.path
import string


file_list_column = [
    [
        sg.Text("Text file Folder"),
        sg.In(size=(40, 1), enable_events=True, key="Folder"),
        sg.FolderBrowse(),
        
    ],
    [sg.Text("Choose a text file from thelist")],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="Files"
        )
    ],
]

rot_cipher_column = [
    [sg.Text("File under operation:")],
    [sg.Text(size=(60, 4), key="selected", text_color='black')],
    [sg.Text("Choose whether to encrypt or decrypt the text"), sg.Combo(list(['encrypt','decrypt']), size=(20,4), key='crypt')],
    [sg.Text('Enter the rotation number (0-25)'), sg.InputText(size=(20,4), key='rotnum')],
    [
        sg.Text("Output file Folder"),
        sg.In(size=(40, 1), enable_events=True, key="OutFolder"),
        sg.FolderBrowse(),
        
    ],
    [sg.Button('Operate', key='operate')],
    [sg.Multiline(size=(60, 4), key="-output-", text_color='black')]

]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(rot_cipher_column),
    ]
]

window = sg.Window("Kuroonai's Caesar cipher", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Folder":
        folder = values["Folder"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".txt", ".docx",".doc",".odt",".rtf",".wpd"))
        ]
        window["Files"].update(fnames)
    elif event == "Files":
        try:
            filename = os.path.join(
                values["Folder"], values["Files"][0]
            )
            window["selected"].update(filename)

        except:
            pass
        
    
    elif event=='operate':
        if values['crypt'] == 'encrypt' :crypt = 1
        else:  crypt = 0
        rotnum = int(values['rotnum'])
        data = window["selected"].update(filename)
        actual = list(string.ascii_letters)
        ciphered = list(actual[rotnum:] + actual[:rotnum])
        

        with open(filename, 'r', errors="ignore") as file:
            inp = file.read() #.replace('\n', ' ')
    
        split_inp = inp.splitlines()
        out = ''
        
        for iind, i in enumerate(split_inp):
            letters = list(i)
            
            newword = ''
            for  j in letters:
                if crypt == True:
                    if j in ciphered:newword += actual[ciphered.index(j)]
                    else : newword += j
                else:
                    if j in actual:newword += ciphered[actual.index(j)]
                    else : newword += j
            if iind != 0:
                out +='\n'
            
            out += newword
        
        filetosave = '-'.join([f"{values['crypt']}ed", values["Files"][0]])
        filename = os.path.join(values["OutFolder"], filetosave)
        
        with open(filename,'w') as oup:
            oup.write(out)
        
        displaytext = f"The {values['crypt']}ed text is saved as {filename}"
        window["-output-"].update(displaytext)

window.close()
