FROM ubuntu:focal

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-venv curl\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY requirements.txt .
ENV PATH=/venv/bin:$PATH
RUN : \
    && python3 -m venv /venv \
    && pip --no-cache-dir install -r requirements.txt

COPY . .

CMD python3 nbaPlaylistGenerator/main.py