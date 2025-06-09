# 1. Chọn base image Python nhẹ
FROM python:3.10-slim

# 2. Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# 3. Cài curl (và cleanup cache để giảm dung lượng)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*


# 3. Copy file requirements và cài đặt các thư viện
RUN pip install streamlit

# 4. Copy toàn bộ source code của bạn vào container
COPY . .

# 5. Mở cổng 8501 để truy cập Streamlit
EXPOSE 8501

# 6. Thiết lập biến môi trường mặc định cho URL backend
#    (khi chạy, nếu bạn không override, app sẽ gọi tới host.docker.internal:8000)
# ENV SERVER_URL=http://host.docker.internal:8000/

# 7. Lệnh khởi động Streamlit
CMD ["streamlit", "run", "app.py", \
     "--server.port", "8501", \
     "--server.address", "0.0.0.0"]
