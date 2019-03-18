1. Prerequisite: Install Java
2. Prerequisite: Python 2.7.x, 3.5.x, or 3.6.x and pip
3. Prerequisite: Install Pip
4. Prerequisites: Install pyyaml for reading the configuration from yaml file
    sudo pip install pyyaml
    #sudo apt update
    #sudo apt install python-pip

How to run the file
python h2oinstaller.py --cmd install

Note: cmd will take the params <br/>
      install : install the latest h2o3.<br/>
      run: runs the H2o3<br/>
      uninstall: uninstall the installed h2o3<br/>
      upgrade: upgrade to the latest h2o3 from previous version<br/>
      status: shows the h2o status<br/>

Ex:<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py
usage: h2oinstaller.py [-h] --cmd {install,uninstall,upgrade,status,run}
h2oinstaller.py: error: argument --cmd is required

Ex:
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd status
h2o status
ubuntu@ip-10-100-1-237:/tmp/h2opython$

Ex:
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd install
h2o install
installing pre requisites
:
starting h2o
Checking whether there is an H2O instance running at http://localhost:54321. connected.
--------------------------  ---------------------------------------------------
H2O cluster uptime:         21 mins 46 secs
H2O cluster timezone:       Etc/UTC
H2O data parsing timezone:  UTC
H2O cluster version:        3.22.1.6
H2O cluster version age:    4 days
H2O cluster name:           H2O_from_python_ubuntu_qw4pot
H2O cluster total nodes:    1
H2O cluster free memory:    1.724 Gb
H2O cluster total cores:    2
H2O cluster allowed cores:  2
H2O cluster status:         locked, healthy
H2O connection url:         http://localhost:54321
H2O connection proxy:
H2O internal security:      False
H2O API Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, Core V4
Python version:             2.7.15 candidate
--------------------------  ---------------------------------------------------
H2o session is running. Press Ctrl + Z to run the H2o process in background.
^Z
[1]+  Stopped                 python h2oinstaller.py --cmd install

Note: H2o process is running in background. We need to kill it manually or it will be running till next boot.


Ex :
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd status
h2o status
Name: h2o
Version: 3.22.1.6
Summary: H2O, Fast Scalable Machine Learning, for python
Home-page: https://github.com/h2oai/h2o-3.git
Author: H2O.ai
Author-email: support@h2o.ai
License: Apache v2
Location: /home/ubuntu/.local/lib/python2.7/site-packages
Requires: future, tabulate, requests, colorama
ubuntu@ip-10-100-1-237:/tmp/h2opython$


Ex:
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd upgrade
h2o upgrade
Uninstalling h2o-3.22.1.6:
  Successfully uninstalled h2o-3.22.1.6
h2o uninstall completed
h2o install


It uninstalls and then followed by install.



