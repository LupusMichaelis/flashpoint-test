#!/bin/bash

basedir=$(realpath $(dirname $0)/..)
cd $basedir
. bin/activate
python manage.py $@
