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
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py<br/>
usage: h2oinstaller.py [-h] --cmd {install,uninstall,upgrade,status,run}<br/>
h2oinstaller.py: error: argument --cmd is required<br/>

Ex:<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd status<br/>
h2o status<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$<br/>

Ex:<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd install<br/>
h2o install<br/>
installing pre requisites<br/>
:<br/>
starting h2o<br/>
Checking whether there is an H2O instance running at http://localhost:54321. connected.<br/>
--------------------------  ---------------------------------------------------<br/>
H2O cluster uptime:         21 mins 46 secs<br/>
H2O cluster timezone:       Etc/UTC<br/>
H2O data parsing timezone:  UTC<br/>
H2O cluster version:        3.22.1.6<br/>
H2O cluster version age:    4 days<br/>
H2O cluster name:           H2O_from_python_ubuntu_qw4pot<br/>
H2O cluster total nodes:    1<br/>
H2O cluster free memory:    1.724 Gb<br/>
H2O cluster total cores:    2<br/>
H2O cluster allowed cores:  2<br/>
H2O cluster status:         locked, healthy<br/>
H2O connection url:         http://localhost:54321<br/>
H2O connection proxy:<br/>
H2O internal security:      False<br/>
H2O API Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, Core V4<br/>
Python version:             2.7.15 candidate<br/>
--------------------------  ---------------------------------------------------<br/>
H2o session is running. Press Ctrl + Z to run the H2o process in background.<br/>
^Z<br/>
[1]+  Stopped                 python h2oinstaller.py --cmd install<br/>
<br/>
Note: H2o process is running in background. We need to kill it manually or it will be running till next boot.<br/>


Ex :<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd status<br/>
h2o status<br/>
Name: h2o<br/>
Version: 3.22.1.6<br/>
Summary: H2O, Fast Scalable Machine Learning, for python<br/>
Home-page: https://github.com/h2oai/h2o-3.git<br/>
Author: H2O.ai<br/>
Author-email: support@h2o.ai<br/>
License: Apache v2<br/>
Location: /home/ubuntu/.local/lib/python2.7/site-packages<br/>
Requires: future, tabulate, requests, colorama<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$<br/>


Ex:<br/>
ubuntu@ip-10-100-1-237:/tmp/h2opython$ python h2oinstaller.py --cmd upgrade<br/>
h2o upgrade<br/>
Uninstalling h2o-3.22.1.6:<br/>
  Successfully uninstalled h2o-3.22.1.6<br/>
h2o uninstall completed<br/>
h2o install<br/>

It uninstalls and then followed by install.<br/>
