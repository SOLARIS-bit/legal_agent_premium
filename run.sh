#!/bin/bash

export FLASK_APP=app.main
export FLASK_ENV=development

# Kill old Flask if running
PORT=5001
PID=$(lsof -t -i:$PORT)
if [ ! -z "$PID" ]; then
  echo "🔥 Stopping previous Flask instance on port $PORT (PID: $PID)..."
  kill -9 $PID
fi

flask run --host=0.0.0.0 --port=$PORT
