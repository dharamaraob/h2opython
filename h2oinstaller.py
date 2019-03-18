#/usr/bin/python3
import argparse
import os
import time
import sys
import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def prerequisites():
    print ("installing pre requisites")
    os.system("pip install -r requirements.txt")

def run():
    print ("starting h2o")
    import h2o
    # h2o.init(ip=cfg["h2o"]["ip"], port=cfg["h2o"]["port"])
    h2o.init()
    print ("H2o session is running. Press Ctrl + Z to run the H2o process in background.")
    while True:
        time.sleep(20)
    print ("h2o running succesfully in background.")

def install():
    print ("h2o install")
    prerequisites()
    #os.system("pip install http://h2o-release.s3.amazonaws.com/h2o/rel-xu/6/Python/h2o-3.22.1.6-py2.py3-none-any.whl")
    if sys.platform == "darwin kernel":
        os.system("pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o --user")
    else:
        os.system("pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o")
    run()

def uninstall():
    os.system("pip uninstall h2o -y")

def upgrade():
    print ("h2o upgrade")
    uninstall()
    print ("h2o uninstall completed")
    time.sleep(10)
    install()
    run()

def status():
    print ("h2o status")
    os.system("pip show h2o")

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--cmd',
                    help='Require install or upgrade' ,required=True, choices=['install', 'uninstall', 'upgrade','status','run'])

args = parser.parse_args()
if args.cmd == "install":
    install()
elif args.cmd == "uninstall":
    uninstall()
elif args.cmd == "upgrade":
    upgrade()
elif args.cmd == "run":
    run()
else:
    status()
