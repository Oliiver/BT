docker build --no-cache --rm -t bt_int .
docker run -d --name bt_int -p 80:80 bt_int
