import re
import tkinter as tk
from tkinter import messagebox

def process_text():
    input_text = text_area.get("1.0", tk.END)  # テキストエリアの内容を取得

    # 正規表現
    pattern = r"\d{1,2}:\d\d\n.+\n.+線?"

    # 抽出
    lines = re.findall(pattern, input_text)

    print(lines)
    # # 処理を行うコード
    # lines = matches.splitlines()  # 改行で分割
    formatted_lines = []

    # 駅名の変換処理
    def convert_station_name(station_name):
    # 特定の駅名を置き換える
        if "学園前" in station_name:
            return "高槻市営バス　学園前バス停"
        elif "芥川商店街" in station_name:
            return "高槻市営バス　芥川商店街バス停"
        elif "高槻駅" in station_name:
            return "JR京都線　高槻駅"
        else:
            return station_name
        # else:
        #     # その他の場合は「（バス」を「バス停」に置き換え
        #     return station_name.replace("（バス", "バス停")

    previous_kind = ""
    previous_station = ""
    # 時間行に全角スペースを追加し、次の行と結合
    for i in range(0, len(lines)):
        temp = lines[i].splitlines()

        if i == 0:
            time = temp[0]
        elif i == len(lines)-1:
            time = temp[0]
        elif i % 2 != 0:
            time = temp[0].strip() + "発" # 時間
        else:
            time = temp[0].strip() + "着"

        station = temp[1].strip()  # 駅名
        station = convert_station_name(temp[1].strip())  # 駅名変換

        if "徒歩" in temp[2]:
            kind = previous_kind
            if "JR京都線　高槻駅" in previous_station:
                kind = "　JR京都線"
        elif "高槻市立安岡寺小学校" in temp[2]:
            kind = "　　自宅発"
        elif "学園前バス停" in station or "芥川商店街バス停" in station:
            kind = ""
        elif "高槻駅" in station:
            previous_station = station
            kind = ""
        elif "線" in temp[2]:
            temp[2].replace("地下鉄", "")
            kind = "　" + temp[2][:temp[2].index("線") + 1]
        elif temp[2] is not None:
            kind = "　" + temp[2]
            # print("*****None detected*****")
        else:
            kind = "　"
            # print("*******else used*******")

        if i is len(lines) - 1:
            kind = "　　現地着"
        previous_station = station
        previous_kind = kind
        formatted_lines.append(f"{time}{kind}　{station}")  # 全角スペースで結合
        result = '\n'.join(formatted_lines)

    # 出力
    print(result)

    result_area.config(state="normal")  # 編集可能に設定
    result_area.delete("1.0", tk.END)  # 古い内容を削除
    result_area.insert("1.0", result)  # 結果を挿入
    result_area.config(state="disabled")  # 編集不可に設定

    # 結果をクリップボードにコピー
    root.clipboard_clear()  # クリップボードをクリア
    root.clipboard_append(result)  # クリップボードに結果を設定
    root.update()  # クリップボード更新
    print("結果をクリップボードにコピーしました")  # 確認メッセージ



# 貼り付けボタン
def paste_from_clipboard():
    try:
        # クリップボードの内容を取得
        clipboard_text = root.clipboard_get()
        text_area.insert("1.0", clipboard_text)  # テキストエリアに貼り付け
    except tk.TclError:
        # クリップボードが空の場合のエラーハンドリング
        text_area.insert("1.0", "クリップボードが空です")


# テキストエリア削除ボタン
def clear_text_area():
    # テキストエリアの内容を削除
    text_area.delete("1.0", tk.END)


# ウィンドウ作成
root = tk.Tk()
root.title("テキスト処理アプリ")
root.geometry("600x400+1300+100")

# クリアボタン
clear_button = tk.Button(root, text="テキストエリアをクリア", command=clear_text_area,bg="lightpink1")
clear_button.pack(side=tk.BOTTOM, ipadx=25, pady=3)

# ボタン
process_button = tk.Button(root, text="処理", command=process_text,bg="lightblue1")
process_button.pack(side=tk.BOTTOM, ipadx=71, pady=3)

# 貼り付けボタン
paste_button = tk.Button(root, text="貼り付け", command=paste_from_clipboard,bg="lemon chiffon")
paste_button.pack(side=tk.BOTTOM, ipadx=60, pady=3)

# テキストエリア
text_area = tk.Text(root, height=20, width=30)
text_area.pack(side=tk.LEFT, padx=30, pady=10)

# 結果表示用テキストエリア
result_area = tk.Text(root, height=20, width=30, state="disabled")  # 初期は編集不可
result_area.pack(side=tk.RIGHT, padx=30, pady=10)




root.mainloop()
