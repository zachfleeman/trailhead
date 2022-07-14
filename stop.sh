#!/usr/bin/env bash

BPID=$(cat trailhead_backend.pid)
sudo kill -9 $BPID

FPID=$(cat trailhead_frontend.pid)
sudo kill -9 $FPID