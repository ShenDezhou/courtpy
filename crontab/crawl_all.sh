#!/usr/bin/env bash
cd ~/courtpy
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_all.log"
echo $path_to_log
scrapy mc_crawl_all -s LOG_FILE=$path_to_log &
