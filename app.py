import datetime
import tkinter as t
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import shelve
import random
import smtplib

r = t.Tk()
r.title('bank system')
r.config(bd=8, bg='grey', relief=GROOVE, highlightbackground='red', )
Label(r, text='Welcome', font=('Arial', 25), pady=10, relief=RAISED, bd=8).pack()


def call_main(frame, b):
    # disable window m
    b.state('withdraw')
    frame.destroy()
    main()


def check_value():
    # creating new account
    print(gen.get())
    if ent_phone.get().isdigit() == False or len(ent_phone.get()) != 10:
        messagebox.showinfo('Error', 'Please enter correct phone no. value')

        ent_phone.focus_set()


    elif ent_file.get().isalpha() == False:
        messagebox.showinfo('Error', 'Please enter correct name value')
    try:
        if (int(e_d.get()) > 31 or int(e_d.get()) < 1) or (int(e_m.get()) < 1 or int(e_m.get()) > 12) or len(
                e_y.get()) != 4:
            messagebox.showinfo('Error', 'Please enter correct Date of birth  value')
        else:
            creating_acc()
    except ValueError:
        messagebox.showinfo('Error', 'Please fill entrys enter')


def check_value1(name):
    # edit
    print(gen1.get())
    if ent_phone1.get().isdigit() == False or len(ent_phone1.get()) != 10:
        messagebox.showinfo('Error', 'Please enter correct phone no. value')

        ent_phone1.focus_set()


    elif ent_file1.get().isalpha() == False:
        messagebox.showinfo('Error', 'Please enter correct name value')
    try:
        if (int(e_d1.get()) > 31 or int(e_d1.get()) < 1) or (int(e_m1.get()) < 1 or int(e_m1.get()) > 12) or len(
                e_y1.get()) != 4:
            messagebox.showinfo('Error', 'Please enter correct Date of birth  value')
        else:
            editing_acc(name)

    except ValueError:
        messagebox.showinfo('Error', 'Please fill entrys enter')


def creating_acc():
    a = shelve.open('acclist')
    file_name = '91' + ent_phone.get()
    try:
        k = a['list1']
        k.append(file_name)
        a['list1'] = k
    except:
        a['list1'] = file_name

    a.close()

    file_name = '91' + ent_phone.get()
    new_file = shelve.open(file_name)
    new_file['acc_num'] = '91' + ent_phone.get()
    new_file['user_name'] = ent_file.get()
    new_file['address'] = ent_add.get()
    new_file['password'] = ent_pass.get()
    new_file['phone'] = ent_phone.get()
    new_file['acc_type'] = acctype.get()
    new_file['email'] = ent_mail.get()
    new_file['balance'] = 0
    new_file['statement'] = []
    new_file['index'] = 1
    new_file['dob'] = e_d.get() + ' / ' + e_m.get() + ' /' + e_y.get()
    new_file.close()
    messagebox.showinfo('MESSAGE', '''YOUR ACCOUNT IS SUCCESSFUL CREATE
AND YOUR ACC. NO. ''' + file_name)


def new(frame):
    # creating new window for new account
    global ent_file, m, ent_add, ent_pass, ent_phone, acctype, gen, ent_mail, e_d, e_m, e_y
    r.state('withdraw')

    m = t.Tk()
    m.title('New Acoount')
    # lab_=Label(m,text="From ",font=("",20))
    # lab_.place(x=180,y=10)
    lab_name = Label(m, text='NAME :', font=("", 16), fg='red')
    lab_name.place(x=40, y=70)
    lab_messege = Label(m, text="  (name less than or equal to 16 alpha)", font=("", 10), fg='grey')
    lab_messege.place(x=155, y=100)
    lab_add = Label(m, text='ADDRESS :', font=("", 16), fg='red')
    lab_add.place(x=40, y=125)
    lab_pass = Label(m, text='PASSWORD :', font=("", 16), fg='red')
    lab_pass.place(x=40, y=160)
    lab_phone = Label(m, text='PHONE NO :', font=("", 16), fg='red')
    lab_phone.place(x=40, y=190)
    lab_gender = Label(m, text='GENDER :', font=("", 16), fg='red')
    lab_gender.place(x=40, y=225)
    lab_dob = Label(m, text='D. O. B :', font=("", 16), fg='red')
    lab_dob.place(x=40, y=265)
    lab_mail = Label(m, text='E-MAIL :', font=("", 16), fg='red')
    lab_mail.place(x=40, y=305)
    lab_acctype = Label(m, text='ACC. Type :', font=("", 16), fg='red')
    lab_acctype.place(x=40, y=340)
    lab_d = Label(m, text='(dd/mm/yyyy)', fg='grey')
    lab_d.place(x=320, y=265)

    e_d = ttk.Entry(m, width=2, font=("", 16))
    e_d.place(x=165, y=265)
    e_m = ttk.Entry(m, width=2, font=("", 16))
    e_m.place(x=205, y=265)
    e_y = ttk.Entry(m, width=4, font=("", 14))
    e_y.place(x=255, y=265)
    ent_phone = ttk.Entry(m, width=10, font=("", 16))

    ent_phone.place(x=165, y=195)
    ent_file = ttk.Entry(m, width=25, font=("", 16))
    ent_file.place(x=165, y=70)
    ent_pass = ttk.Entry(m, width=20, font=("", 16))
    ent_pass.place(x=165, y=160)
    ent_add = ttk.Entry(m, width=25, font=("", 16))
    ent_add.place(x=165, y=125)
    ent_mail = ttk.Entry(m, width=30, font=("", 16))
    ent_mail.place(x=165, y=310)

    acctype = StringVar()
    ttk.Radiobutton(m, text='Saving', value='Male', variable=acctype).place(x=165, y=340)
    ttk.Radiobutton(m, text='Current', value='Female', variable=acctype).place(x=250, y=340)
    gen = StringVar()
    aaa = ttk.Radiobutton(m, text='Male', value='0', variable=gen)
    aaa.place(x=165, y=225)
    a = ttk.Radiobutton(m, text='Female', value='1', variable=gen)
    a.place(x=250, y=225)

    but_submit = ttk.Button(m, text="submit", command=check_value)
    but_submit.place(x=250, y=380)
    # ent_.insert(0,"less then or equal to 16 letters")
    but_back = ttk.Button(m, text="Back", width=10, command=lambda: call_main(frame, m))
    # but_back.place(x=10,y=10)
    # but_back=ttk.Button(m,text="verifi email",width=10,command=call_main)
    # but_back.place(x=10,y=10)

    but_back.grid(row=300, column=10, padx=10, pady=10)
    # check_value

    m.geometry('600x500')
    m.mainloop()


# ----edit profile
def editing_acc(name):
    new_file = shelve.open(name)
    new_file['acc_num'] = '91' + ent_phone1.get()
    new_file['user_name'] = ent_file1.get()
    new_file['address'] = ent_add1.get()
    new_file['gender'] = gen1.get()
    new_file['password'] = ent_pass1.get()
    new_file['phone'] = ent_phone1.get()
    new_file['acc_type'] = acctype1.get()
    new_file['email'] = ent_mail1.get()
    new_file['dob'] = e_d1.get() + ' / ' + e_m1.get() + ' /' + e_y1.get()
    new_file.close()
    messagebox.showinfo('MESSAGE', '''YOUR PROFILE IS SUCCESFULLY
UPDATED ''' + name)


def edit(frame, name):
    # creating new window for new account
    global ent_file1, m1, ent_add1, ent_pass1, ent_phone1, acctype1, gen1, ent_mail1, e_d1, e_m1, e_y1
    r.state('withdraw')

    m1 = t.Tk()
    m1.title('Edit Profile')
    lab_name = Label(m1, text='NAME :', font=("", 16), fg='red')
    lab_name.place(x=40, y=70)
    lab_messege = Label(m1, text="  (name less than or equal to 16 alpha)", font=("", 10), fg='grey')
    lab_messege.place(x=155, y=100)
    lab_add = Label(m1, text='ADDRESS :', font=("", 16), fg='red')
    lab_add.place(x=40, y=125)
    lab_pass = Label(m1, text='PASSWORD :', font=("", 16), fg='red')
    lab_pass.place(x=40, y=160)
    lab_phone = Label(m1, text='PHONE NO :', font=("", 16), fg='red')
    lab_phone.place(x=40, y=190)
    lab_gender = Label(m1, text='GENDER :', font=("", 16), fg='red')
    lab_gender.place(x=40, y=225)
    lab_dob = Label(m1, text='D. O. B :', font=("", 16), fg='red')
    lab_dob.place(x=40, y=265)
    lab_mail = Label(m1, text='E-MAIL :', font=("", 16), fg='red')
    lab_mail.place(x=40, y=305)
    lab_acctype = Label(m1, text='ACC. Type :', font=("", 16), fg='red')
    lab_acctype.place(x=40, y=340)
    lab_d = Label(m1, text='(dd/mm/yyyy)', fg='grey')
    lab_d.place(x=320, y=265)

    e_d1 = ttk.Entry(m1, width=2, font=("", 16))
    e_d1.place(x=165, y=265)
    e_m1 = ttk.Entry(m1, width=2, font=("", 16))
    e_m1.place(x=205, y=265)
    e_y1 = ttk.Entry(m1, width=4, font=("", 14))
    e_y1.place(x=255, y=265)
    ent_phone1 = ttk.Entry(m1, width=10, font=("", 16))

    ent_phone1.place(x=165, y=195)
    ent_file1 = ttk.Entry(m1, width=25, font=("", 16))
    ent_file1.place(x=165, y=70)
    ent_pass1 = ttk.Entry(m1, width=20, font=("", 16))
    ent_pass1.place(x=165, y=160)
    ent_add1 = ttk.Entry(m1, width=25, font=("", 16))
    ent_add1.place(x=165, y=125)
    ent_mail1 = ttk.Entry(m1, width=30, font=("", 16))
    ent_mail1.place(x=165, y=310)

    acctype1 = StringVar()
    ttk.Radiobutton(m1, text='Saving', value='Male', variable=acctype1).place(x=165, y=340)
    ttk.Radiobutton(m1, text='Current', value='Female', variable=acctype1).place(x=250, y=340)
    gen1 = StringVar()
    aaa1 = ttk.Radiobutton(m1, text='Male', value='0', variable=gen1)
    aaa1.place(x=165, y=225)
    a1 = ttk.Radiobutton(m1, text='Female', value='1', variable=gen1)
    a1.place(x=250, y=225)

    but_submit1 = ttk.Button(m1, text="submit", command=lambda: check_value1(name))
    but_submit1.place(x=250, y=390)
    # ent_.insert(0,"less then or equal to 16 letters")
    but_back = ttk.Button(m1, text="Back", width=10, command=lambda: call_main(frame, m1))
    # but_back.place(x=10,y=10)
    # but_back=ttk.Button(m,text="verifi email",width=10,command=call_main)
    # but_back.place(x=10,y=10)

    but_back.grid(row=300, column=10, padx=10, pady=10)
    # check_value

    m1.geometry('700x700')
    m1.mainloop()


def aa():
    print()
    print(gen.get())


def open1(name, password, frame, e3, otp):
    global s
    op = shelve.open('acclist')

    name = ent.get()
    if e3 == otp:
        if (name in op['list1']):
            o = shelve.open(name)
            # print(o['password'])
            if o['password'] == password:
                r.state('withdraw')
                s = t.Tk()
                s.title('SDK BANK')

                def withdraw():
                    global e_withdraw
                    l_withdraw = ttk.Label(s, text='Enter Amount to withdraw :', font=('', 16)).place(x=45, y=230)
                    e_withdraw = ttk.Entry(s, width=10, font=('', 14))
                    e_withdraw.focus_set()
                    e_withdraw.bind('<Return>', sub_wid)
                    e_withdraw.place(x=300, y=230)
                    b_withdraw = ttk.Button(s, text='Click', command=lambda: sub_wid(name)).place(x=150, y=270)

                def deposit(name):
                    global e_deposit
                    l_deposit = ttk.Label(s, text='Enter Amount to Deposit :', font=('', 16)).place(x=45, y=230)
                    e_deposit = ttk.Entry(s, width=10, font=('', 14))
                    e_deposit.focus_set()
                    e_deposit.bind('<Return>', add_dep)
                    e_deposit.place(x=300, y=230)
                    b_deposit = ttk.Button(s, text='Click', command=lambda: add_dep(name)).place(x=150, y=270)
                    detail.close()

                def sub_wid(name):
                    if e_withdraw.get().isdigit() == True:
                        detail = shelve.open(name)
                        if detail['balance'] > 2000:
                            detail['balance'] -= int(e_withdraw.get())
                            lab_balance.config(text='Balance :' + str(detail['balance']))
                            k = detail['statement']
                            tj.config(state='normal')
                            d = datetime.datetime.now()

                            tj.delete('1.0', END)
                            tj.insert(INSERT, 'Your   ' + e_withdraw.get() + '\trupees successfull withdraw\n')

                            tj.config(state='disabled')

                            k.append(str(detail['index']) + '    ' + str(d.day) + '/' + str(d.month) + '/' + str(
                                d.year) + '                   ' + e_withdraw.get() + 'dr.     ' + str(
                                detail['balance']))
                            detail['index'] += 1
                            print(k)
                            print(str(detail['index']) + '    ' + str(d.day) + '/' + str(d.month) + '/' + str(
                                d.year) + '                   ' + e_withdraw.get() + 'dr.     ' + str(
                                detail['balance']), '     **helloweoihfweenfkeiifif')
                            # print(detail['statement'])
                            detail['statement'] = k
                            # print(str(d))
                            detail.close()
                            e_withdraw.delete(0, t.END)
                            # messagebox.showinfo('With draw',e_withdraw.get()+' rupess successfully withdraw')
                        else:
                            messagebox.showinfo('Error', 'Low Balance')
                    else:
                        messagebox.showinfo('Error', 'Enter correct value')

                def add_dep(name):
                    if e_deposit.get().isdigit() == True:
                        detail = shelve.open(name)
                        print(name)
                        detail['balance'] += int(e_deposit.get())
                        k = detail['statement']
                        tj.config(state='normal')
                        d = datetime.datetime.now()

                        tj.delete('1.0', END)
                        lab_balance.config(text='Balance :' + str(detail['balance']))
                        tj.insert(INSERT, 'Your   ' + e_deposit.get() + '\trupees successfull deposit\n')
                        tj.config(state='disabled')
                        k.append(str(detail['index']) + '    ' + str(d.day) + '/' + str(d.month) + '/' + str(
                            d.year) + '     ' + e_deposit.get() + 'cr.     ' + '              ' + str(
                            detail['balance']))
                        print(k)
                        detail['statement'] = k
                        detail['index'] += 1
                        # print(detail['statement'])

                        # print(str(d))

                        detail.close()
                        e_deposit.delete(0, t.END)
                        messagebox.showinfo('Deposit', e_deposit.get() + ' rupess successfully deposit')
                    else:
                        messagebox.showinfo('Error', 'Enter correct value')

                def sat(name):
                    detail = shelve.open(name)

                    tj.config(state='normal')
                    tj.delete('1.0', END)
                    tj.insert(INSERT, 'So.no.   Date     Deposit      Withdraw    Balance \n')

                    # t.insert(INSERT,str(str(detail['index'])+'\t' + e_withdraw.get()+'dr.\t'+str(detail['balance'])))
                    for i in detail['statement']:
                        # print(i,end='\n')
                        print(i)
                        tj.insert(INSERT, i + '\n')

                    tj.config(yscrollcommand=scroll.set)
                    tj.config(state='disabled')

                tj = Text(s, width=60, height=12, wrap='word')

                tj.grid(row=1, column=0, pady=300, padx=50)
                scroll = Scrollbar(s, orient=VERTICAL, command=tj.yview)
                scroll.grid(row=1, column=1, pady=300, sticky=N + S)
                # scroll.place(x=460,y=230)
                # tj.place(x=30,y=300)
                tj.config(state='disabled')
                # tj.config(state='disabled')
                global lab_balance
                detail = shelve.open(name)
                lab_ = ttk.Label(s, text='ACCOUNT DETAIL', font=('', 20)).place(x=130, y=18)
                lab_name3 = ttk.Label(s, text='Name    :' + detail['user_name'], font=('', 13)).place(x=90, y=50)
                lab_phone2 = ttk.Label(s, text='Phone   :' + detail['phone'], font=('', 13)).place(x=90, y=70)
                lab_email3 = ttk.Label(s, text='Email    :' + detail['email'], font=('', 13)).place(x=90, y=90)
                lab_dob = ttk.Label(s, text='D. O. B. :' + detail['dob'], font=('', 13)).place(x=90, y=110)
                lab_address = ttk.Label(s, text='Address :' + detail['address'], font=('', 13)).place(x=90, y=130)
                lab_Acc = ttk.Label(s, text='Acc. No. :' + detail['acc_num'], font=('', 13)).place(x=90, y=150)

                lab_balance = ttk.Label(s, text='Balance :' + str(detail['balance']), font=('', 13))
                lab_balance.place(x=90, y=170)
                b = ttk.Button(s, text='Deposit', command=lambda: deposit(name)).place(x=70, y=190)
                b1 = ttk.Button(s, text='With draw', command=withdraw).place(x=190, y=190)
                b11 = ttk.Button(s, text='statement', command=lambda: sat(name)).place(x=310, y=190)
                b_back = ttk.Button(s, text='Back', width=10, command=back_main).place(x=10, y=10)
                b_edit = ttk.Button(s, text='Edit Profile', width=10, command=lambda: edit(frame, name)).place(x=10,
                                                                                                               y=40)

                s.geometry('600x500')
                s.mainloop()
            else:
                messagebox.showinfo('ERROR', 'Incorrect Account no. or Password...\n   Try again!')
        else:
            messagebox.showinfo('ERROR', 'Incorrect Account no. or Password...\n   Try again!')
    else:
        messagebox.showinfo('ERROR', 'Wrong OTP...\n Try again!')


def back_main():
    s.state('withdraw')
    r.state('normal')


def send(x):
    global otp1
    s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number

    s.starttls()
    s.login("prashastineema@gmail.com", "Pn@52003")
    otp = random.randint(1000, 9999)
    otp1 = str(otp)

    s.sendmail("prashastineema@gmail.com", x, otp1)
    print("OTP sent succesfully..")
    # close smtp session
    s.quit()


def main():
    # main starting of program
    r.state('normal')
    global ent
    frame = LabelFrame(r, padx=100, pady=60)
    frame.pack(padx=100, pady=60)

    def otp(name):
        global e3
        print(name)
        detail = shelve.open(name)
        send(detail['email'])
        l5 = Label(frame, text='Check for OTP sent on your e-mail', fg='green')
        l5.grid(row=3, column=0, columnspan=2, sticky='W')
        l3 = Label(frame, text='OTP')
        l3.grid(row=2, column=0, sticky=W)
        e3 = Entry(frame)
        e3.grid(row=2, column=1)
        e3.focus_set()

        confirmbut = Button(frame, text='   LOGIN   ',
                            command=lambda: open1(ent.get(), e2.get(), frame, e3.get(), otp1))
        confirmbut.grid(row=4, column=0, columnspan=2)

    lab = Label(frame, text='Account No.')
    lab.grid(row=0, column=0, sticky=W)
    lab1 = Label(frame, text='Password')
    lab1.grid(row=1, column=0, sticky=W)

    # l4=Label(frame,text='')
    # l4.grid(row=3,column=0,sticky=W)

    ent = Entry(frame)
    ent.grid(row=0, column=1)
    e2 = Entry(frame)
    e2.grid(row=1, column=1)

    confirmbut = Button(frame, text='CONFIRM', command=lambda: otp(ent.get()))
    confirmbut.grid(row=4, column=0, columnspan=2)
    create = Button(frame, text='Create a New Account', command=lambda: new(frame))
    create.grid(row=5, column=0, columnspan=2)

    ent.focus_set()
    ent.bind('<Return>', open)
    r.geometry('600x400+100+50')


main()
r.mainloop()
