
MYSQL_CONTAINER_ID=$(docker run --name mysql2 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password1 -e MYSQL_HOST=mysql1 -e MYSQL_USER=user1 --network network2 mysql)


MYSQL_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $MYSQL_CONTAINER_ID)


docker build -t api .


docker run --name api -d -p 5000:5000 -e MYSQL_ROOT_PASSWORD=password1 -e MYSQL_HOST=$MYSQL_HOST -e MYSQL_USER=root --network network2 api


