#!/bin/bash

lat_plane=$1
lat_vert=$2
dir_name="C_plane${lat_plane}_vert${lat_vert}"
echo "Creating directory: $dir_name"
mkdir -p "$dir_name"
