#!/bin/bash

if docker ps ; then
    docker-compose down 
    docker rm -fv test-helper_ai_small
fi