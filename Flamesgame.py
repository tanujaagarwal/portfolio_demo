import tkinter as tk

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

def calculate_flames():
    p1 = player1_entry.get().lower().replace(" ", "")
    p2 = player2_entry.get().lower().replace(" ", "")
    p1_list = list(p1)
    p2_list = list(p2)
    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]
    result_label.config(text="Relationship status: " + result[0])

def restart_game():
    player1_entry.delete(0, tk.END)
    player2_entry.delete(0, tk.END)
    result_label.config(text="")

def adjust_size(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.5)
    height = int(screen_height * 0.5)
    root.geometry(f"{width}x{height}")

root = tk.Tk()
root.title("FLAMES Game")

adjust_size(root)

player1_label = tk.Label(root, text="Player 1 name:")
player1_label.pack()
player1_entry = tk.Entry(root, width=20)
player1_entry.pack()

player2_label = tk.Label(root, text="Player 2 name:")
player2_label.pack()
player2_entry = tk.Entry(root, width=20)
player2_entry.pack()

calculate_button = tk.Button(root, text="Calculate FLAMES", command=calculate_flames, bg="green", fg="white")
calculate_button.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game, bg="red", fg="white")
restart_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()