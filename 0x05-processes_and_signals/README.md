[![Holberton logo](https://secure.meetupstatic.com/photos/event/6/9/5/0/600_445886960.jpeg)](https://www.holbertonschool.com/)

***

# Processes And Signals

### Description
Learning how to use ps, pgrep, pkill, kill, exit, and trap commands in bash

### Concepts
At the end of this project you are expected to be able to explain, without the help of Google:

*    What is a PID
*    What is a process
*    How to find a process PID
*    How to kill a process
*    What is a signal
*    What are the 2 signals that cannot be ignored

### File Content
This repository contains the following files*:

| File | Task |
| :--- | :--- |
| 0-what-is-my-pid | Write a Bash script that displays its PID. |
| 1-list_your_processes | Write a Bash script that displays a list of currently running processes. |
| 2-show_your_bash_pid | Using your previous exercise command, write a Bash script that displays line containing the bash word, this allowing you to easily get the PID of your Bash process |
| 3-show_your_bash_pid_made_easy | Write a Bash script that displays the PID, along with the process name, of processes which name contains the word bash. |
| 4-to_infinity_and_beyond | Write a Bash script that displays To infinity and beyond indefinitely. |
| 5-kill_me_now | We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this. |
| 6-kill_me_now_made_easy | Write a Bash script that kills 4-to_infinity_and_beyond process. |
| 7-highlander | Write a Bash script that displays: To infinity and beyond indefinitely, With a sleep 2 in between each iteration, I am invincible!!! when receiving a SIGTERM signal. |
| 8-beheaded_process | Write a Bash script that kills the process 7-highlander. |
| 100-process_and_pid_file | Write a Bash script that: Creates the file /var/run/holbertonscript.pid containing its PID, Displays To infinity and beyond indefinitely, Displays I hate the kill command when receiving a SIGTERM signal, Displays Y U no love me?! when receiving a SIGINT signal, Deletes the file /var/run/holbertonscript.pid and terminate itself when receiving a SIGQUIT or SIGTERM signal. |
| 101-manage_my_process | Write Bash (init) script 101-manage_my_process that manages manage_my_process. |
| 102-zombie.c | Write a C program that creates 5 zombie processes. |

> *All test files excluded
### Author
Diego Castellanos
