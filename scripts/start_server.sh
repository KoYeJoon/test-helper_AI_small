#!/bin/bash

if [ -d docker-compose.yml ]; then
    docker-compose down
fi
