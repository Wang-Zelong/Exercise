import random

def hangman_game():
    print("欢迎来到Hangman游戏！")
    words = ["apple", "banana", "cherry", "date", "fig", "grape"]  # 单词列表
    chosen_word = random.choice(words)  # 随机选择一个单词
    display = '_' * len(chosen_word)  # 初始化显示为下划线
    attempts = 10  # 初始尝试次数
    guessed_letters = []  # 记录已猜字母

    while attempts > 0:
        print(f"\n剩余尝试次数：{attempts}")
        print(f"当前单词状态：{display}")
        guess = input("请猜一个字母：").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("无效字符，请重新输入一个字母。")
            continue

        if guess in guessed_letters:
            print("你已经猜过这个字母了，请重新输入。")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("正确！")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display = display[:i] + guess + display[i+1:]
            if display == chosen_word:
                print("太棒了！你猜对了单词：", chosen_word)
                break
        else:
            print("错误！")
            attempts -= 1
            display = '_' * len(chosen_word)  # 重置显示为下划线

    if display == chosen_word:
        print("谢谢你玩。下次见")
    else:
        print("谢谢您玩。下次好运")

if __name__ == "__main__":
    hangman_game()