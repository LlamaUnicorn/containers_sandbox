FROM python:3-alpine
WORKDIR /apps/subredditfetcher/
COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "newsbot.py"]


