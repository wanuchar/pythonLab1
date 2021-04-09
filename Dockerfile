FROM python:3.9

ENV TARGET /Users/user/sem4python/lab1/

WORKDIR "${TARGET}"

COPY main.py "${TARGET}"
COPY requirements.txt "${TARGET}"

RUN set -ex \ 
	pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

CMD ["python3", "main.py"]
