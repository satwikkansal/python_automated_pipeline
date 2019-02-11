#!/bin/bash
URL=127.0.0.1
PORT=5000
if nc -vz $URL $PORT; then
    echo "Everything is fine!"
else
    echo "Something went wrong :("
    exit 1
fi
