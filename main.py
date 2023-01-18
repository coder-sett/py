import requests
import csv
import time


def read_tex(path):
    data = []
    for line in open(path, "r"):  # 设置文件对象并读取每一行文件
        data.append(line.rstrip())  # rstrip()删除字符串末尾的空行
    return data


def format_time(time1):
    return time.strftime('%Y-%m-%d', time.strptime(time1, '%Y-%m-%dT%H:%M:%S%fZ'))


def get_results(repo_name):
    url = "https://api.github.com/repos/" + repo_name
    repo_response = requests.get(
        url, headers={'Connection': 'close', 'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token ***'})
    status_code = repo_response.status_code
    print("Status code:", status_code, url)
    if status_code == 200:
        repo_dict = repo_response.json()
        star = repo_dict['stargazers_count']
        forks = repo_dict['forks']
        created_at = repo_dict['created_at']
        pushed_at = repo_dict['pushed_at']
        topics = repo_dict['topics']
        description = repo_dict['description']
        return {'仓库url': 'https://github.com/' + repo_name, 'star数': star, 'fork数': forks, '第一次提交': format_time(created_at), '最近一次提交': format_time(pushed_at),  "topics": topics, "description": description}
    else:
        return {'仓库url': 'https://github.com/' + repo_name}


if __name__ == '__main__':

    # 创建或打开文件
    csvfile = open('仓库信息2.csv', mode='w', newline='', encoding='utf-8')
    # 标题列表
    fieldnames = ['仓库url', 'star数', 'fork数',
                  '第一次提交', '最近一次提交', "topics", "description"]
    # 创建 DictWriter 对象
    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入表头
    write.writeheader()
    data = read_tex("selectedActiveList.txt")
    # data = ['k9mail/k-9']
    for i in data:
        write.writerow(get_results(i))   # 写入一行数据
        time.sleep(0.2)
