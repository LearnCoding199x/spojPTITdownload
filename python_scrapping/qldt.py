import requests
from pdfrw import PdfWriter
from bs4 import BeautifulSoup
res = requests.session()
r = res.get('http://qldt.ptit.edu.vn')
bs = BeautifulSoup(r.content, "html.parser")
#d1 = bs.find(id="ctl00_ContentPlaceHolder1_ctl00_lblCapcha").text
viewstate = bs.find(id = "__VIEWSTATE")['value']
# print viewstate
c_data = {
    "__EVENTTARGET" : "",
    "__EVENTARGUMENT" : "",
    "__VIEWSTATE" : viewstate,
    "__VIEWSTATEGENERATOR" : "CA0B0334",
    # "ctl00$ContentPlaceHolder1$ctl00$txtCaptcha" : d1,
    "ctl00$ContentPlaceHolder1$ctl00$ucDangNhap$txtTaiKhoa" : "B15DCPT063",
    "ctl00$ContentPlaceHolder1$ctl00$ucDangNhap$txtMatKhau" : "ha100497",
    "ctl00$ContentPlaceHolder1$ctl00$ucDangNhap$btnDangNhap" : "%u0110%u0103ng%20Nh%u1EADp"
}
r = res.post('http://qldt.ptit.edu.vn/default.aspx?page=gioithieu', data = c_data)
r = res.post('http://qldt.ptit.edu.vn/Default.aspx?page=thoikhoabieu')
with open('login_success.html','wb') as f:
    f.write(r.content)
print('Success!!!!!!')