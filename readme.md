# KT IPTV Rating Info Archiving  
Archiving real-time KT IPTV rating into DB  
for SBS TV listing  
  
This code will collect and push the rating data every minute.

## How to Run
It needs "config.py" in "Utils/" dicrectory. config.py should includes followings:
``` python
HOST = [DB HOST]
PORT = [DB PORT]
USER = [DB USERNAME]
PASSWORD  = [DB PASSWORD]
DATABASE = [DB]
```
and run by`$ python main.py`  

I'm currently using MySQL Server located in 19F  

### requirement
* pymysql

### Rating data includes...
* 현재시각 (YYYY-MM-DD HH:MM)
* 채널번호
* 채널이름
* 프로그램이름
* 편성 시간 (HH:MM ~ HH:MM)
* 시작 시각 (HH:MM)
* 종료 시각 (HH:MM)
* 시청률
* 시청률 순위
* 편성 지속시간(Duration) (HH:MM)