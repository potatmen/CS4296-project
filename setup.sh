#!/bin/bash

# Define client IP addresses
WORKERS=("ec2-98-81-137-231.compute-1.amazonaws.com"
"ec2-18-207-128-217.compute-1.amazonaws.com"
"ec2-54-81-142-216.compute-1.amazonaws.com"
"ec2-54-152-190-58.compute-1.amazonaws.com"
"ec2-3-88-175-79.compute-1.amazonaws.com"
"ec2-54-226-83-135.compute-1.amazonaws.com"
"ec2-34-234-86-36.compute-1.amazonaws.com"
"ec2-54-172-98-244.compute-1.amazonaws.com")

# Loop through each client and execute the iperf command
for CLIENT in "${WORKERS[@]}"; do
    #echo $CLIENT
    ssh -i "Cloud_course.pem" -o StrictHostKeyChecking=no ubuntu@$WORKERS 'bash -s' < ./worker_bootstrapper.sh &
done
wait