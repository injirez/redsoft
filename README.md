# Register
http -f http://127.0.0.1:8000/api/v1/auth/register/ username=test password=test

# Get pair of tokens
http -f http://127.0.0.1:8000/api/v1/auth/token/ username=test password=test

# Refresh token
http -f http://127.0.0.1:8000/api/v1/auth/token/refresh/ username=test password=test

# Get list of clients
http GET http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer {your_token_here}'

# Delete client
http DELETE http://127.0.0.1:8000/api/v1/clients/manage/{int:pk}/ Authorization:'Bearer {your_token_here}'

# Add client
http -f http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer {your_token_here}' name=test1 surname=test1 birth_date=2003-03-03 gender=женский photo.file@/Users/rodionibragimov/Downloads/cheetos.jpeg left=100 top=100 right=400 bottom=400

# Update client
http PUT http://127.0.0.1:8000/api/v1/clients/manage/{int:pk}/ Authorization:'Bearer {your_token_here}' name=Name2_new 