import re

# 対象の文字列
text = """
7:11

高槻市立安岡寺小学校
〒569-1029 大阪府高槻市安岡寺町１丁目６０−１
徒歩徒歩


約 3 分、190 m
7:14
学園前（バス）
バス５系統（高槻）ＪＲ高槻駅北行


8 分
（8 駅）
7:22
芥川商店街（バス）
徒歩徒歩


約 6 分
7:33
高槻駅
電車東海道・山陽本線快速姫路行


13 分
（2 駅）
· 乗換地点 ID: JR-A38
7:46
新大阪駅
徒歩徒歩


約 2 分
7:53
新大阪駅
電車おおさか東線各停久宝寺行


25 分
（8 駅）
· 1 番ホーム · 乗換地点 ID: A46
8:18
ＪＲ河内永和駅
徒歩徒歩


約 6 分、400 m
8:24

〒577-0809 大阪府東大阪市永和２丁目７−３０
"""

# 駅名の変換処理
def convert_station_name(station_name):
    # 「（バス」を「バス停」に置き換え
    return station_name.replace("（バス", "バス停")

# 正規表現
pattern = r"\d{1,2}:\d\d[\s]*[\S]*[駅バス]"

# 抽出
lines = re.findall(pattern, text)



formatted_lines = []
    # 時間行に全角スペースを追加し、次の行と結合
for i in range(0, len(lines)):
    temp = lines[i].splitlines()

    if i % 2 == 0:
        time = temp[0].strip() + "発" # 時間
    else:
        time = temp[0].strip() + "着"

    station = temp[1].strip()  # 駅名
    station = convert_station_name(temp[1].strip())  # 駅名変換
    formatted_lines.append(f"{time}　{station}")  # 全角スペースで結合
    result = '\n'.join(formatted_lines)

for fline in formatted_lines:
    print(fline)
