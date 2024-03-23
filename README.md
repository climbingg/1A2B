# 1A2B程式解

## 環境

- 使用python的3.12.1
- 無須安裝任何第三方庫

## 使用說明

- 有兩個檔案，一個是[1A2B_3.py](1A2B_3.py)，另一個是[1A2B_4.py](1A2B_4.py)
- 打大小寫沒差，程式會自動處理

## 演算法說明

- 使用掃描後找到9種可能的分別的數量(但是要去除3a0b，因為3a0b等於獲勝)
- 以下9種

```plaintext
0A0B
0A1B
0A2B
0A3B
1A0B
1A1B
1A2B
2A0B
3A0B
```

- 1A2B的4位數版本的演算法也只是換湯不換藥，這裡就不列了(4位數有13種可能，4a0b才是獲勝)
- 從all_num的第0項一個一個找，把所有的種類後面都初始化為0，把opposite_num一個一個檢查，檢查all_num[i]和opposite_num[j]是9種的哪一種，檢查完所有的opposite_num之後，把3a0b的去掉後，把8種的各自數量的平方全部家在一起得到分數，再從all_num[i]之中，找到all_num[i]會得到最小的分數，選擇猜all_num[i]
- 以下是程式碼示意

```python
opposite_num = all_num.copy()
all_score = []
for i in range(len(all_num)):
    score = 0
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
    for j in range(len(opposite_num)):
        every_answer[get_many_a_many_b(all_num[i], opposite_num[j])] += 1
    for answer, num in every_answer:
        if answer == "3A0B":
            continue
        score += num
    all_score.append((i, score))
t = min(all_score, key=lambda x: x[1])
print(f"該猜{all_num[t[0]]}")
```

## 使用須知

- 其實機器人不具有直接檢查你的回答真實性的功能，只能夠最後如果發現你每次的回答無法出現任何一個數字的時候，才能檢查，同時程式就會被中斷，例如請看以下範例

```plaintext
你的回答有誤!!!!
第1次我猜453你回答0A1B
第2次我猜561你回答2A0B
第3次我猜867你回答0A0B
第4次我猜521你回答2A0B
第5次我猜591你回答0A1B
請仔細檢查你的回答!!
```

## 感言

- 以上1A2B程式是受到自己啟發
- 以上演算法都是自己想到的
- 以上程式碼除了語法支持，沒有任何問Chatgpt的部分
