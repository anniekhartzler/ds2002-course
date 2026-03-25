#!/bin/bash

aws ec2 describe-instances | jq '.Reservations[].Instances[] | {
  ImageId: .ImageId,
  InstanceId: .InstanceId,
  InstanceType: .InstanceType,
  InstanceName: ([.Tags[]? | select(.Key=="Name") | .Value][0]),
  PublicIpAddress: .PublicIpAddress,
  State: .State
}'
