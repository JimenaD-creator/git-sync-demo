#!/bin/bash

REPO_DIR="/home/jimena_diaz/git-sync-demo"
BRANCH="main"
LOG_FILE="/home/jimena_diaz/git-sync.log"

echo "Sync started $(date)" >> $LOG_FILE

cd $REPO_DIR || exit

git pull origin $BRANCH >> $LOG_FILE 2>&1

echo "Sync finished $(date)" >> $LOG_FILE