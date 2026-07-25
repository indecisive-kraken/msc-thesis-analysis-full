#!/bin/bash

PIP_VERSION = test $(pip --version)
PACKAGE_MANAGER = getPackageManager()
REQUIREMENTS_DIRECTORY =
PWD = $(which pwd)

#Adjust based on your distro, I have added most of the mainstream distros
getPackageManager() {

}
#make it with case esac because for some kind of reason the python interpreter could be installed and the pip version could not (and vice versa)
if [[ PIP_VERSION == 0 ]] then
  #If you want a more customized environment check out pyvenv: or compile from source
  sudo $PACKAGE_MANAGER install python3
fi

if [[ $PWD != $REQUIREMENTS_DIRECTORY ]] then
  test -s $REQUIREMENTS_DIRECTORY
  cd $REQUIREMENTS_DIRECTORY
  python3 -m venv $REQUIREMENTS_DIRECTORY
  source ./bin/activate
  pip install -r requirements.txt

  if [[ PIP_VERSION ]]
else
  echo "Something went very wrong, fix it yourself."
fi