# Music API
Simple music API.

Written with `FastAPI`

## Installation
You need python3.10 version and git
1) Clone repository
```bash
$ git clone https://github.com/omadli/music-api
``` 
2) Open folder and create `virtual env`
Example in ubuntu:
```bash
$ cd music-api
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

3) Install requirements
```bash
$ pip install wheel
$ pip install -r requirements.txt
```

4) Start with uvicorn
```bash
$ uvicorn main:app
```

## Deploy to server with nginx and gunicorn

### Gunicorn configurations

Before you start, you should open the `gunicorn_conf.py` and `musicapi.service` files and edit the paths.

1) Copy service file
```bash
$ cp musicapi.service /etc/systemd/system/musicapi.service
```
2) Start & enable the service.
```bash
$ sudo systemctl start musicapi
$ sudo systemctl enable musicapi
```
To verify if everything works run the following command.
```bash
$ sudo systemctl status musicapi
```
Also, you can check the response using the following command.
```bash
$ curl --unix-socket unix:/home/ubuntu/music-api/gunicorn.sock localhost
```
The expected output for the provided demo code is:
```json
{"message": "Hello World"}
```

### Nginx configurations

1) Install Nginx
```bash
$ sudo apt update
$ sudo apt install nginx
```

2) Add vhost configuration
Add vhost file to sites-available directory.
```bash
$ sudo nano /etc/nginx/sites-available/<YOUR_DOMAIN>
```
Paste the following content (replace your_domain with your actual domain) and save the file using `CTRL` + `X` then `ENTER`.
```
server {
    listen 80;
    server_name <YOUR_DOMAIN> www.<YOUR_DOMAIN>;

    location / {
        proxy_pass http://unix:/home/ubuntu/music-api/gunicorn.sock;
    }
}
```

3) Activate vhost configuration
Add a soft link of the vhost file in the sites-enabled directory.
```bash
$ sudo ln -s /etc/nginx/sites-available/<YOUR_DOMAIN> /etc/nginx/sites-enabled/
```
Test and reload the configuration

Test the configuration.
```bash
$ sudo nginx -t
```
Expected output:
```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

4) Reload Nginx.
```
$ sudo systemctl reload nginx
```



<br><hr>The end.<br>
&copy; Omadli😎 2022.