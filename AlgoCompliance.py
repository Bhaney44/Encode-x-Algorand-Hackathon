# Copyright Fortior Blockchain, LLLP 2022
# Automated Compliance on Algorand
# Apache License

# Widgets:
from tkinter import *
from tkinter.messagebox import *

# Natural Language Ratings
natural_language_compression = {'good':0.75, 'acceptable':0.5, 'outstanding': 1, 'unacceptable': 0, 'marginal': .25}

# Frontend
## The frontend is a simple user interface.
master = Tk()
# Factor 1 Equity: An asset is less likely to be a security if it does not represent an equity interest in a company.
label0 = Label(master, text = 'Equity', relief = 'groove', width = 12)
# Factor 2 Decentralization: An asset is less likely to be a security if it is decentralized.
label1 = Label(master, text = 'Decentralization', relief = 'groove', width = 12)
# Factor 3 Participation: An asset is less likely to be a security if users earn the asset through participation.
label2 = Label(master, text = 'Participation', relief = 'groove', width = 12)
# Factor 4 Investment: An asset is less likely to be a security if it is not marketed or sold as an investment.
label3 = Label(master, text = 'Investment', relief = 'groove', width = 12)
# Factor 5 Utility: An asset is less likely to be a security if has a specific utility.
label4 = Label(master, text = 'Utility', relief = 'groove', width = 12)
# Factor 6 Purpose: An asset is less likely to be a security if the asset has an intended purpose for use aside from financial return.
label5 = Label(master, text = 'Purpose', relief = 'groove', width = 12)
# Factor 7 Control: An asset is less likely to be a security if the asset gives the user control over an organizations decision making.
label6 = Label(master, text = 'Control', relief = 'groove', width = 12)
# Factor 8 Derivatives: An asset is less likely to be a security if it does not offer users derivatives or returns.
label7 = Label(master, text = 'Derivatives', relief = 'groove', width = 12)
# Factor 9 Commonality: An asset is less likely to be a security if it is not dedicated to the furtherance of a common enterprise.
label8 = Label(master, text = 'Commonality', relief = 'groove', width = 12)
# Compliance Score provides a statistical measure of the likelyhood an asset is a security.
# The statistical analysis is set such that 1.0 is least likely to be a security and 0.0 is most likely to be a security.
label9 = Label(master, text = 'Compliance Score', relief = 'groove', width = 20)
entry0 = Entry(master, relief = 'groove', width = 12)
entry1 = Entry(master, relief = 'groove', width = 12)
entry2 = Entry(master, relief = 'groove', width = 12)
entry3 = Entry(master, relief = 'groove', width = 12)
entry4 = Entry(master, relief = 'groove', width = 12)
entry5 = Entry(master, relief = 'groove', width = 12)
entry6 = Entry(master, relief = 'groove', width = 12)
entry7 = Entry(master, relief = 'groove', width = 12)
entry8 = Entry(master, relief = 'groove', width = 12)
blank0 = Entry(master, relief = 'groove', width = 20)

# Backend
# The backend is an artificial intelligence (AI) program for automating compliance analysis.
# The AI program uses an embedded knowledge and a geometric mean to capture human intuition and provide intelligent analysis.
def compliance_ai():
    intuition = 1/9
    knowledge = float(natural_language_compression[entry0.get()]) * float(natural_language_compression[entry1.get()]) * float(natural_language_compression[entry2.get()]) *float(natural_language_compression[entry3.get()]) * float(natural_language_compression[entry4.get()]) * float(natural_language_compression[entry5.get()]) * float(natural_language_compression[entry6.get()]) * float(natural_language_compression[entry7.get()]) * float(natural_language_compression[entry8.get()])
    intelligence = float(knowledge) ** intuition
    blank0.insert(0, intelligence)
button0 = Button(master, text = 'Calculate ASA Compliance', relief = 'groove', width = 25, command =compliance_ai)

# Frontend
## The frontend is a simple user interface.
label0.grid( row = 1, column = 1, padx = 10 )
label1.grid( row = 2, column = 1, padx = 10 )
label2.grid( row = 3, column = 1, padx = 10 )
label3.grid( row = 4, column = 1, padx = 10 )
label4.grid( row = 5, column = 1, padx = 10 )
label5.grid( row = 6, column = 1, padx = 10 )
label6.grid( row = 7, column = 1, padx = 10 )
label7.grid( row = 8, column = 1, padx = 10 )
label8.grid( row = 9, column = 1, padx = 10 )
label9.grid( row = 2, column = 3, padx = 10 )
entry0.grid( row = 1, column = 2, padx = 10 )
entry1.grid( row = 2, column = 2, padx = 10 )
entry2.grid( row = 3, column = 2, padx = 10 )
entry3.grid( row = 4, column = 2, padx = 10 )
entry4.grid( row = 5, column = 2, padx = 10 )
entry5.grid( row = 6, column = 2, padx = 10 )
entry6.grid( row = 7, column = 2, padx = 10 )
entry7.grid( row = 8, column = 2, padx = 10 )
entry8.grid( row = 9, column = 2, padx = 10 )
blank0.grid( row = 3, column = 3, padx = 10 )
button0.grid( row = 4, column = 3, columnspan = 2)

# Software Title
master.title('Automated Compliance on Algorand')
