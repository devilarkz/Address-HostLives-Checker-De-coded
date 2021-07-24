import socket;
import json;
from urllib.request import urlopen;

print ("     >>>>>>TOOL RIÊNG CỦA AN_BQ<<<<<<")
print ("          >>Youtube: An_BQ<<")
print ("    ------>Discord: An BQ#5874<------")
print ("------>Website: https://shopanbq.com/<------")
print ("Gửi Lời Chào Đến: LoudestMaside , D9CAN , JohnEjan , Chino , KAYOUTUBEROBLOX") #Phần chào hỏi thôi cu
print (" ?????????????????CÓ CỐ SKID CODE CỦA BỐ CŨNG ĐÉO ĐƯỢC ĐÂU :3????????????????")
print ();
def google_ok():
    try:
        urlopen('https://www.google.com', timeout=10);
        return True
    except: 
        return False
    return True
def yahoo_ok():
    try:
        urlopen('https://www.yahoo.com', timeout=10);
        return True
    except: 
        return False
    return True
def site_ok():
    try:
        urlopen('https://ipinfo.io', timeout=10);
        return True
    except: 
        return False
    return True
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address);
    except socket.error:
        return False
    return True
def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address);
    except socket.error:
        return False
    return True
#Nhập địa chỉ hiểu chưa?
host = input("Nhập Địa Chỉ IP Nạn Nhân: ");

if google_ok() or yahoo_ok():
    if site_ok():
        if is_valid_ipv4_address(host) or is_valid_ipv6_address(host):
     #Phần dưới này là API của website để track network
            whois = "https://ipinfo.io/" + host + "/json";
            data   = urlopen(whois).read();
            js = json.loads(data)
            if "bogon" in js :
                print ();
                print ("Lỗi 009: Your IP Address is not a Public IP Address !");
        #Lỗi mã chỉ để chưng cho đẹp thôi cu
            else:
                print ();
             
                print (">>>>>>>>>>>>>Địa chỉ IP địa lý: " + js["ip"]);
              
                print (">>>>>>>>>>>>>Quốc Gia Của Nạn Nhân: " + js["country"]);
              
                print (">>>>>>>>>>>>>Vị trí địa lý của nạn nhân: " + js["loc"]);
              
                print (">>>>>>>>>>>>>Thông Tin Mạng Lưới: " + js["org"]);
               
                print (">>>>>>>>>>>>>Thời Gian Tại Quốc Gia Của Nạn Nhân(Ví dụ: UTC+): " + js["timezone"]); 
               

                print (" ///////////ĐÃ DÁN CODE ẨN CHỐNG SKID-RolgdJAT api////////////")
        else:
            print ();
            print ("Lỗi: Địa chỉ của ip được nhập sai!");
    else:
        print ();
        print ("Lỗi: Thông tin không tồn tại!");
else:
    print ();
    print ("Lỗi 202: Kiểm tra kết nối mạng!");
