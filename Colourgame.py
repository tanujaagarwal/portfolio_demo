import tkinter as tk
from tkinter import messagebox as mb

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.correct = 0
        self.data_size = len(question)
        self.opt_selected = tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_title()
        self.display_question()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {wrong_count}"
        wrong = f"Wrong: {self.correct}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = tk.Button(gui, text="Next", command=self.next_btn,
                                width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

        quit_button = tk.Button(gui, text="Quit", command=gui.destroy,
                                width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=700, y=50)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = tk.Label(gui, text=question[self.q_no], width=60,
                        font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)
        self.display_options()

    def display_title(self):
        title = tk.Label(gui, text="QUIZ",
                         width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(gui, text="", variable=self.opt_selected,
                                       value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

# Create a GUI Window
gui = tk.Tk()
gui.geometry("800x450")
gui.title("GeeksforGeeks Quiz")

# Sample questions and answers
question = [
    "What is the capital of France?",
    "Which programming language is used for web development?",
    "What is the largest planet in our solar system?",
    "Who is the CEO of SpaceX?",
    "Who painted the Mona Lisa?",
    "What is the smallest country in the world?",
    "Who wrote Romeo and Juliet?",
    "What is the chemical symbol for gold?",
    "What is the largest living species of lizard?",
    "What is the capital of Austrailia?",
    "What is the largest mammal on Earth?",
    "What is the capital of China?",
    "What is the largest city in South America?",
    "In what year was the first iPhone released?",
    "What is the tallest mountain in the world?",
    "Which planet is known as the Red Planet?",
    "Who discovered electricity?",
    "What is the world's largest ocean?",
    "Who came up with the theory of relativity?",
    "What language is spoken in Brazil?",
    "What is the main ingredient in hummus?",
    "In what year did the Great October Socialist Revolution take place?",
    "What is the largest lake in the world?",
    "Who wrote the novel War and Peace?",
    "Which gas is used to extinguish fire?",
    "Hitler's party is known as:",
    "Which is the largest island?",
    "What is the phobia of thunder and rain?",
    "What does Carpe Diem mean in Latin?",
    "When the humans use more facial muscles?",
    "What animal is a symbol of peace and neutrality?",
    "Which river is the second longest in the world?",
    "Fathometer is used to measure",
    "Which actor portrayed James Bond in a record seven movies?",
    "How many teeth does an adult dog have?",
    "Which of these buildings is in India?"
    ]

options = [
    ["Paris", "London", "Berlin", "Rome"],
    ["Python", "Java", "C++", "JavaScript"],
    ["Earth", "Saturn", "Jupiter", "Uranus"],
    ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Bill Gates"],
    ["Leonardo da Vinci","Michelangelo","Raphael","Caravaggio"],
    ["Vatican City","Monaco","Nauru","Tuvalu"],
    ["William Shakespeare","Jane Austen","Charles Dickens","J.K. Rowling"],
    ["Ag","Au","Hg","Pb"],
    ["Komodo Dragon","Saltwater crocodile","Black mamba","African elephant"],
    ["Sydney","Melbourne","Canberra","Perth"],
    ["Blue whale","African elephant","Hippopotamus","Rhinoceros"],
    ["Beijing","Shanghai","Guangzhou","Hong Kong"],
    ["Sao Paulo","Buenos Aires","Lima","Bogota"],
    ["2005","2007","2008","2010"],
    ["K2","Mount Everest","Mount Kilimanjaro","Denali"],
    ["Venus","Mars","Jupiter","Saturn"],
    ["Isaac Newton","Nikola Tesla","Michael Faraday","Benjamin Franklin"],
    ["Atlantic Ocean","Indian Ocean","Pacific Ocean","Southern Ocean"],
    ["Edgar Allan Poe","Albert Einstein","Galileo Galilei","Louis Pasteur"],
    ["Spanish","Portuguese","English","French"],
    ["Potatoes","Lentils","Chickpeas","White Beans"],
    ["1917","1923","1914","1920"],
    ["Caspian Sea","Baikal","Lake Superior","Ontario"],
    ["Anton Chekhov","Fyodor Dostoevsky","Leo Tolstoy","Ivan Turgenev"],
    ["Oxygen","Nitrogen","Carbon dioxide","Hydrogen"],
    ["Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party"],
    ["New Guinea","Andaman Nicobar","Greenland","Hawaii"],
    ["Astraphobia","Ombrophobia","Acrophobia","Claustrophobia"],
    ["Enjoy the moment", "Have no fear","Sorry I blew it","Hello"],
    ["While smiling","While frowning","While sleeping","While talking"],
    ["Polar bear","White tiger","White lion","White crane"],
    ["Amazon","Yangtze","Nile","Mississippi"],
    ["Earthquakes","Rainfall","Ocean depth","Sound intensity"],
    ["Brad Pitt", "Daniel Craig", "Pierce Brosnan","Roger Moore"],
    ["32","34","38","42"],
    ["Eiffel Tower","Colosseum","Taj Mahal","Great Wall of China"],
    
]
answer = [0, 3, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 1, 1, 3, 2, 1, 1, 2, 0, 1, 2, 2, 1, 2, 0, 0, 3, 3, 0, 2, 3, 3, 2]

# Create an object of the Quiz Class.
quiz = Quiz()

# Initialize the GUI
quiz.display_title()
quiz.display_question()

# Start the GUI
gui.mainloop()