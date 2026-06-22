# Lightweight Python image use kar rahe hain taki server fast load ho aur RAM kam use kare
FROM python:3.9-slim

# Server ke andar folder setup
WORKDIR /app

# Files ko server me copy karna
COPY requirements.txt .
COPY server.py .

# Packages ko bina cache ke install karna taki storage waste na ho
RUN pip install --no-cache-dir -r requirements.txt

# Render ke port ko open karna
EXPOSE $PORT

# Server start karne ka command
CMD ["python", "server.py"]
