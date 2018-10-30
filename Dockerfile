FROM python:3.6 AS lint

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install pylint



FROM python:3.6-alpine
RUN mkdir -p /opt/lc

WORKDIR /opt/lc

COPY requirements.txt /opt/lc
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/lc

EXPOSE 12589

ENTRYPOINT ["/opt/lc/start.sh"]