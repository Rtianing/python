# --*-- coding:utf-8 --*--

import json
import time


class Address(object):
    def __init__(self):
        with open("通讯录.txt", 'r', encoding='utf-8') as f:
            self.data = json.loads(f.read())  # 所有联系人列表
            # print(self.data, type(self.data))

    def main_menu(self):
        # 主菜单（主页面）
        while True:
            print('通讯录'.center(20, '='))
            menu = {'1': '快速查找',
                    '2': '添加联系人',
                    '3': '显示所有联系人'}
            for k, v in menu.items():
                print(k + ' ' + v)
            command = input('请选择你的操作>>')
            if command == '1':
                Address.__search(self)
            elif command == '2':
                Address.__add_address(self)
            elif command == '3':
                Address.__show(self)
            elif command == 'q':
                print('退出...')
                break

    def __search(self):
        print('快速查找'.center(20, '='))
        # 可以根据联系人名字查找，也可以根据电话号码查找
        find_info = input('请输入查找信息>>')
        count = 0
        for i in range(len(self.data)):
            if count > len(self.data):
                print('未找到该联系人')
                break
            if find_info in self.data[i]['name']:
                Address.__person_info(self, self.data[i])  # 若有该联系人，则进入联系人个人信息页
            elif find_info in self.data[i]['phone_number']:
                Address.__person_info(self, self.data[i])  # 若有该号码，则进入联系人个人信息页
            else:
                pass
            count += 1

    def __person_info(self, info):
        # 个人信息页
        # find_info 是该联系人的信息字典
        print('已为你找到:{}'.format(info['name']))
        menu = {'1': '查看个人信息', '2': '修改信息', '3': '删除联系人', '4': '呼叫联系人', '5': '呼叫记录'}
        while True:
            print('个人信息页'.center(20, '='))
            for k, v in menu.items():
                print(k + ' ' + v)
            command = input('请选择操作>>')
            if command == '1':
                print('姓名：{}\n电话号码：{}\n通话记录：{}'.format(info['name'],
                                                       info['phone_number'], info['call_records']))
            elif command == '2':
                Address.__modify_info(self, info)
            elif command == '3':
                Address.__del_contact(self, info)
                break  # 删除联系人之后，该联系人的个人信息页就没了，所以就得跳回去
            elif command == '4':
                Address.call(self, info)
            elif command == '5':
                Address.call_logs(self, info)
            elif command == 'q':
                print('返回...')
                break

    def call_logs(self, info):
        # 通话记录
        print('呼叫记录'.center(20, '='))
        with open('通讯录.txt', 'r', encoding='utf-8') as f:
            data_list = json.loads(f.read())
        for data in data_list:
            if data['name'] == info['name']:
                print(data['call_records'])
                break
            else:
                continue

    def call(self, info):
        # 呼叫联系人
        print('呼叫{}'.format(info['name']).center(20, '='))
        print('通话中...')
        self.data.remove(info)
        start_time = time.time()
        now_time = time.ctime()
        input('按e挂断电话>>')
        end_time = time.time()
        pass_time = end_time - start_time
        info['call_records'].append(now_time+"通话时长："+str(pass_time))  # 将本次通话加入通话记录的列表中
        self.data.append(info)
        Address.updata_address(self)
        print('通话结束')

    def __del_contact(self, info):
        # 删除联系人
        try:
            self.data.remove(info)
        except Exception as e:
            print(e)
        Address.updata_address(self)
        print('成功删除联系人: {}'.format(info['name']))

    def __modify_info(self, info):
        # 修改联系人信息
        # info是该联系人信息字典
        if info in self.data:
            self.data.remove(info)  # 将所有联系人的列表中的该联系人删除，等修改好之后再后在重新加进去，然后更新通讯录
        menu = {'1': '修改备注', '2': '修改号码', '3': '删除通话记录'}
        while True:
            print('修改信息'.center(20, '='))
            for k, v in menu.items():
                print(k + ' ' + v)
            command = input('请选择操作>>')
            if command == 'q':
                print('返回...')
                break
            if command == '1':
                info['name'] = input('请输入备注>>')
            elif command == '2':
                info['phone_number'] = input('请输入号码>>')
            elif command == '3':
                info['call_records'] = []
            else:
                continue
        self.data.append(info)  # 将修改过的该联系人信息加入所有联系人信息列表，以待更新通讯录
        # print(self.data)
        Address.updata_address(self)  # 更新通讯录
        print('信息修改成功')

    def updata_address(self):
        # 刷新通讯录
        with open('通讯录.txt', 'w', encoding='utf-8') as f:
            try:
                json.dump(self.data, f, ensure_ascii=False)
            except Exception as e:
                print('操作失败：%s' % e)

    def __add_address(self):
        # 添加联系人
        print(self.data)
        print('添加联系人'.center(20, '='))
        new_contact = {}
        new_contact['name'] = input('请输入联系人备注>>')
        new_contact['phone_number'] = input('请输入号码>>')
        new_contact['call_records'] = []
        self.data.append(new_contact)
        Address.updata_address(self)  # 更新通讯录
        print('成功添加联系人')

    def __show(self):
        # 显示所有联系人
        print('所有联系人'.center(20, '='))
        contacts = {}  # 所有联系人的名字
        for i in range(len(self.data)):
            contacts[str(i)] = self.data[i]['name']
            print('{} {}'.format(str(i), self.data[i]['name']))
        command = input('请选择查看联系人>>')
        name = contacts[command]
        for data in self.data:
            if data['name'] == name:
                Address.__person_info(self, data)
            else:
                continue


if __name__ == '__main__':
    a1 = Address()
    a1.main_menu()