#!/usr/bin/env bash

echo "Setting up environment..."
python3 -m venv venv > /dev/null 2>&1
source venv/bin/activate > /dev/null 2>&1
pip3 install --user -r requirements.txt > /dev/null 2>&1

echo "Starting backend..."
cd backend/app
uvicorn main:app > /dev/null 2>&1 &
BPID=$!
echo $BPID > ../../trailhead_backend.pid
cd ../..



echo "Starting frontend..."
cd frontend
yarn --silent > /dev/null 2>&1
yarn --silent serve > /dev/null 2>&1 &
FPID=$!
echo $FPID > ../trailhead_frontend.pid
cd ..
