FROM python:3.7-alpine
MAINTAINER KnightWhoSayNi <threeheadedknight@protonmail.com>

RUN apk add --update --no-cache \
    python3-dev

RUN pip install --upgrade pip

WORKDIR /app

COPY /ifconfigparser /app

RUN export PYTHONPATH=$PYTHONPATH:${pwd}:$(pwd)/:$(pwd)/tests && \
    python -m unittest -v test_ifconfig_parser.TestIfconfigParser

CMD ["/bin/bash"]
