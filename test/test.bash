#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuki Nishijima
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch network_usage talk_listen.launch.py > /tmp/network_usage.log

cat /tmp/network_usage.log |
grep 'Listen: 10'
