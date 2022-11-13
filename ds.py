import hashlib
import string
from art import text2art
from hashlib import sha256
import sqlite3
import pyautogui
from colorama import Back, Fore, Style, deinit, init
import smtplib
import ssl
from email.message import EmailMessage
from pip._vendor.distlib.compat import raw_input
import secrets

print(Fore.LIGHTCYAN_EX+(text2art("Welcome To My Project"))+Style.RESET_ALL)

import cowsay
import string
cowsay.tux(Fore.BLUE+"Ds"+Style.RESET_ALL)
print("\n\n\n\n")
conn=sqlite3.connect('Etudiant.db')
c=conn.cursor()
#activer les foreign_keys
c.execute("PRAGMA foreign_keys=on")


#****************************************************creation du table**********************************************************

c.execute(""" create table if not exists T_Etablissement(id_Etab integer  primary key autoincrement ,Libelle_Etab varchar(20), Adresse varchar(20)) """)
c.execute(""" create table if not exists T_Etudiant(N_carte integer primary key autoincrement ,Nom varchar(20),Prenom varchar(20), email varchar(20), pwd varchar(30),id_Etablissement integer ,FOREIGN KEY(id_Etablissement) REFERENCES T_Etablissement(id_Etab)) """)

import string


#****************************************************table etablissement**********************************************************
"""
sql = "INSERT INTO T_Etablissement (Libelle_Etab, Adresse) VALUES (?, ?)"
val = [
  ('université centrale', '12rue saka'),
  ('esprit', '55 rue nasr'),
  ('insat', '41 rue manzah')

]

conn.executemany(sql, val)

conn.commit()

"""

#c.execute(""" insert into T_Etablissement(Libelle_Etab,Adresse) values('Universite centrale','25 Rue Hedi Nouira') """)

#c.execute(""" insert into T_Etablissement(Libelle_Etab,Adresse) values('Universite centrale','25 Rue Hedi Nouira') """)
conn.commit()
import  re


#****************************************************formulaire d'enregistrement**********************************************************

def register():
    print(Fore.LIGHTCYAN_EX+(text2art("enregistrez   vous"))+Style.RESET_ALL)

    trouver=False
    user_email = "^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
    nom = input("Donner votre nom\n")
    #nom=nom.upper()
    prenom = input("Donner votre prenom\n")
    #prenom=string.capwords(prenom)
    # test mail
    while True:
        try:
         email = input("donnez votre email\n"+Fore.RED +" (exp:exemle.exemle@gmail.com):\n"+Style.RESET_ALL)
         if (re.search(user_email, email)):

            break

         else:
             print("Merci d'introduire un email valide \n")
        except ValueError:
            print("Merci d'introduire un email valide \n")
    c.execute("select id_Etab from T_Etablissement")
    itemes = c.fetchone()

    # test password
    while True:
        depno = int(input("Donner votre numero de dep\n"))
        if (depno in itemes):
            break

        else:
            print(Fore.RED+"le departement n'existe pas\n"+Style.RESET_ALL)


    user_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    while True:
        try:
            password = pyautogui.password("Entrer votre mot de passe \n(exp:_qui contient abet miniscule et majuscule\n_contient les caractere speciaux :@#$%^&+=]\n_contient au moin un numero\n ")
            result = re.findall(user_password, password)
            if (result):
                break
            else:
                print("Merci d'introduire un mot de passe valide\n ")
        except ValueError:
            print("Merci d'introduire un mot de passe valide\n ")

    
    #**************************************************** code aléatoire email **********************************************************

    pwd_length = 4
    code = "^[A-Z0-9a-z]*$"
    cd = ''
    for i in range(pwd_length):
     cd += ''.join(secrets.choice(code))
#**************************************************** send mail **********************************************************

    email_sender = 'shopy909@gmail.com'
    email_password = 'jqtsnlvikxuuidlo'
    email_receiver =email

    # Set the subject and body of the email
    subject = 'mot de passe oublié'
    body = ("""copier le code : """+cd)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("verifier votre boite mail") 
    vrf=input("saisir le code :\n")  
    while True:
        try:      
         if cd==vrf :
          
          c.execute(""" insert into T_Etudiant(Nom,Prenom,email,pwd,id_Etablissement) values(?,?,?,?,?) """,(nom.upper(),string.capwords(prenom),email,hashlib.sha256(password.encode()).hexdigest(),depno))
          conn.commit()  
          login() 
         else:
          print("votre compte n'a pas été valider\n")
        except ValueError:
            print("votre compte n'a pas été valider\n ")  
#****************************************************sign in**********************************************************

def login():
        print(Fore.LIGHTCYAN_EX+(text2art("connecter   vous"))+Style.RESET_ALL)

        email=input("entrer votre mail\n")
        pwd=pyautogui.password("entrer votre password\n")

        c.execute("""select * from T_Etudiant where email=? and pwd=?""",(email,hashlib.sha256(pwd.encode()).hexdigest()))
        if(c.fetchone()==None):
         print('données incrorect ressayez \n')
         print('voulez vous esseyer une autre fois ou changer votre mot de passe \n - 1 :sign in \n - 2 :mot de passe oublié')
         choix=int(input("Donner votre choix\n"))

         match choix:
                case 1:
                    login()


                case 2:
#**************************************************** send mail **********************************************************

#**************************************************** code aléatoire email **********************************************************

                    pwd_length = 4
                    code = "^[A-Z0-9a-z]*$"
                    cd = ''
                    for i in range(pwd_length):
                     cd += ''.join(secrets.choice(code))
#**************************************************** send mail **********************************************************

                    email_sender = 'shopy909@gmail.com'
                    email_password = 'jqtsnlvikxuuidlo'
                    email_receiver =email

                    # Set the subject and body of the email
                    subject = 'mot de passe oublié'
                    body = ("""copier le code : """+cd)

                    em = EmailMessage()
                    em['From'] = email_sender
                    em['To'] = email_receiver
                    em['Subject'] = subject
                    em.set_content(body)

                    # Add SSL (layer of security)
                    context = ssl.create_default_context()

                    # Log in and send the email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(email_sender, email_password)
                            smtp.sendmail(email_sender, email_receiver, em.as_string())
                            print("verifier votre boite mail") 
                    vrf=input("saisir le code :\n")        
                    if cd==vrf :
                      npwd=print("saisir le nouveau mot de passe :\n")
                      user_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
                      while True:
                        try:
                            password = pyautogui.password("Entrer votre mot de passe \n(exp:_qui contient abet miniscule et majuscule\n_contient les caractere speciaux :@#$%^&+=]\n_contient au moin un numero\n ")
                            result = re.findall(user_password, password)
                            if (result):
                                break
                            else:
                                print("Merci d'introduire un mot de passe valide\n ")
                        except ValueError:
                            print("Merci d'introduire un mot de passe valide\n ")

                      c.execute(""" Update  T_Etudiant SET pwd = ? where email=? """,(hashlib.sha256(password.encode()).hexdigest(),email))
                      conn.commit() 
                      print("password Updated successfully")       
                   
        else:
                            print(Fore.LIGHTCYAN_EX+(text2art("Welcome    To    your   session"))+Style.RESET_ALL)
                            ex()




#**************************************************** ex 1 **********************************************************

def ex1(d, reverse=False):
    print("Original dictionary elements:")
    colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
    print(colors)
    print("\nSort (ascending) the said dictionary elements by value:")
    print(ex1(colors))
    print("\nSort (descending) the said dictionary elements by value:")
    print(ex1(colors, True))
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))



#**************************************************** ex 2 **********************************************************
def ex2():
    
    d = {0: 10, 1: 20}
    print(d)
    d.update({2: 30})
    print(d)



#**************************************************** ex 3 **********************************************************

def ex3():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic4 = {}
    for d in (dic1, dic2, dic3): dic4.update(d)
    print(dic4)



#**************************************************** ex 4 **********************************************************
def ex4():
    
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


    def is_key_present(x):
        if x in d:
            print('Key is present in the dictionary')
        else:
            print('Key is not present in the dictionary')


    is_key_present(5)
    is_key_present(9)



#**************************************************** ex 5 **********************************************************

def ex5():
    
    d = {'x': 10, 'y': 20, 'z': 30}
    for dict_key, dict_value in d.items():
        print(dict_key, '->', dict_value)




#**************************************************** ex 6 **********************************************************

def ex6():
    
    d = dict()
    for x in range(1, 16):
        d[x] = x ** 2
    print(d)




#**************************************************** ex 7 **********************************************************

def ex7():
    
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(myDict)
    if 'a' in myDict:
        del myDict['a']
    print(myDict)



#**************************************************** ex 8 **********************************************************
def ex8():
    
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    color_dictionary = dict(zip(keys, values))
    print(color_dictionary)




#**************************************************** ex 9 **********************************************************

def ex9():
    
    color_dict = {'red': '#FF0000',
                'green': '#008000',
                'black': '#000000',
                'white': '#FFFFFF'}

    for key in sorted(color_dict):
        print("%s: %s" % (key, color_dict[key]))





#**************************************************** ex 10 **********************************************************
def ex10():
    student_data = {'id1':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id2':
                        {'name': ['David'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },

                    }
    result = {}
    for key in student_data['id1']['subject_integration']:
        print(key)

    for key in student_data['id2']['subject_integration']:
        print(key[0], key[1], key[2], key[3], key[4], key[5], key[6])




#**************************************************** ex 11 **********************************************************

def ex11():
    
    student_data = {'id1':
                        {'name': ['Sara'],
                        'class': ['V'],
                        'subject_integration': ['English, math, science']
                        },
                    'id2':
                        {'name': ['David'],
                        'class': ['V'],
                        'subject_integration': ['English, math, science']
                        },
                    'id3':
                        {'name': ['Sara'],
                        'class': ['V'],
                        'subject_integration': ['English, math, science']
                        }
                    }

    result = {}

    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value

    print(result)



#**************************************************** menu ex **********************************************************
def ex():
    choises={
                1:"ex1",
                2:"ex2",
                3:"ex3",
                4:"ex4",
                5:"ex5",
                6:"ex6",
                7:"ex7",
                8:"ex8",
                9:"ex9",
                10:"ex10",
                11:"ex11"}
    print(choises)            

    x=int(input("Donner votre num\n"))

    match x:
        case 1:
            ex1()
        case 2:
            ex2()
        case 3:
            ex3()
        case 4:
            ex4()
        case 5:
            ex5()
        case 6:
            ex6()
        case 7:
            ex7()
        case 8:
            ex8()
        case 9:
            ex9()
        case 10:
            ex10()
        case 11:
            ex11()



#**************************************************** menu sign in / sign up  **********************************************************
print("choisisez votre choix\n - 1:login\n- 2:register")
sign=int(input("Donner votre choix\n"))

match sign:
    case 1:
        login()


    case 2:
        register()
        
        
        
