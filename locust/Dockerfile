FROM locustio/locust

WORKDIR /mnt/locust

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .  
CMD ["-f", "/mnt/locust/locustfile.py", "--host=http://app:8000"]


