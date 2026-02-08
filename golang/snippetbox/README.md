podman run -d \
   --name mysql-snippetbox \
   -p 3306:3306 \
   mysql/mysql-server:latest

mysql -h 127.0.0.1 -uweb -Dsnippetbox -p

