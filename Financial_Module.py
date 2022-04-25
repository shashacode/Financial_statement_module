import tkinter as tk
import pandas as pd
from pandas import DataFrame
from tabulate import tabulate
from tkinter.filedialog import askopenfilename

class FinStatement: 

    def __init__(self):

        self.doc =askopenfilename()
        
    def get_doc(self):
            
        doc = self.doc 

        df = pd.read_csv(doc)
    
        # return tabulate(df.values,df.columns, tablefmt="pipe")
        return df

    def get_date(self):
            
            while True:

                try:
                    g_doc = self.get_doc()
                    g_doc["Date"] = pd.to_datetime(g_doc["Date"])
            
                    date = str(input("Enter date of transaction needed in dd-mm-yy format: "))
                    dats = g_doc[g_doc["Date"] == "{}".format(date)]
                    dates = dats.drop(dats.columns[-2], axis=1)

                    # return dates

                    if dates.empty == True:
                        raise pd.errors.EmptyDataError('Empty DataFrame')
                    return dates
                    break
                except Exception as e:
                    print('There was an error in your input, please input a correct date')
                    
    

    def get_comment(self):
    
        while True:

            try:
                g_doc = self.get_doc()
                search = str(input("Enter whatever you need from the remark a Name, VAT etc:  "))
                group = g_doc[g_doc["Remarks"].str.upper().str.contains(search)]

                return group
                break

            except KeyError:
                print('Wrong input')
                

    def get_ref(self):
        
        while True:
            try:

                g_doc = self.get_doc()
                group = g_doc.groupby('Reference')
                ref = str(input("Enter reference number : " ))
                get = group.get_group(float(ref))

                # tabulated_values = tabulate(get.values,get.columns, tablefmt="pipe")
                return get
                
                break

            except KeyError:
                print('Wrong reference')

            except ValueError:
                print("it's a digit not a letter")
    
    def get_debit(self):
        
        while True:

            try:

                g_doc = self.get_doc()
                get = str(input('Enter debit amount :  ₦'))
                get_it = g_doc[g_doc.Debit == '{}'.format(get)]
            

                if get_it.empty == True:
                    raise pd.errors.EmptyDataError('Empty DataFrame')

                return get_it
                break
            except Exception as e:
                print('Amount not found, please try again')
                
    def get_credit(self):

        while True:

            try:

                g_doc = self.get_doc()
                get = str(input('Enter credit amount :  ₦'))
                get_cr = g_doc[g_doc.Credit == '{}'.format(get)]
                if get_cr.empty == True:
                    raise pd.errors.EmptyDataError('Empty DataFrame')
                return get_cr
                break
            except Exception as e:
                print('Amount not found, please try again')
            
        
    def get_bal(self):

        while True:

            try:

                g_doc = self.get_doc()
                get = str(input('Enter balance amount :  ₦'))
                get_it = g_doc[g_doc.Balance == '{}'.format(get)]
            
                if get_it.empty == True:
                    raise pd.errors.EmptyDataError('Empty DataFrame')
                return get_it
                break
            except Exception as e:
                print('Amount not found, please try again')

    def get_des(self):

        g_doc = self.get_doc()
        
        bal = g_doc['Balance'].str.replace(',', '').astype(float)
        d_bal = bal.mean().round()

        # This gets the average balance

        deb = g_doc['Debit'].str.replace(',', '').astype(float)
        d_deb = deb.mean().round()

        # This gets the average debit

        cred = g_doc['Credit'].str.replace(',', '').astype(float)
        d_cred = cred.mean().round()
        
        # This gets the average credit

        total_rows = len(g_doc)
        # This gets the number of rows

        g_doc['Date'] = pd.to_datetime(g_doc['Date'])

        min_date = g_doc['Date'].min()
        max_date = g_doc['Date'].max()

        # This gets the date

        print(f'The total number of transaction in this statement is {total_rows}')
        print(f'The statement is dated from {min_date} to {max_date}')
        print(f'The average balance of this statement is ₦{d_bal}')
        print(f'The average credit amount is ₦{d_cred}')
        print(f'The average debit amount is ₦{d_deb}')
        

    def menu(self):
        
        print('Enter A to access the document')
        print('Enter B to access any date')
        print('Enter C to access any Remark')
        print('Enter D to access a reference')
        print('Enter E to access a debit amount')
        print('Enter F to access a credit amount')
        print('Enter G to access any balance')
        print('Enter H to access the summary of the account')
        print('\n')

        Do = str(input('Choose an option :  '))

        if Do == 'A' or Do == 'a':
            # A = self.get_doc()
            A = tabulate(self.get_doc().values,self.get_doc().columns, tablefmt="pipe")
            print(A)
            print('\n')
        
        
            what = str(input('Type "Yes" to go back to the main menu : ')).title()
            if what == 'Yes':
                x.menu()
    
            elif what != 'Yes':
                print('You can only go back to the main menu')
                x.menu()

        elif Do == 'B' or Do == 'b':

            j = self.get_date()
            B = tabulate(j.values,j.columns, tablefmt="pipe",showindex=False)
            print(B)
            print('\n')
            
            while True:

                what = str(input('Would you like to search for another date?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_date())
                    #this recurses the question until it breaks

                elif what == 'No':
                    x.menu()

                elif what != 'Yes' and what != 'No':
                    print('input not recognized')
    
                else:
                    break
                
        elif Do == 'C' or Do == 'c':

            l = self.get_comment()
            C = tabulate(l.values,l.columns, tablefmt="pipe",showindex=False)
            print(C)
            print('\n')
            while True:

                what = str(input('Would you like to search for another comment?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_comment())
                    #this recurses the question until it breaks
                    
                elif what == 'No':
                    x.menu()

                elif what != 'Yes' and what != 'No':
                    print('input not recognized')

                else:
                    break
                
                
        elif Do == 'D' or Do == 'd':

            m = self.get_ref()
            D = tabulate(m.values,m.columns, tablefmt="pipe",showindex=False)
            print(D)
            print('\n')

            while True:

                what = str(input('Would you like to search for another reference?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_ref())
                    #this recurses the question until it breaks
                elif what == 'No':
                    x.menu()

                elif what != 'Yes' and what != 'No':
                    print('input not recognized')
                else:
                    break
                    
        elif Do == 'E' or Do == 'e':
            n = self.get_debit()
            E = tabulate(n.values,n.columns, tablefmt="pipe",showindex=False)
            print(E)
            print('\n')

            while True:

                what = str(input('Would you like to search for another debit?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_debit())
                    #this recurses the question until it breaks
                elif what == 'No':
                    x.menu()

                elif what != 'Yes'and what != 'No':
                    print('input not recognized')

                else:
                    break
                    
        elif Do == 'F' or Do == 'f':
            o = self.get_credit()
            F = tabulate(o.values,o.columns, tablefmt="pipe",showindex=False)
            print(F)
            print('\n')

            while True:

                what = str(input('Would you like to search for another credit?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_credit())
                    #this recurses the question until it breaks
                elif what == 'No':
                    x.menu()

                elif what != 'Yes' and what != 'No':
                    print('input not recognized')

                else:
                    break
                    
        elif Do == 'G' or Do == 'g':
            p = self.get_bal()
            G = tabulate(p.values,p.columns, tablefmt="pipe",showindex=False)
            print(G)
            print('\n')

            while True:

                what = str(input('Would you like to search for another balance?(Yes or no): ')).title()

                if what == 'Yes':
                    print(self.get_bal())
                    #this recurses the question until it breaks
                elif what == 'No':
                    x.menu()

                elif what != 'Yes' and what != 'No':
                    print('input not recognized')
                else:
                    break

        elif Do == 'H' or Do == 'h':
            z = self.get_des()
            H = tabulate(z.values,z.columns, tablefmt="pipe")
            print(H)
            print('\n')
        
        
            what = str(input('Type "Yes" to go back to the main menu : ')).title()
            if what == 'Yes':
                x.menu()
    
            elif what != 'Yes':
                print('You can only go back to the main menu')
                x.menu()
        elif Do != 'A' or Do != 'B' or Do != 'C' or Do != 'D' or Do != 'E' or Do != 'F'or Do != 'G' or Do != 'H':
            print('Option not recognized') 
            print('\n')
            x.menu()

print("Shasha's Bank Module!")
get_name = input("Please enter your name: ").title()
print("Welcome, {}".format(get_name))
print("\n")
print('Please open the icon that shows and select the file in the directory you want to read')

x = FinStatement()
x.menu()

