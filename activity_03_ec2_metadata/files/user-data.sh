#!/bin/bash
yum update -y
yum install httpd -y
systemctl enable httpd
systemctl start httpd
cd /var/www/html
echo "<h2>Some Metadata Information</h2>" > index.html
echo "ami-id: " >> index.html
curl http://169.254.169.254/latest/meta-data/ami-id >> index.html 
echo "<br>" >> index.html 
echo "instance-id: " >> index.html
curl http://169.254.169.254/latest/meta-data/instance-id >> index.html 
echo "<br>" >> index.html
echo "instance-type: " >> index.html
curl http://169.254.169.254/latest/meta-data/instance-type >> index.html 
echo "<br>" >> index.html
echo "availability-zone: " >> index.html
curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> index.html 
echo "<br>" >> index.html
echo "security-groups: " >> index.html
curl http://169.254.169.254/latest/meta-data/security-groups >> index.html 
