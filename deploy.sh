#!/bin/bash

sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

while getopts "c" options; do
    case ${options} in
     c) create=true;;
    esac
done

if [ ${create} ]; then
    python3 create.py
fi

"Cat - > /tmp/app.service << EOF
{Unit}
description=run flask app as systemd

[service]
user=jenkins
environment=db_uri=$db_uri
environment=secretkey=$secretkey
environment=GUNICORN_CMD_ARGS='--workers=4 --bind=0.0.0.0:5000'
ExecStart=/bin/sh -c 'cd /home/jenkins/.jenkinsworkspace/SchoolDatabase-Project- && gunicorn3
app:app'
[install]
WantedBy=multi-user.target
EOF

sudo cp /tmp/app.service /etc/systemd/system.app.service
sudo systemct1 daemon--reload
sudo systemct1 start app"