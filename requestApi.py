import requests
import bs4
import re

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str ='UM_distinctid=161bc918d89733-0eabab0fd241c7-3b60490d-1fa400-161bc918d8b120; cna=1SYVEyn+1DoCAXrj9CaAfIm8; ali_ab=122.227.244.38.1519287111070.3; hng=CN%7Czh-CN%7CCNY%7C156; lid=%E7%91%9C%E4%BC%BD%E7%94%9F%E6%B4%BB%E4%BD%93%E9%AA%8C%E9%A6%86; ali_apache_track=c_mid=b2b-576881338eyne0|c_lid=%E7%91%9C%E4%BC%BD%E7%94%9F%E6%B4%BB%E4%BD%93%E9%AA%8C%E9%A6%86|c_ms=1; last_mid=b2b-576881338eyne0; __last_loginid__=%E7%91%9C%E4%BC%BD%E7%94%9F%E6%B4%BB%E4%BD%93%E9%AA%8C%E9%A6%86; _cn_slid_=nx%2BARrrZbm; enc=LGC83wZw100PMbFKlbq1%2BZoBAUvh%2BTZ9DTtx1oCEH0yvEy2%2BwYOwX8x6vskMOkzhT4keuXnlGgWe%2FNLiu978dQ%3D%3D; h_keys="%u963f%u91cc%u5df4%u5df4#%u745c%u4f3d%u7816#%u745c%u4f3d%u67f1#%u745c%u4f3d%u57abNBR#%u745c%u4f3d%u57ab#PVC%u745c%u4f3d%u57ab#%u4f38%u5c55%u5e26#%u745c%u4f3d%u7403#%u5f39%u529b%u5e26#%u513f%u7ae5%u821e%u8e48%u57ab"; ad_prefer="2018/08/03 19:26:39"; __cn_logon_id__=%E7%91%9C%E4%BC%BD%E7%94%9F%E6%B4%BB%E4%BD%93%E9%AA%8C%E9%A6%86; __cn_logon__=true; cookie2=2eaa63992524b84972e96b08947d40e1; t=e2202281a869cf6600c91e2061d39eac; _tb_token_=ee5e83e18e333; ali_apache_tracktmp=c_w_signed=Y; tbsnid=vAgmpMs2IONjYX%2B7dopbxAjU73%2Bps0NdsbGeB1iat7Q6sOlEpJKl9g%3D%3D; userID=PA9f5AWyVy%2Bz1BF%2BtTxEOQJLwyksgIQ7Iir7S2SHc3U6sOlEpJKl9g%3D%3D; userIDNum=7Qs2HusB8%2F4yp8JBi5lr6w%3D%3D; JSESSIONID=D0xYcna-3m9aWMw6FehN6rSvi8-eUfVk0R-wRNj; cookie1=AVTi8%2BdFwMOpOgQZ5doYl33UfyHXWuk2ErULwXirTCA%3D; cookie17=VvlxeQ1Yj78l; sg=%E9%A6%8686; csg=abf77dd3; LoginUmid=d%2FJPvO%2BJ66JbUEaxd5Cae5ZzGt0ThjPRVfntuNmv37zElUbKolxKOQ%3D%3D; unb=576881338; cn_tmp="Z28mC+GqtZ0r+WAaarlyok9Lx8s/NswQgw4KxGFOFGpJjckoUk7vALu1/0pSS3inKtlS4eIifw5d/zmY227bnXxLvQYnN3KOuDsud1x/z6IIJj8xuX1UcYmEkEB7Kcyi8nqmDv1HWx2jqrFzCzQlwhG+464+sMH0wKtHt1A8qE/JHD9M9+B3RC0GJtazUNh8Zk6JSFdy1sqxbMe+Xuyk2HPGJdklT2Vfv2wy44lvGaFMt6UhLPBnpVYpT7iNW6EjSyOwxK+Bvxyvu7TaLhO8JA=="; login=kFeyVBJLQQI%3D; _nk_=MExcnGCSTiozCpe5%2Fb6vrQ%3D%3D; _csrf_token=1534311446364; __rn_alert__=false; JSESSIONID=B9619CDB7522D44C312DD74F5769EF35; _tmp_ck_0=zbfvknZrLptzj5DcJ5pSIyq6HZsKHdCFgkPQ74K2Z8KzZvdMIMNj1T%2BX3%2FxmLLiIux%2FgxuvaG%2BO4cSX9%2BnZxjA%2FmbnKuOaRuXhMKBUegTg8bHMPjTq7lFFSSqOYArQrXjp80zkDwEkYx2k4jdMq1ncibY9X72UQSzXp666gwCafcVHq9bMvIZa8TF3oTm7xv3P5q1Z%2FCe1oN0kDu3fjLNQMX8fKwVQ28VQXVKX8XXXcfFE4S01l6aWUJZLH3RuYI2FDlZDcbz%2BihQBM49%2Bu5sUOGKY5eMSExovTR9rsb%2BeRwcilyUGhuDB9m9cmoegKlps87M7KZFZLOlQhtK7sctwsVkmKIVPRZQRjSX%2FNlK3X7N7S6nWsjEUaKzrTfEz7w3J3r8IGKyfVLPI7WtOayLnaU%2FQbaXqAmAOMnWj8HzeXgGOvZCRgcjbOPH9eUTJTBnCBAISpHbWnaQnOp%2BF9psKye%2BCt84HXIA7JuYOJpjU9yUjproR27vynmTij6Pz0DGMR%2F2%2Bps7JtBbsFWhd%2FDwSw8AsNlzvUGD5QuLLNI5sc%3D; alicnweb=touch_tb_at%3D1534318583025%7Clastlogonid%3D%25E7%2591%259C%25E4%25BC%25BD%25E7%2594%259F%25E6%25B4%25BB%25E4%25BD%2593%25E9%25AA%258C%25E9%25A6%2586%7ChomeIdttS%3D02953759199564258136606143011504411703%7ChomeIdttSAction%3Dtrue; _is_show_loginId_change_block_=b2b-576881338eyne0_false; _show_force_unbind_div_=b2b-576881338eyne0_false; _show_sys_unbind_div_=b2b-576881338eyne0_false; _show_user_unbind_div_=b2b-576881338eyne0_false; ctk=17a41d7cfe487e22fb62cb4f03fee67e; isg=BP7-A6gMKdpdqXwDoz87VLJ-TxSAl9a2G01sgqgHasE8S54lEM8SySQNx1ci87rR'

url = 'https://trade.1688.com/order/new_step_order_detail.htm?orderId=203110988462883813'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

resp = requests.get(url, headers = headers, cookies = cookies)
status_code = resp.status_code
content = bs4.BeautifulSoup(resp.content.decode("gbk"), "lxml")
no = content.find_all(class_="logistics-flow-exposure")
info  = content.find_all(class_='panel-content')
mobile = content.find_all(text=re.compile('手机：'))
print(status_code)

print(info)
print(no)
print(mobile)