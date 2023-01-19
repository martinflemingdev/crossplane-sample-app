#!/bin/bash

# run from root of repo with Elastic IP
ssh -i "upbound-test.pem" ec2-user@"$1"