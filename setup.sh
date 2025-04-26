#!/bin/bash

# Define worker DNS addresses
WORKERS=("ec2-54-82-36-59.compute-1.amazonaws.com"
"ec2-98-81-217-202.compute-1.amazonaws.com"
"ec2-54-82-110-7.compute-1.amazonaws.com"
"ec2-54-221-190-189.compute-1.amazonaws.com"
"ec2-107-23-142-66.compute-1.amazonaws.com"
"ec2-98-81-84-106.compute-1.amazonaws.com"
"ec2-50-17-26-8.compute-1.amazonaws.com"
"ec2-54-159-54-183.compute-1.amazonaws.com")

# Loop through each worker and bootstrap
for WORKER in "${WORKERS[@]}"; do
    ssh -i "Cloud_course.pem" -o StrictHostKeyChecking=no ubuntu@$WORKER 'bash -s' < ./worker_bootstrapper.sh &
done
wait