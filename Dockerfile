FROM python:3.7.3-stretch


WORKDIR /app

COPY . src/ /app/

RUN pip install --upgrade pip &&\
    pip install Flask


EXPOSE 80

CMD ["python", "app.py"]

