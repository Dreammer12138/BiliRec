# BiliRec

## Bilibili自动录播站

***需要python3+ffmpeg的支持***

录播脚本来源于之前写的一个[项目](https://github.com/dreammer12138/DDMonitor)

### 安装

#### Linux

```shell
# 安装python依赖
$ sudo pip3 install -r requirements.txt

$ sudo python3 manage.py migrate
$ sudo python3 manage.py makemigrations
```

#### Windows

```powershell
> pip install -r requirements.txt
> python manage.py migrate
> python manage.py makemigrations
```

### 运行

#### Linux

```shell
$ sudo python3 start.py -r <room_id> -o <out_path> -p <port>
```

#### Windows

```powershell
> python start.py -r <room_id> -o <out_path> -p <port>
```

#### 参数

`-r/--room` 房间ID

`-o/--outpath` 保存路径

`-p/--port` Web端口