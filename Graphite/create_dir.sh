#!/bin/bash

dim_plane=$1
dim_vert=$2
dir_name="C_plane${dim_plane}_vert${dim_vert}"
echo "Creating directory: $dir_name"
mkdir -p "$dir_name"
