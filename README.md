# Register
```bash
$ http -f http://127.0.0.1:8000/api/v1/auth/register/ username=test password=test
```

# Get pair of tokens
```bash
$ http -f http://127.0.0.1:8000/api/v1/auth/token/ username=test password=test
```

# Refresh token
```bash
$ http -f http://127.0.0.1:8000/api/v1/auth/token/refresh/ username=test password=test
```

# Get list of clients
```bash
$ http GET http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer {your_token_here}'
```

# Delete client
```bash
$ http DELETE http://127.0.0.1:8000/api/v1/clients/manage/{int:pk}/ Authorization:'Bearer {your_token_here}'
```

# Add client
```bash
$ http -f http://127.0.0.1:8000/api/v1/clients/manage/ Authorization:'Bearer {your_token_here}' name=test1 surname=test1 birth_date=2003-03-03 gender=женский photo.file@/Users/rodionibragimov/Downloads/cheetos.jpeg left=100 top=100 right=400 bottom=400
```

# Update client
```bash
$ http PUT http://127.0.0.1:8000/api/v1/clients/manage/{int:pk}/ Authorization:'Bearer {your_token_here}' name=Name2_new 
```

# Get weather
```bash
$ http GET http://127.0.0.1:8000/api/v1/weather/{str:city}/{str:date(YYYY-MM-DD)} Authorization:'Bearer {your_token_here}'
```

# Run python daemon
```bash
$ cd redsoft/source
$ nohup python3 -u memory_usage.py
```

# Get memory usage
```bash
$ http GET http://127.0.0.1:8000/api/v1/monitor/memory/ Authorization:'Bearer {your_token_here}'
```
