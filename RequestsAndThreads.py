# -*-coding:utf-8-*-
# !/usr/bin/env Python
import codecs
import os

import datetime
import requests, multiprocessing, time, json
from threading import Thread


def get_pro_items(province):
    # print(province)
    for j in (1, 2):
        item_str = province + str(j)
        # print(item_str)
        for i in range(20):
            num = i + 1
            str_num = str(num)
            proj_name = pro_map.get(num)
            if (j == 1):
                str1 = "http://111.8.17.230:9001/vote3/tool/search.php?opt=4&telNo=" + item_str + "&project=" + str(
                    num) + "&jtype=2"
                r = requests.get(str1)
                obj = json.loads(r.text)
                if (type(obj) is list):
                    str_result = obj[0]['productive_value'] + ',' + obj[0]['novelty'] + ',' + obj[0][
                        'usability'] + ',' + obj[0]['efficiency'] + ',' + obj[0]['generalizability']
                    # print(obj[0]['0'])
                else:
                    str_result = str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0)
                ideal_file.write(item_str + "," + str_num + "," + proj_name + "," + str_result + '\n')
                print(item_str + "," + str_num + "," + proj_name + "," + str_result)
            if (j == 2):
                str1 = "http://111.8.17.230:9001/vote3/tool/search.php?opt=4&telNo=" + item_str + "&project=" + str(
                    num) + "&jtype=1"
                r = requests.get(str1)
                obj = json.loads(r.text)
                if (type(obj) is list):
                    str_result = obj[0]['devops_degree'] + ',' + obj[0]['technical_difficulty'] + ',' + obj[0][
                        'technical_innovation'] + ',' + obj[0]['framework'] + ',' + obj[0]['algorithm_design'] + ',' + \
                                 obj[0]['product_design'] + ',' + obj[0]['deployment'] + ',' + obj[0][
                                     'benefit'] + ',' + obj[0]['feasibility']
                else:
                    str_result = str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(
                        0) + ',' + str(0) + ',' + str(0) + ',' + str(0)
                    # print(obj[0]['0'])
                ideal_file.write(item_str + "," + str_num + "," + proj_name + "," + str_result + '\n')
                print(item_str + "," + str_num + "," + proj_name + "," + str_result)


# 多进程
# for item in pro_list:
#     t = multiprocessing.Process(target=get_pro_items, args=(item,), name=item)
#     t.start()

# 多线程
if __name__ == '__main__':
    pro_list = ["anhui", "beijing", "chongqing", "fujian", "gansu", "guangdong", "guizhou", "henan", "hubei", "hunan",
                "jilin", "jiangsu", "jiangxi", "liaoning", "shandong", "shanghai", "sichuan", "yunnan", "tianjing",
                "zhejiang"]
    pro_map = {1: '浙江', 2: '湖北', 3: '江苏', 4: '广东', 5: '河南', 6: '广东', 7: '湖南', 8: '广东', 9: '天津', 10: '山东', 11: '湖南',
               12: '安徽', 13: '广东', 14: '安徽', 15: '福建', 16: '广东', 17: '安徽', 18: '江苏', 19: '广东', 20: '吉林'}

    ideal_file = open("Result.csv", "a", encoding='utf-8')
    # ideal_file.write(codecs.BOM_UTF8)
    ideal_file.write("省" + ",项目名称" + "，项目对应省" + "\n")
    threads = []
    starttime = datetime.datetime.now()
    for item in pro_list:
        t = Thread(target=get_pro_items, args=(item,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    ideal_file.close()
    endtime = datetime.datetime.now()
    print("总用时：" + str((starttime - endtime).seconds / 1000))

# 单项测试
# get_pro_items("zhejiang")
