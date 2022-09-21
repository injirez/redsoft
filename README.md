#Register
http -f http://127.0.0.1:8000/api/v1/auth/register/ username=test password=test

#Get pair of tokens
http -f http://127.0.0.1:8000/api/v1/auth/token/ username=test password=test

#Refresh token
http -f http://127.0.0.1:8000/api/v1/auth/token/refresh/ username=test password=test

#Get list of clients
http GET http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNzY0MzE3LCJpYXQiOjE2NjM3NjQwMTcsImp0aSI6ImNhYjQwZTU5ZmZmZDRiY2FiZjA2OGZmZGNhZjZhZGY1IiwidXNlcl9pZCI6MX0.--pQqcpDh9kD4yvHtN92oShGAZyueouhhhLysmU75L8'

#Delete client
http DELETE http://127.0.0.1:8000/api/v1/clients/manage/<int:pk>/ Authorization:'Bearer <your_token_here>'

#Add client
http -f http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer <your_token_here>' name=test1 surname=test1 birth_date=2003-03-03 gender=женский photo.file@/Users/rodionibragimov/Downloads/cheetos.jpeg

#Update client
http PUT http://127.0.0.1:8000/api/v1/clients/manage/<int:pk>/ Authorization:'Bearer <your_token_here>' name=Name2_new 