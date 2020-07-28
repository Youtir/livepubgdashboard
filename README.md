# A Sort of Real-time Dashboard for PUBG

## A WORK IN PROGRESS
This project will make use of the data available from the PUGB API (https://developer.pubg.com/).  We will use Apache Kafka (https://kafka.apache.org/) and Apache Druid (https://druid.apache.org/).

## Introduction

I wanted to play around and get to know Apache Druid and how I could make a real-time dashboard.  For fun I decided to try and send telemetry data from a PUBG game to Druid via Kafka.  A dashboard would then query the data in Druid providing a pseudo real-time status of the game.

## Setup

After cloning the repo, `pip install -r requirements.txt` to install all the needed packages.

Head over to https://developer.pubg.com/ and get a developer key and download some telemetry data.

Follow the instructions to download and install Kafka and Druid.  Follow this guide ingest some data into Druid to build the table schema https://druid.apache.org/docs/latest/tutorials/tutorial-kafka.html.

Once Druid and Kafka are running, and you have a telemetry file, run `process_data.py` and `app.py`.  The data will begin to stream into Druid via Kafka.  The dashboard auto-refreshes and will get the latest state of all players as the telemetry data is processed.