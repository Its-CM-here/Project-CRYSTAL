import mysql.connector as mc
from pyttsx3 import *
from datetime import *
import csv
import os
import matplotlib.pyplot as graph
import numpy as np

if not os.path.isfile("security_que.csv"):
    with open("security_que.csv", "a", newline="") as file:
        field = ['Name', 'Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5']
        fwriter = csv.writer(file)
        fwriter.writerow(field)

connection = mc.connect(host="localhost", user="root", passwd="2005", database="pms")
command_line = connection.cursor()

class State_Dict:
    def select_state(self):
        selection = '''Enter the state
1. Andhra Pradesh (Click 1)
2. Arunachal Pradesh (Click 2)
3. Assam (Click 3)
4. Bihar (Click 4)
5. Chhattisgarh (Click 5)
6. Goa (Click 6)
7. Gujarat (Click 7)
8. Haryana (Click 8)
9. Himachal Pradesh (Click 9)
10. Jharkhand (Click 10)
11. Karnataka (Click 11)
12. Kerala (Click 12)
13. Madhya Pradesh (Click 13)
14. Maharashtra (Click 14)
15. Manipur (Click 15)
16. Meghalaya (Click 16)
17. Mizoram (Click 17)
18. Nagaland (Click 18)
19. Odisha (Click 19)
20. Punjab (Click 20)
21. Rajasthan (Click 21)
22. Sikkim (Click 22)
23. Tamil Nadu (Click 23)
24. Telengana (Click 24)
25. Tripura (Click 25)
26. Uttar Pradesh (Click 26)
27. Uttarakhand (Click 27)
28. West Bengal (Click 28)
29. Andaman and Nicobar Islands (Click 29)
30. Chandigarh (Click 30)
31. Dadra and Nagar Haveli and Daman and Diu (Click 31)
32. Delhi (Click 32)
33. Jammu and Kashmir (Click 33)
34. Ladakh (Click 34)
35. Lakshadweep (Click 35)
36. Puducherry (Click 36)
: '''
        return selection

    def get_state(self):
        sname={1: "Andhra Pradesh",
               2: "Arunachal Pradesh",
               3: "Assam",
               4: "Bihar",
               5: "Chhattisgarh",
               6: "Goa",
               7: "Gujarat",
               8: "Haryana",
               9: "Himachal Pradesh",
               10: "Jharkhand",
               11: "Karnataka",
               12: "Kerala",
               13: "Madhya Pradesh",
               14: "Maharashtra",
               15: "Manipur",
               16: "Meghalaya",
               17: "Mizoram",
               18: "Nagaland",
               19: "Odisha",
               20: "Punjab",
               21: "Rajasthan",
               22: "Sikkim",
               23: "Tamil Nadu",
               24: "Telengana",
               25: "Tripura",
               26: "Uttar Pradesh",
               27: "Uttarakhand",
               28: "West Bengal",
               29: "Andaman and Nicobar Islands",
               30: "Chandigarh",
               31: "Dadra and Nagar Haveli and Daman and Diu",
               32: "Delhi",
               33: "Jammu and Kashmir",
               34: "Ladakh",
               35: "Lakshadweep",
               36: "Puducherry"}
        return sname

    def state_pop(self):
        spop_dict={"Andhra Pradesh": 49577103,
                   "Arunachal Pradesh": 1383727,
                   "Assam": 31205576,
                   "Bihar": 104099452,
                   "Chhattisgarh": 25545198,
                   "Goa": 1458545,
                   "Gujarat": 60439692,
                   "Haryana": 25351462,
                   "Himachal Pradesh": 6864602,
                   "Jharkhand": 32988134,
                   "Karnataka": 61095297,
                   "Kerala": 33406061,
                   "Madhya Pradesh": 72626809,
                   "Maharashtra": 112374333,
                   "Manipur": 2570390,
                   "Meghalaya": 2966889,
                   "Mizoram": 1097206,
                   "Nagaland": 1978502,
                   "Odisha": 41974219,
                   "Punjab": 27743338,
                   "Rajasthan": 68548437,
                   "Sikkim": 610577,
                   "Tamil Nadu": 72147030,
                   "Telengana": 35003674,
                   "Tripura": 3673917,
                   "Uttar Pradesh": 199812341,
                   "Uttarakhand": 10086292,
                   "West Bengal": 91276115,
                   "Andaman and Nicobar Islands": 380581,
                   "Chandigarh": 1055450,
                   "Dadra and Nagar Haveli and Daman and Diu": 585764,
                   "Delhi": 16787941,
                   "Jammu and Kashmir": 12267032,
                   "Ladakh": 274000,
                   "Lakshadweep": 64473,
                   "Puducherry": 1247953}
        return spop_dict

st_d=State_Dict()

class Info:
    def stats(self):
        dates = []  # x-axis
        d, r, i, s = [], [], [], []  # y-axis
        state_data_Ti, state_data_Tr, state_data_Td = {}, {}, {}

        st = int(input("Enter the choice \n"
                       "1. National COVID Graph (Click 1) \n"
                       "2. State-wise Analytic SIR Graph (Click 2) \n"
                       "3. Pie Chart representations (Click 3) \n"
                       "4. Exit (Click 4) \n"
                       ": "))

        while st in [1, 2, 3]:
            if st==1:
                confirmed, deaths, cured = [], [], []
                _confirmed, _deaths, _cured = [], [], []
                with open('covid_19_india.csv') as df:
                    reader = csv.reader(df)
                    for rows in reader:
                        if rows[4] != 'Confirmed':
                            confirmed.append(rows[4])
                        if rows[3] != 'Deaths':
                            deaths.append(rows[3])
                        if rows[2] != 'Cured':
                            cured.append(rows[2])

                for xy in confirmed:
                    _confirmed.append(int(xy))
                    continue

                _conf = np.array(_confirmed, dtype=int)

                for yz in deaths:
                    _deaths.append(int(yz))
                    continue

                _death = np.array(_deaths, dtype=int)

                for zx in cured:
                    _cured.append(int(zx))
                    continue

                _cure = np.array(_cured, dtype=int)

                graph.subplot(1, 3, 1)
                graph.title('Infected')
                graph.plot(_conf)

                graph.subplot(1, 3, 2)
                graph.title('Deaths')
                graph.plot(_death)

                graph.subplot(1, 3, 3)
                graph.title('Recovered')
                graph.plot(_cure)

                graph.suptitle('National COVID Graph')
                graph.show()

            if st==2:
                state=int(input(st_d.select_state()))
                name = st_d.get_state().get(state)
                if name is None:
                    print("State not found \nTry Again")
                    continue
                else:
                    filename = name + ".csv"
                    with open(filename) as f:
                        data = csv.reader(f)
                        for row in data:
                            dates.append(row[0])
                            r.append(int(row[2]))
                            d.append(int(row[3]))
                            i.append(int(row[4]))
                            s.append(st_d.state_pop().get(name) - (int(row[3]) + int(row[4])))
                        graph.plot(dates, s, label="Susceptible")
                        graph.plot(dates, i, label="Infected")
                        graph.plot(dates, r, label="Recovered")
                        graph.xlabel('Dates')
                        graph.ylabel('Values')
                        graph.title('SIR Model - %s' % name)
                        graph.legend()
                        graph.show()
                    print("Back to Menu")

            if st==3:
                pie = int(input("Enter the choice for representation \n"
                                "1. Top 5 States With The Highest Total Recovery (Click 1) \n"
                                "2. Top 5 States With The Highest Total Death (Click 2) \n"
                                "3. Top 5 States With The Highest Total Infected (Click 3) \n"
                                "4. Back to menu (Click 4) \n"
                                ": "))

                for nu in st_d.get_state():
                    x, y, z = [], [], []
                    name = st_d.get_state().get(nu)
                    filename = name + ".csv"
                    with open(filename) as f:
                        data = csv.reader(f)
                        for row in data:
                            x.append(int(row[2]))
                            state_data_Tr[name] = sum(x)
                            y.append(int(row[3]))
                            state_data_Td[name] = sum(y)
                            z.append(int(row[4]))
                            state_data_Ti[name] = sum(z)

                while pie in [1, 2, 3]:
                    if pie == 1:
                        d_val_r = list(state_data_Tr.values())
                        d_val_r.sort(reverse=True)
                        key_list_r = list(state_data_Tr.keys())
                        max_states_name_r, pie_data_r = [], []
                        for i in range(5):
                            index = d_val_r[i]
                            position = list(state_data_Tr.values()).index(index)
                            max_states_name_r.append(key_list_r[position])
                        for j in max_states_name_r:
                            pie_data_r.append(state_data_Tr.get(j))

                        clr = ['orange', 'blue', 'green', 'yellow', 'cyan']
                        graph.axis('equal')
                        graph.pie(pie_data_r, labels=max_states_name_r, colors=clr, autopct='%2.2f%%')
                        graph.title("Top 5 States With The Highest Total Recovery")
                        graph.show()

                    if pie == 2:
                        d_val_d = list(state_data_Td.values())
                        d_val_d.sort(reverse=True)
                        key_list_d = list(state_data_Td.keys())
                        max_states_name_d, pie_data_d = [], []
                        for i in range(5):
                            index = d_val_d[i]
                            position = list(state_data_Td.values()).index(index)
                            max_states_name_d.append(key_list_d[position])
                        for j in max_states_name_d:
                            pie_data_d.append(state_data_Td.get(j))

                        clr = ['orange', 'blue', 'green', 'yellow', 'cyan']
                        graph.axis('equal')
                        graph.pie(pie_data_d, labels=max_states_name_d, colors=clr, autopct='%2.2f%%')
                        graph.title("Top 5 States With The Highest Total Death")
                        graph.show()

                    if pie == 3:
                        d_val_i = list(state_data_Ti.values())
                        d_val_i.sort(reverse=True)
                        key_list_i = list(state_data_Ti.keys())
                        max_states_name_i, pie_data_i = [], []
                        for i in range(5):
                            index = d_val_i[i]
                            position = list(state_data_Ti.values()).index(index)
                            max_states_name_i.append(key_list_i[position])
                        for j in max_states_name_i:
                            pie_data_i.append(state_data_Ti.get(j))

                        clr = ['orange', 'blue', 'green', 'yellow', 'cyan']
                        graph.axis('equal')
                        graph.pie(pie_data_i, labels=max_states_name_i, colors=clr, autopct='%2.2f%%')
                        graph.title("Top 5 States With The Highest Total Infected")
                        graph.show()

                    pie = int(input("Enter the choice for representation \n"
                                    "1. Top 5 States With The Highest Total Recovery (Click 1) \n"
                                    "2. Top 5 States With The Highest Total Death (Click 2) \n"
                                    "3. Top 5 States With The Highest Total Infected (Click 3) \n"
                                    "4. Back to menu (Click 4) \n"
                                    ": "))

            st = int(input("Enter the choice \n"
                           "1. National COVID Graph (Click 1) \n"
                           "2. State-wise Analytic SIR Graph (Click 2) \n"
                           "3. Pie Chart representations (Click 3) \n"
                           "4. Exit (Click 4) \n"
                           ": "))
        print("User Logged Out")

    def assistant(self):
        s1 = input("Do you have fever? (Y/N): ")
        s2 = input("Do you have dry cough? (Y/N): ")
        s3 = input("Do you feel tired? (Y/N): ")
        s4 = input("Do you feel difficulty in breathing? (Y/N): ")
        s5 = input("Do you have pain in chest region? (Y/N): ")
        s6 = int(input("How many days since these symptoms showed up?: "))
        if s6<2:
            print("I advice you to consult with a doctor nearby")
        elif s6>=3 or s6<=14:
            symptoms = [s1, s2, s3, s4, s5]
            if max(symptoms) == "Y":
                print("We advice you to take COVID test as soon as possible")
            else:
                print("I advice you to consult with a doctor nearby and isolate yourself")
        else:
            print("I advice you to consult with a doctor nearby")

def baymax():
    covid = Info()
    baymax_voice = init()
    text = ["Hi! I am Baymax. Your personal healthcare companion.",
            "What can i do for you?",
            "1. Give COVID Statistics (Click 1)",
            "2. Take a AI Consultation (Click 2)"]
    for l in text:
        baymax_voice.say(l)
        print(l)
        baymax_voice.runAndWait()
    q = int(input(" : "))
    if q == 1:
        covid.stats()
    if q == 2:
        covid.assistant()
    else:
        exit()

def passwrd_verify(username, main_q):
    global Y
    password = input("Enter Password: ")
    if main_q == 1:
        syntax = "select password from admin_login where username='{}'".format(username)
    if main_q == 2:
        syntax = "select password from people_login where username='{}'".format(username)
    command_line.execute(syntax)
    j = command_line.fetchall()
    for m in j:
        for n in m:
            if n == password:
                print("Welcome back %s" % username)
                Y = True
            else:
                print("Password is incorrect \nTry Again !")
                Y = False
    return Y

def pswrd_register():
    password = input("Enter a password: ")
    low, up, special, num = 0, 0, 0, 0
    if len(password)>=7:
        for i in password:
            if i.isnumeric():
                num+=1
            elif i.isupper():
                up+=1
            elif i.islower():
                low+=1
            else:
                special+=1
        continuation = True
    else:
        print("Password must contain minimum of 7 characters")
        continuation = False
    return continuation, num, special, up, low, password

def verify_plus_eff(num, special, up, low, password):
    global cont
    if num >= 2:
        if special >= 1:
            if up >= 1:
                if low >= 1:
                    cont=True
                else:
                    print("Password must contain minimum of 1 Lowercase letter")
                    cont = False
            else:
                print("Password must contain minimum of 1 Uppercase letter")
                cont = False
        else:
            print("Password must contain minimum of 1 special symbol")
            cont = False
    else:
        print("Password must contain minimum of 2 numerical values")
        cont = False
    return cont

def psc():
    next, number, symbols, upper, lower, pswrd = pswrd_register()
    while next == False:
        next, number, symbols, upper, lower, pswrd = pswrd_register()
    else:
        cont = verify_plus_eff(number, symbols, upper, lower, pswrd)
        if cont:
            return cont, pswrd
        else:
            psc()

def choices():
    global que_ans, que1, que2, que3, ans1, ans2, ans3, ch1, ch2, ch3

    question = {1: "A. Messi or B. CR7",
                2: "A. Coffee or B. Tea",
                3: "A. Summer or B. Winter",
                4: "A. Paris or B. Maldives",
                5: "A. Science or B. Commerce"}

    ch1 = int(input("Your first choice : "))
    if ch1 in [1,2,3,4,5]:
        ch2 = int(input("Your second choice : "))
        if ch2 != ch1:
            if ch2 in [1,2,3,4,5]:
                ch3 = int(input("Your third choice : "))
                if ch3 != ch1 and ch3 != ch2 :
                    if ch3 in [1,2,3,4,5]:
                        for i in range(1, 6):
                            if ch1 == i:
                                que1 = question[i]
                                ans1 = input("%s \nClick A or B : " %que1)
                            if ch2 == i:
                                que2 = question[i]
                                ans2 = input("%s \nClick A or B : " %que2)
                            if ch3 == i:
                                que3 = question[i]
                                ans3 = input("%s \nClick A or B : " %que3)
                    else:
                        print("Please choose either 1,2,3,4 or 5")
                        choices()
                else:
                    print("Please choose three different questions.")
                    choices()
            else:
                print("Please choose either 1,2,3,4 or 5")
                choices()
        else:
            print("Please choose different questions.")
            choices()
    else:
        print("Please choose either 1,2,3,4 or 5")
        choices()

def block(username, main_q):
    if main_q == 1:
        syntax = "select password from admin_login where username='{}'".format(username)
    if main_q == 2:
        syntax = "select password from people_login where username='{}'".format(username)
    command_line.execute(syntax)
    j = command_line.fetchall()
    for m in j:
        for n in m:
            password = n
    block_date = datetime.today().date()
    timeperiod = timedelta(days=2)
    unblock_date = block_date + timeperiod
    if main_q == 1:
        syntax = "insert into admin_blocked values('{}', '{}', '{}', '{}')".format(block_date, unblock_date, username, password)
        command_line.execute(syntax)
        syntax2 = "delete from admin_login where username='{}'".format(username)
        command_line.execute(syntax2)
    if main_q == 2:
        syntax = "insert into people_blocked values('{}', '{}', '{}', '{}')".format(block_date, unblock_date, username, password)
        command_line.execute(syntax)
        syntax2 = "delete from people_login where username='{}'".format(username)
        command_line.execute(syntax2)
    connection.commit()

def unblock(main_q):
    if main_q == 1:
        command_line.execute("select * from admin_blocked")
    if main_q == 2:
        command_line.execute("select * from people_blocked")
    for i in command_line:
        DATE, sql_unblock_date, usrnme, pswrd = i[0], i[1], i[2], i[3]
        if datetime.today().date() == sql_unblock_date:
            if main_q == 1:
                syntax = "insert into admin_login values('{}', '{}')".format(usrnme, pswrd)
            if main_q == 2:
                syntax = "insert into people_login values('{}', '{}')".format(usrnme, pswrd)
            command_line.execute(syntax)
            if main_q == 1:
                syntax = "delete from admin_blocked where username='{}'".format(usrnme)
            if main_q == 2:
                syntax = "delete from people_blocked where username='{}'".format(usrnme)
            command_line.execute(syntax)
            connection.commit()

def reset():
    global nxt
    question = {1: "A. Messi or B. CR7",
                2: "A. Coffee or B. Tea",
                3: "A. Summer or B. Winter",
                4: "A. Paris or B. Maldives",
                5: "A. Science or B. Commerce"}
    text = ["Please answer the following questions correctly to proceed",
            "After resetting your password, your account will be unblocked."]
    baymax_voice = init()
    for x in text:
        baymax_voice.say(x)
        print(x)
        baymax_voice.runAndWait()
    usrname = input("Enter your username : ")
    with open("security_que.csv", 'r', newline="") as file:
        reader = csv.reader(file)
        y=[]
        for i in reader:
            for j in range(len(i)):
                if usrname == i[0]:
                    x=[0,1,2,3,4,5]
                    if i[j] != "" and i[j] != usrname:
                        y.append(x.pop(j))
            val, bool = 0, False
            for a in y:
                val+=1
                qs = question.get(a)
                q = input("%s \nClick A or B: " %qs)
                if q == i[a]:
                    print("Correct Answer")
                else:
                    print("As you have entered wrong answer, your account cannot be unblocked !")
                    bool=False
                    break
                if val==3:
                    bool=True
                    break
            if bool:
                break
        else:
            print("User not found. Try again!")
    new_pswrd = input("Enter your new password : ")
    new_pswrd_confirm = input("Enter your new password for confirmation : ")
    if bool:
        if new_pswrd == new_pswrd_confirm:
            command_line.execute("select * from people_blocked where username = '%s'" %usrname)
            print("Password changed successfully")
            for i in command_line:
                usrnme, pswrd = i[2], i[3]
                syntax = "insert into people_login values('{}', '{}')".format(usrnme, new_pswrd)
                command_line.execute(syntax)
                print("Unblocked successfully")
                syntax = "delete from people_blocked where username='{}'".format(usrnme)
                command_line.execute(syntax)
                connection.commit()
            print("Please login again to continue.")
            nxt=False
            verify.public(2)

        else:
            print("Passwords do not match. Try again.")
            nxt=True
            while nxt:
                if new_pswrd == new_pswrd_confirm:
                    syntax = "update people_login set Password = {0} where Username = {1}".format(str(usrname), str(new_pswrd))
                    command_line.execute(syntax)
                    connection.commit()
                    print("Password changed successfully")
                    command_line.execute("select * from people_blocked where username = %s" % usrname)
                    for i in command_line:
                        usrnme, pswrd = i[2], i[3]
                        syntax = "insert into people_login values('{}', '{}')".format(usrnme, pswrd)
                        command_line.execute(syntax)
                        syntax = "delete from people_blocked where username='{}'".format(usrnme)
                        command_line.execute(syntax)
                        connection.commit()
                    print("Please login again to continue.")
                    nxt=False
                verify.public(2)

class Credentials:
    def public(self, main_q):
        global X, a

        lors = int(input("1. Login (Click 1)\n"
                         "2. Register (Click 2) \n"
                         " : "))
        if lors == 1:
            username = input("Enter Username: ")
            syntax_usr = "select username from people_login where username='{}'".format(username)
            command_line.execute(syntax_usr)
            i = command_line.fetchall()
            if len(i) == 0:
                syntax_usr = "select username from people_blocked where username='{}'".format(username)
                command_line.execute(syntax_usr)
                j = command_line.fetchall()
                if len(j) == 0:
                    print("Username not found")
                    verify.public(main_q)
                else:
                    for m in j:
                        for n in m:
                            if username == n:
                                print("User blocked")
                                reset()
                                syntax_usr = "select unblock_due_date from people_blocked where username='{}'".format(username)
                                command_line.execute(syntax_usr)
                                for a in command_line:
                                    unblock_date = a[0]
                                    z = unblock_date - datetime.today().date()
                                    print("The user", username, "will be unblocked on", unblock_date, "(", z, "days from today)")
                                    verify.public(main_q)
            else:
                for k in i:
                    for l in k:
                        if username == l:
                            a=passwrd_verify(username, main_q)
                        else:
                            print("Username not found")
                            verify.public(main_q)
            return username, a

        if lors == 2:
            try:
                username = input("Enter Username: ")
                print("Password must contain minimum of 7 characters. \n"
                      "Password must contain minimum of 2 numerical values. \n"
                      "Password must contain minimum of 1 special symbol. \n"
                      "Password must contain minimum of 1 Uppercase letter. \n"
                      "Password must contain minimum of 1 Lowercase letter")
                flow, pswrd = psc()
                if flow:
                    syntax = "insert into people_login values('{}', '{}')".format(username, pswrd)
                    command_line.execute(syntax)
                    connection.commit()
                    print("You have successfully registered with PMS !!")
                    text = ['Please answer the following questions for security purposes.',
                            'Choose any 3 from 5 questions.',
                            "1. Messi or CR7 (Click 1)",
                            "2. Coffee or Tea (Click 2)",
                            "3. Summer or Winter (Click 3)",
                            "4. Paris or Maldives (Click 4)",
                            "5. Science or Commerce (Click 5)"]
                    voice = init()
                    for l in text:
                        voice.say(l)
                        print(l)
                        voice.runAndWait()
                    choices()
                    with open("security_que.csv", "a", newline="") as file:
                        fwriter = csv.writer(file)
                        que_ans = [username, "", "", "", "", ""]
                        que_ans[ch1], que_ans[ch2], que_ans[ch3] = ans1, ans2, ans3
                        fwriter.writerow(que_ans)
                return username, True
            except mc.errors.IntegrityError:
                print("User already exists")

    def admin(self, main_q):
        global X
        username = input("Enter Username: ")
        syntax_usr = "select username from admin_login where username='{}'".format(username)
        command_line.execute(syntax_usr)
        i = command_line.fetchall()
        if len(i) == 0:
            print("Username not found")
            verify.admin(main_q)
        else:
            for k in i:
                for l in k:
                    if username == l:
                        X = passwrd_verify(username, main_q)
                    else:
                        print("Username not found")
                        verify.admin(main_q)
        return username, X

def admin_func():
    flag = True
    while flag:
        with open("covid_19_india.csv", "a", newline="") as f:
            w1 = csv.writer(f)
            print("Select State")
            state = int(input(st_d.select_state()))
            state_name = st_d.get_state().get(state)
            if state_name is None:
                print("State not found \nTry Again")
                continue
            else:
                d = input("Enter date (DD-MM-YYYY): ")
                c = int(input("Enter Cured: "))
                dead = int(input("Enter Death: "))
                cc = int(input("Enter Confirmed Cases: "))
                rec = [d, state_name, c, dead, cc]
                w1.writerow(rec)
                filename = state_name + ".csv"
                with open(filename, "a") as f1:
                    w2 = csv.writer(f1)
                    w2.writerow(rec)

                flag = input("Do you want to enter more records (Y/N): ")
                if flag=="Y":
                    flag=True
                elif flag=="N":
                    flag=False

print("Welcome to Pandemic Management System")
main_q = int(input("Are you \n"
                   "1. a health official (Click 1)\n"
                   "2. a public (Click 2)\n"
                   " : "))
verify = Credentials()

if main_q == 1:
    adm, a = verify.admin(main_q)
    unblock(main_q)
    if a:
        ad_ch = int(input("1. Enter COVID records (Click 1) \n"
                          "2. Log out (Click 2) \n"
                          ": "))
        if ad_ch==1:
            admin_func()
        else:
            print("Logging out ...")
        print("User logged out")
    else:
        num = 0
        while num < 2:
            x = passwrd_verify(adm, main_q)
            if not x:
                num += 1
            else:
                break
        else:
            print("Sorry! As you have entered the password incorrectly multiple times, we have temporarily blocked your account \n"
                  "Try again later!")
            block(adm, main_q)

elif main_q == 2:
    usr, a = verify.public(main_q)
    unblock(main_q)
    if a:
        baymax()
    else:
        num = 0
        while num < 2:
            Y = passwrd_verify(usr, main_q)
            if not Y:
                num += 1
            else:
                break
        else:
            print("Sorry! As you have entered the password incorrectly multiple times, we have temporarily blocked your account \n"
                  "Try again later!")
            block(usr, main_q)
