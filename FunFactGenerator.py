import tkinter as tk
import random

class FunFactGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Fact Generator")
        self.facts = [
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896, and lasted only 38 minutes.",
            "The longest word in the English language, according to the Oxford English Dictionary, is pneumonoultramicroscopicsilicovolcanoconiosis, a lung disease caused by inhaling very fine particles of silica.",
            "Butterflies taste with their feet.",
            "A group of flamingos is called a 'flamboyance' of flamingos.",
            "The Great Wall of China is visible from space.",
            "There are more stars in the universe than there are grains of sand on all the beaches on Earth.",
            "The human nose can detect over 1 trillion different scents.",
            "The world's largest living organism is a fungus that covers over 2,200 acres in Oregon, USA.",
            "The shortest verse in the Bible is John 11:35, which reads, 'Jesus wept.'",
            "The longest recorded flight of a chicken is 13 seconds.",
        ]

        self.fact_label = tk.Label(root, text="", wraplength=400)
        self.fact_label.pack(pady=20)

        self.generate_button = tk.Button(root, text="Generate Fun Fact", command=self.generate_fact)
        self.generate_button.pack(pady=20)

    def generate_fact(self):
        fact = random.choice(self.facts)
        self.fact_label.config(text=fact)

if __name__ == "__main__":
    root = tk.Tk()
    app = FunFactGenerator(root)
    root.mainloop()



    
