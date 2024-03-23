import random


def filter_opposite_num(opposite_num: set[str], many_a_b: str, num: str):
    a = int(many_a_b[0])
    b = int(many_a_b[2])
    a_b = (a, b)
    list_opposite_num = list(opposite_num)
    for i in list_opposite_num:
        if a_b != response_user(num, i):
            opposite_num.remove(i)


def filted_num(num: str) -> bool:
    if "0" in num:
        return False
    return len(set(num)) == 3


def response_user(num: str, guess_num: str):
    a = 0
    b = 0
    for i in range(3):
        if num[i] == guess_num[i]:
            a += 1
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if num[i] == guess_num[j]:
                b += 1
    return a, b


def decide_which_one_to_guess(not_guessed_num: set[str], oppsite_num: set[str]) -> str:
    ret = None
    if len(oppsite_num) == 504:
        ret = random.choice(list(oppsite_num))
        not_guessed_num.remove(ret)
        return ret
    min_score_and_str_set = [1e9, set()]
    for i in not_guessed_num:
        every_answer = {
            "0A0B": 0,
            "0A1B": 0,
            "0A2B": 0,
            "0A3B": 0,
            "1A0B": 0,
            "1A1B": 0,
            "1A2B": 0,
            "2A0B": 0,
            "3A0B": 0,
        }
        for j in oppsite_num:
            response = response_user(i, j)
            every_answer[str(response[0]) + "A" + str(response[1]) + "B"] += 1
        score = 0
        for j in every_answer:
            if j == "3A0B":
                continue
            score += every_answer[j] ** 2
        if score < min_score_and_str_set[0]:
            min_score_and_str_set[0] = score
            min_score_and_str_set[1].clear()
            min_score_and_str_set[1].add(i)
        elif score == min_score_and_str_set[0]:
            min_score_and_str_set[1].add(i)
    ret = random.choice(list(min_score_and_str_set[1]))
    not_guessed_num.remove(ret)
    return ret


def user_guess(self_num, all_num, every_reponse, opposite_num, first_or_after):
    opposite_guess_num = input("你要猜什麼數字?:")
    while opposite_guess_num not in all_num:
        opposite_guess_num = input("你要猜什麼數字?(只能猜三位數,不能重複,不能有0):")
    response = response_user(self_num, opposite_guess_num)
    print(f"你猜的結果是{response[0]}A{response[1]}B")
    if response == (3, 0):
        if first_or_after == "a":
            print("你贏了!!")
        else:
            print("因為你是先猜的人，所以我可以在猜一次，猜對了的話就平手!!")
            will_guess_num = random.choice(list(opposite_num))
            user_reponse = input(f"我猜{will_guess_num},請問幾A幾B?:").upper()
            while user_reponse not in every_reponse:
                user_reponse = input(
                    f"你的輸入格式不正確\n只能輸入以下9種:\n0A0B\n0A1B\n0A2B\n0A3B\n1A0B\n1A1B\n1A2B\n2A0B\n3A0B\n我猜{will_guess_num},請問幾A幾B?:"
                ).upper()
            if user_reponse == "3A0B":
                print("平局!!!!")
        return True
    return False


def main():
    every_reponse = {
        "0A0B",
        "0A1B",
        "0A2B",
        "0A3B",
        "1A0B",
        "1A1B",
        "1A2B",
        "2A0B",
        "3A0B",
    }
    ai_guess_answer = []
    all_num = list(range(123, 988))
    all_num = list(map(str, all_num))
    all_num = set(filter(filted_num, all_num))
    self_num = random.choice(list(all_num))
    opposite_num = all_num.copy()
    not_guessed_num = all_num.copy()
    first_or_after = input("你要先猜還是後猜?(f先猜,a後猜):")
    while first_or_after not in ["f", "a"]:
        first_or_after = input("你要先猜還是後猜?(f先猜,a後猜(只能輸入f或a)):")
    if first_or_after == "f":
        if user_guess(self_num, all_num, every_reponse, opposite_num, first_or_after):
            return None

    while True:
        will_guess_num = decide_which_one_to_guess(not_guessed_num, opposite_num)
        user_reponse = input(f"我猜{will_guess_num},請問幾A幾B?:").upper()
        while user_reponse not in every_reponse:
            user_reponse = input(
                f"你的輸入格式不正確\n只能輸入以下9種:\n0A0B\n0A1B\n0A2B\n0A3B\n1A0B\n1A1B\n1A2B\n2A0B\n3A0B\n我猜{will_guess_num},請問幾A幾B?:"
            ).upper()
        ai_guess_answer.append((will_guess_num, user_reponse))
        filter_opposite_num(opposite_num, user_reponse, will_guess_num)
        if len(opposite_num) == 0:
            print("\n\n你的回答有誤!!!!")
            for i, t in enumerate(ai_guess_answer):
                j, k = t
                print(f"第{i + 1}次我猜{j}你回答{k}")
            print("請仔細檢查你的回答!!")
            return None
        if user_reponse == "3A0B":
            if first_or_after == "f":
                print("你輸了......")
                print(f"公布答案:{self_num}")
            else:
                print("因為你是後猜的人，所以你可以在猜一次，猜對了的話就平手!!")
                opposite_guess_num = input("你要猜什麼數字?:")
                while opposite_guess_num not in all_num:
                    opposite_guess_num = input("你要猜什麼數字?(只能猜三位數,不能重複,不能有0):")
                if opposite_guess_num == self_num:
                    print("你猜對了，你和我平手了!!")
                else:
                    print("你輸了......")
                    print(f"公布答案:{self_num}")
            break
        if user_guess(self_num, all_num, every_reponse, opposite_num, first_or_after):
            return None


main()
