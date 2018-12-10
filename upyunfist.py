import upyun

up = upyun.UpYun('dev-img-zone', 'wbc', 'wbc111111', timeout=30, endpoint=upyun.ED_AUTO)
notify_url = 'http://image-dev.egtcp.com'
fetch_tasks = [
    {
        'url': 'https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-1/p200x200/18813665_1836111640043040_1586858903275093616_n.jpg?_nc_cat=101&_nc_ht=scontent-nrt1-1.xx&oh=170df4580d7a9c9eee9b0fe3eed724f8&oe=5C715E43',
        'random': False,
        'overwrite': True,
        'save_as': '/avatar/a.jpg',
    }
]
print (up.put_tasks(fetch_tasks, notify_url, ''))