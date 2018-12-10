import time

def test1():
    str="function1"
    print(str);
    local = time.localtime(1542312695)
    pub_time = time.strftime('%Y-%m-%d %H:%M:%S',local)
    print(pub_time)
    float_time = time.time()
    now = time.strftime('%y%m%d%H%M%S')
    for n in range(1,10000):
        now = time.strftime('%y%m%d%H%M%S')
        print(time.clock())
        print(now)
        float_time = time.time()
        print(float_time)
test1()