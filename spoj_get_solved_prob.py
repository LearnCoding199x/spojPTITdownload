import requests
import sys
import urllib
import os
from bs4 import BeautifulSoup

def getInfoAndDownload(username,password):
    with requests.Session() as s:
        url = 'http://www.spoj.com/login/'
        values = {'login_user': username,
                'password': password,
                'next_raw': '/',
                'autologin': '1'} 
        r = s.post(url, data=values)
        data = r.text
        if data.find('sign in')>-1:
            print('Wrong username or password,Exitting....')
            return
        solve = 'solved_prob_{}'.format(username)
        os.makedirs(solve)
        url = 'http://www.spoj.com/PTIT/users/{}/'.format(username)
        r = s.post(url)
        data = r.text
        soup = BeautifulSoup(data)
        td = soup.find_all("table",{"class": "table table-condensed"})
        print('Danh sach cac bai ban da lam : ')
        list_prob_solved = []
        list_prob_unsolved = []
        check = 0
        with open('solved.txt',mode='w') as f:
            for table_data in td:
                if check == 0 :
                    f.write(table_data.text)
                    check = 1
                else:
                    with open('unsolved.txt',mode='w') as g:
                        g.write(table_data.text)
                    g.close()
        f.close()
        with open('solved.txt','r') as f:
            list_prob_solved =f.read().splitlines() 
            list_prob_solved = list(filter(None, list_prob_solved))
        f.close()
        with open('unsolved.txt','r') as f:
            list_prob_unsolved =f.read().splitlines() 
            list_prob_unsolved = list(filter(None, list_prob_unsolved))
        f.close()
        print(list_prob_solved, '\ntong so bai la : ', len(list_prob_solved))
        print('\n\nDanh sach cac bai chua lam xong : ', list_prob_unsolved ,'\ntong so bai la : ',len(list_prob_unsolved))
        print('Please wait,we are downloading your solved problems code into solved_prob folder......')
        for solve_prob in list_prob_solved:
            url = 'http://www.spoj.com/PTIT/status/{},{}/'.format(solve_prob,username)
            r = requests.post(url)
            data = r.text
            soup = BeautifulSoup(data)
            status = soup.find_all("td",{"class": "statusres"})
            for stt in status:
                if stt.text.find('accepted')> -1:
                    id = stt.get('id')
                    id = id[id.find('_')+1:]
                    break
            url = 'http://www.spoj.com/PTIT/files/src/save/{}/'.format(id)
            file_name = '{}/{}-src.cpp'.format(solve,solve_prob)
            response = s.get(url)
            if response.status_code == 200:
                with open(file_name, 'wb') as f:
                    f.write(response.content)
            print('Save file '+solve_prob+'-src.cpp')
