#!/bin/bash
if [ ! -f /root/.bashrc ]; then
    cp /etc/skel/.bashrc /root/.bashrc
fi