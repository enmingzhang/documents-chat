#/bin/bash

uvicorn ${MAIN_APP}:app --host  0.0.0.0 --workers ${WORKER_NUM}