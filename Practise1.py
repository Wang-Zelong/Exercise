# 1. Ask user to enter a string and check that it is made up only alphabets:
# 获取用户输入
user_input = input("请输入一个字符串：")
# 初始化标志变量，用于标记是否所有字符都是字母
all_letters = True
# 遍历字符串中的每个字符
for char in user_input:
    # 检查字符是否在字母的ASCII码范围内
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
        all_letters = False
        break  # 如果发现非字母字符，立即停止检查
# 根据标志变量打印结果
if all_letters and user_input:  # 确保字符串不为空
    print("输入的字符串仅由字母组成。")
else:
    print("输入的字符串包含非字母字符或为空。")

# 2. Now, make sure that the string is made up of both alphabets and numbers:
#    TRY using isalnum() function and then entering only alhpabets in the string and see what happens.
# 获取用户输入
user_input = input("请输入一个字符串：")
# 检查字符串是否仅由字母和数字组成
if user_input.isalnum():
    print("输入的字符串仅由字母和数字组成。")
else:
    print("输入的字符串包含非字母数字字符。")

# 3. Now, make sure that the string is made up of both alphabets and at least one number:
# 获取用户输入
user_input = input("请输入一个字符串：")
# 初始化字母和数字的计数器
letter_count = 0
digit_count = 0
# 检查字符串是否符合条件
for char in user_input:
    if char.isalpha():  # 如果字符是字母
        letter_count += 1
    elif char.isdigit():  # 如果字符是数字
        digit_count += 1
# 确保字符串至少有两个字母和至少一个数字
if letter_count >= 2 and digit_count >= 1:
    print("输入的字符串符合条件：至少有两个字母和至少一个数字。")
else:
    print("输入的字符串不符合条件：需要至少两个字母和至少一个数字。")

# 4. Now, make sure that the string is made up of both alphabets, at least one number, and at least one special character:1
# 获取用户输入
user_input = input("请输入一个字符串：")
# 初始化字母、数字和特殊字符的计数器
letter_count = 0
digit_count = 0
special_char_count = 0
# 检查字符串是否符合条件
for char in user_input:
    if char.isalpha():  # 如果字符是字母
        letter_count += 1
    elif char.isdigit():  # 如果字符是数字
        digit_count += 1
    elif not char.isspace():  # 如果字符不是空格也不是字母或数字，则视为特殊字符
        special_char_count += 1
# 确保字符串至少有两个字母、至少一个数字和至少一个特殊字符
if letter_count >= 2 and digit_count >= 1 and special_char_count >= 1:
    print("输入的字符串符合条件：至少有两个字母、至少一个数字和至少一个特殊字符。")
else:
    print("输入的字符串不符合条件：需要至少两个字母、至少一个数字和至少一个特殊字符。")

# 5. Now, modify the above code so that if the user enters an invalid string, the program should ask the user to enter another string again, and keep asking until a valid string has been entered.
while True:
    # 获取用户输入
    user_input = input("请输入一个字符串：")
    # 初始化字母、数字和特殊字符的计数器
    letter_count = 0
    digit_count = 0
    special_char_count = 0
    # 检查字符串是否符合条件
    for char in user_input:
        if char.isalpha():  # 如果字符是字母
            letter_count += 1
        elif char.isdigit():  # 如果字符是数字
            digit_count += 1
        elif not char.isspace():  # 如果字符不是空格也不是字母或数字，则视为特殊字符
            special_char_count += 1
    # 确保字符串至少有两个字母、至少一个数字和至少一个特殊字符
    if letter_count >= 2 and digit_count >= 1 and special_char_count >= 1:
        print("输入的字符串符合条件：至少有两个字母、至少一个数字和至少一个特殊字符。")
        break  # 跳出循环
    else:
        print("输入的字符串不符合条件：需要至少两个字母、至少一个数字和至少一个特殊字符。请再次输入。")