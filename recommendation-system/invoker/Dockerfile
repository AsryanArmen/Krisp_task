FROM python:3.9-slim

WORKDIR /app

COPY invoker.py /app

RUN pip install flask requests redis cachetools

EXPOSE 5001

CMD ["python", "invoker.py"]
