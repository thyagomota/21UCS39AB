#!/bin/bash
sudo mkdir /home/ec2-user/hello
sudo wget https://scissors-sinners.s3-us-west-1.amazonaws.com/hello.py -P /home/ec2-user/hello
sudo chown -R ec2-user /home/ec2-user/hello
sudo wget https://scissors-sinners.s3-us-west-1.amazonaws.com/hello.service -P /etc/systemd/system
sudo systemctl enable hello; systemctl start hello