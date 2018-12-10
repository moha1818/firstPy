import sys
import json
import re


if __name__ == '__main__':
    data = '[{"avatar":"https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-1/p200x200/45596939_767054013642598_4234533511257653248_n.png?_nc_cat=1&_nc_ht=scontent-nrt1-1.xx&oh=dce6b53cd85525415ff3fdafc83ba897&oe=5C6E5306","imageList":[],"lastTime":"1542318674","nickName":"Finteza","text":"Website & mobile apps traffic analysis plus banners rotation service. Without delay & sampling."},{"avatar":"https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-1/p200x200/45596939_767054013642598_4234533511257653248_n.png?_nc_cat=1&_nc_ht=scontent-nrt1-1.xx&oh=dce6b53cd85525415ff3fdafc83ba897&oe=5C6E5306","imageList":["https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/46303977_2170110006643200_5534956472120639488_n.jpg?_nc_cat=109&_nc_ht=scontent-nrt1-1.xx&oh=6758d7a5e4aa8f5e987f0428b3aa64de&oe=5C646E0D","https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/46403390_2170110003309867_8893513252827299840_n.jpg?_nc_cat=107&_nc_ht=scontent-nrt1-1.xx&oh=c38d6d78f8a5cc10c19c5214230bd2dc&oe=5C6C4336"],"lastTime":"1542288538","nickName":"Muhammad Mustaqeem","text":"CR trimmings and Rolling plates available from USA, Interested inbox please. \\r WhatsApp: 0092 336 2416577"}]'

    json_str = json.dumps(eval(data))
    print(json_str)
    data2 = json.loads(json_str)
    print(data2)
    print("data2['name']: ", data2[0]['avatar'])
