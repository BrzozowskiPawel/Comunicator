# Comunicator
A program that enables text communication between users using an Internet connection.

## Table of Contents

- [Descripition](#description)

- [Demo](#demo)

- [Connection](#connection)

- [Disconnection](#disconnection)

- [Build guide](#build-guide)

- [Improvements](#improvements)

## Description
This program was created to enable communication between computer users. A minimum of 2 computers are required for the successful operation of the program. One of the users starts the server and the rest as a client can connect to it. Communication is based on the Half-Duplex model.

## Demo
View of the program from the perspective of a server-type user.
<img src="readme_files/server.gif" alt="drawing" width="834"/> 

The appearance of the program from the perspective of the client type.
<img src="readme_files/client.gif" alt="drawing" width="566"/> 

## Connection
To connect, start the server first. Then, information about the IP address of the server will be sent. By default, port 5050 is set (both on the client and server side). The IP address should be provided to the client to allow him to join the server.

## Disconnection
To disconnect simply type command  ```!DISCONNECT```. You have to send is as a message. Please note that this command can only be used as client not a server.

## Build guide

You can use IDE or Terminal to build this project. Below I present the instructions on how to run the program using the terminal.

1. Clone the repository.
2. Unzip project
3. start server or client.
```
python3 server.py
```
4. Enter / provide the IP address to the client

## Improvements
In future code versions I would like to implement asymmetric encryption and also improve the UI.
