import json
from os import path
from scannerbt import Scanner
import re

CONF_FILE = "./address-id.json"

if __name__=="__main__":
    #コンフィグファイルの有無
    if path.exists(CONF_FILE):
        with open(CONF_FILE) as f:
            data_list = json.load(f)
    else:
        data_list = []
        print("コンフィグファイルを新規作成します。")

    yn = input("周囲のBTデバイスを検索しますか？(y/_)：")
    if yn=="y":
        scanner = Scanner()
        print("周囲のデバイスを検索しています...")
        scanner.scan()
        print(scanner)
    
    mac_pattern_full = r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}"
    mac_pattern_num = r"[0-9a-fA-F]{12}"
    id_pattern_main = r"[0-9]{7}"
    id_pattern_major = r"s[0-9]{6}"

    mac = input("MACアドレスを入力してください。（XX:XX:XX:XX:XX:XX | 12桁の英数字）：")
    while True:
        if re.fullmatch(mac_pattern_num, mac):
            mac = ":".join([mac[i: i+2] for i in range(0, len(mac), 2)])
            print(mac+"に置換済み")
        if re.fullmatch(mac_pattern_full, mac):
            break
        mac = input("フォーマットが不適正です。再度入力してください。：")

    id = input("学生番号を入力してください。：")
    while True:
        if re.fullmatch(id_pattern_major, id):
            id = id.replace("s", "8")
            print(id+"に置換済み")
        if re.fullmatch(id_pattern_main, id):
            break
        id = input("フォーマットが不適正です。再度入力してください。：")

    name = input("学生の名前を入力してください。（※ 任意） => ")
    


    indiv_object = {"mac":mac, "id":id, "name":name}

    mac_list = [indiv["mac"] for indiv in data_list]
    id_list = [indiv["id"] for indiv in data_list]

    update = True
    exists = {"mac":mac in mac_list, "id":id in id_list}

    if True in exists.values():
        while True:
            if exists["mac"]:
                yn = input("登録済みのアドレスです。変更しますか？([y]/n) => ")
            elif exists["id"]:
                yn = input("登録済みの学籍番号です。変更しますか？([y]/n) => ")
                
            if yn in ["y", "n", ""]:
                update = False if yn=="n" else True
                break
        
    if update:
        if True in exists.values():
            data_list = list(filter(lambda indiv: indiv["mac"]!=mac and indiv["id"]!=id, data_list))
            
        data_list.append(indiv_object)

        with open(CONF_FILE, 'w', encoding="utf-8") as f:
            json.dump(data_list, f, indent=2, ensure_ascii=False)

        
        print("現在のコンフィグ：")
        for i, indiv in enumerate(data_list, 1):
            mac = indiv["mac"]
            id = indiv["id"]
            name = indiv["name"]
            print( f"{i}. {mac} : {id}"+ ( f"({name})" if name else '' ) )