# Multi-challenge Sololearn with Grafic Interface
# v0.1

# import grafic modules
from tkinter import *
from tkinter import ttk


# The Spy Life
# Remove all symbols and numerals from the text and invert its sequence
def spy_life(x):
    message = x.split()
    out = []

    for i in message:
        j = re.sub("[^a-zA-Z]", "", i)
        out.append(j)

    return " ".join(out)[::-1]


# Symbols
# Remove all symbols from the text, it keeps the numerals
def symbols(x):
    words = x.split()
    out = []

    for i in words:
        j = re.sub("[^a-zA-Z0-9]", "", i)
        out.append(j)

    return " ".join(out)


# Extra-Terrestrials
# Invert the text sequence
def et(x):
    return x[::-1]


# Pig Latin
# Send the first letter to the end of the word and add -ay in the end
def pig_latin(x):
    palavra = x.split()
    result = []

    for i in palavra:
        j = 0
        k, temp = [], []
        while j < len(i):
            if j == 0:
                temp = i[j]
            else:
                k.append(i[j])
            j += 1
        k.append(temp)
        k.append("ay")
        result.append("".join(k))
    return " ".join(result)


class Tradutor:

    def __init__(self, master):

        master.title('MTC SOLOLEARN')
        master.resizable(False, False)

        self.notebook = ttk.Notebook(master)
        self.notebook.pack()

        self.frame_main = ttk.Frame(self.notebook)
        self.frame_about = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_main, text='Main')
        self.notebook.add(self.frame_about, text='About')

        ttk.Label(self.frame_about, text='Challenges Description:\n\n'
                                         'Extra-Terrestrials:\n Invert the text sequence\n\n'
                                         'Pig Latin:\n'
                                         'Send the first letter to the end of the word and add -ay in the end\n\n'
                                         'The Spy Life:\n'
                                         'Remove all symbols and numerals from the text and invert its sequence\n\n'
                                         'Symbols:\n Remove all symbols from the text, it keeps the numerals'
                                         '\n\n', width=55, wraplength=340).pack(padx=5, anchor='w')

        self.frame_challenges = ttk.Frame(self.frame_main)
        self.frame_challenges.pack(padx=5, pady=2)
        self.frame_challenges.config(relief=SUNKEN)

        ttk.Label(self.frame_challenges, text='Choose the Challenge:').grid(row=0, column=0, padx=2, pady=2)

        self.challenge = StringVar()

        ttk.Radiobutton(self.frame_challenges, text='Extra-Terrestrials', variable=self.challenge, value='Et'
                        ).grid(row=1, column=0, padx=2, pady=2)
        ttk.Radiobutton(self.frame_challenges, text='Pig Latin', variable=self.challenge, value='Pig'
                        ).grid(row=1, column=1, padx=2, pady=2)
        ttk.Radiobutton(self.frame_challenges, text='Spy Life', variable=self.challenge, value='Spy'
                        ).grid(row=1, column=2, padx=2, pady=2)
        ttk.Radiobutton(self.frame_challenges, text='Symbols', variable=self.challenge, value='Sym'
                        ).grid(row=1, column=3, padx=2, pady=2)

        ttk.Label(self.frame_main, text='Insert your message:').pack(padx=5, anchor='w')

        self.message = Text(self.frame_main, width=48, height=4, font=('Arial', 10))
        self.message.pack(padx=5, pady=2)

        self.frame_buttons = ttk.Frame(self.frame_main)
        self.frame_buttons.pack(padx=5, pady=2)

        ttk.Button(self.frame_buttons, text='Translate', command=self.traduzir).grid(row=0, column=0, pady=5)
        ttk.Button(self.frame_buttons, text='Clear', command=self.clear).grid(row=0, column=1, pady=5)

        ttk.Label(self.frame_main, text='Result:').pack(padx=5, anchor='w')

        self.frame_result = ttk.Frame(self.frame_main)
        self.frame_result.pack(padx=5, pady=2)

        self.result = StringVar()
        self.traducao = ttk.Label(self.frame_result, textvariable=self.result, width=55, wraplength=340)
        self.traducao.grid(row=0, column=0, padx=5, sticky='w')

    def traduzir(self):

        if self.challenge.get() == 'Et':
            self.result.set(et(self.message.get(1.0, 'end')))
        elif self.challenge.get() == 'Pig':
            self.result.set(pig_latin(self.message.get(1.0, 'end')))
        elif self.challenge.get() == 'Spy':
            self.result.set(spy_life(self.message.get(1.0, 'end')))
        elif self.challenge.get() == 'Sym':
            self.result.set(symbols(self.message.get(1.0, 'end')))

            self.message.delete(1.0, 'end')

    def clear(self):
        self.message.delete(1.0, 'end')
        self.result.set('')


def main():
    root = Tk()
    Tradutor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
