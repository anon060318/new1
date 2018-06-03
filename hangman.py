def hangman(word):
    wrong_count = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rest_letters = list(word)
    display_board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong_count < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rest_letters:
            print("アタリ！")
            char_position = rest_letters.index(char)
            display_board[char_position] = char
            rest_letters[char_position] = "$"
        else:
            print("ハズレ！")
            wrong_count += 1
        print(" ".join(display_board))
        e = wrong_count + 1
        print("\n".join(stages[0:e]))
        if "_" not in display_board:
            print("あなたの勝ち！")
            print(" ".join(display_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong_count+1]))
        print("あなたの負け！正解は {}.".format(word))
