FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install aiohttp
CMD ["python", "main.py"]
