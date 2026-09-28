#!/usr/bin/env bash
# ==========================================================
# ScareX - Raspberry Pi 5 Edge Node Startup Script
# Starts Camera Stream Server (:8000) and Command Server (:9000)
# ==========================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================================="
echo "          Starting ScareX Raspberry Pi 5 Node             "
echo "=========================================================="

# Check if port 8000 or 9000 already in use
fuser -k 8000/tcp > /dev/null 2>&1
fuser -k 9000/tcp > /dev/null 2>&1

echo "[Pi] Starting Camera Server on port 8000..."
python3 -m raspberry_pi.camera_server &
PID_CAM=$!

sleep 2

echo "[Pi] Starting Command & Hardware Server on port 9000..."
python3 -m raspberry_pi.command_server &
PID_CMD=$!

echo ""
echo "ScareX Pi Node is ONLINE!"
echo "Camera Stream: http://$(hostname -I | cut -d' ' -f1):8000/video"
echo "Command API:   http://$(hostname -I | cut -d' ' -f1):9000/command"
echo ""
echo "Press Ctrl+C to stop both servers."

trap "echo 'Shutting down Pi Node...'; kill $PID_CAM $PID_CMD; exit 0" INT TERM
wait
