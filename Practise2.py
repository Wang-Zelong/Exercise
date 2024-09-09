# 使用 enumerate() 方法
str1 = "Howl's Moving Castle"
for index, char in enumerate(str1):
    print(index, char)

# 使用 join() 方法
some_list = ['Baa', 'baa', 'black', 'sheep']
joined_string = ' '.join(some_list)
print(joined_string)

# 使用 random.choice() 方法
import random
some_list = ['Baa', 'baa', 'black', 'sheep']
random_choice = random.choice(some_list)
print(random_choice)