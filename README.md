# tcpcon

tcpcon is a small uility (developed in Python) to test connections to a given host/port .

Expected to work on Windows, Linux and Mac .

## Motivation

Needed a quick way to test connections from systems where netcat is not available


## Requirements
- Python3

## How to install
```sh
pip instal tcpcon
```

## How to use
Interactive mode:
```sh
tcpcon www.sapo.pt 80
```

Batch mode using stdin:
```sh
 echo -e "HEAD / HTTP/1.0\r\nHost: www.google.com\r\n" \
    | tcpcon www.google.com 80 -v
```
