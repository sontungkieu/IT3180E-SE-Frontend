docker pull codemaivanngu/search-api
docker run -d -p 8000:8000 --name search-api codemaivanngu/search-api .
docker pull codemaivanngu/search-api-demo
docker run -d -p 8501:8501 --network host -e SERVER_URL="http://localhost:8000/" search-api-demo