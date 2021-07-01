#« Mini projet »
#Le Chiffre de César

#projet réalisé par 
#DESSE QUENTIN
#RADDE THEO
#REGNIER LOUIS
 
#Bibliothèque Tkinter
from tkinter import *
from tkinter.filedialog import *

#Fenêtre du logiciel
window = Tk()
window.title("Code César by Quentinou, théophite et louis 1er")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("LOGOI.ico")

#Frame dans la fenêtre du logiciel
frame = Frame(window)

label_title = Label(frame, text = "Chiffrement par decalage", font = ("Arial", 28))
label_title.pack(side = "top")

#Message à crypter
label_message = Label(frame, text = "Message à crypter : ", font = ("Arial", 10))
label_message.pack()
entry_message = Entry(frame, font = ("Arial", 10))
entry_message.pack()

#Cryptage depuis un fichier .txt *
label_import = Label(frame, text = "Ou importez un fichier au format .txt : ", font = ("Arial", 10))
label_import.pack()
FILETYPES = [ ("text files", "*.txt") ]
filename = StringVar(window)
def set_filename():
    filename.set(askopenfilename(filetypes=FILETYPES))
    print(filename.get())

button_filePath = Button(frame, text='Parcourir', command=set_filename)
button_filePath.pack()

def read_filename():
    fileOpen = open(filename.get(), 'r')
    return fileOpen.read()

#Clé de cryptage
label_cle = Label(frame, text = "Entrez votre clé de cryptage : ", font = ("Arial", 10))
label_cle.pack()
entry_cle = Entry(frame, font = ("Arial", 10))
entry_cle.pack()
label_crypted = Label(frame, text = "Votre message crypté apparaîtra ici", font = ("Arial", 10), fg = "red")
label_crypted.pack()

#Fonction du code césar
def cesarCode():
    listMin=['a','b','c','d','e','f','g','h','i','j','k','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
    listCap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    message = str()

    #Petit plus -> zone vide
    if entry_message.get() != '':
        message = entry_message.get()
    else:
        message = read_filename()

    message_code = str()
    if entry_cle.get()=='':
        label_crypted['text'] = "Il faut saisir une clé de chiffrement"
        label_crypted['fg'] = "red"
        return

    #Petit plus -> zone incorect
    if not entry_cle.get().isnumeric():
        label_crypted['text'] = "La clé doit être un nombre"
        label_crypted['fg'] = "red"
        return
    cle = int(entry_cle.get())

    for lettre in message:
        if lettre not in listMin and lettre not in listCap:
            message_code += lettre
        else:
            for alphabetMinLettre in listMin:
                if(lettre == alphabetMinLettre):
                    for i in range (len(listMin)):
                        if listMin[i]==lettre:
                            message_code += str(listMin[(i+cle) % 26])
            
            for alphabetCapLettre in listCap:
                if(lettre == alphabetCapLettre):
                    for i in range (len(listCap)):
                        if listCap[i]==lettre:
                            message_code += str(listCap[(i + cle) % 26])

    #Affichage 
    label_crypted['text'] = message_code
    label_crypted['fg'] = "green"

#Bouton pour Affichage 
bt_submit = Button(frame, text = "Crypter", font = ("Arial", 12), command = cesarCode)
bt_submit.pack()

#Placement de la frame dans la fenêtre du logiciel
frame.pack(expand = "yes")

#Affichage de la fenêtre
window.mainloop()