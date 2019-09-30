[![Holberton logo](https://secure.meetupstatic.com/photos/event/6/9/5/0/600_445886960.jpeg)](https://www.holbertonschool.com/)

***

# HTTPS SSL

### Description
Learning how to setup a secure HTTP with SSL certificate

### Concepts
At the end of this project you are expected to be able to explain, without the help of Google:

*    What is HTTPS SSL 2 main roles
*    What is the purpose encrypting traffic
*    What SSL termination means

### File Content
This repository contains the following files*:

| File | Task |
| :--- | :--- |
| 0-https_abc* |  |
| 1-world_wide_web | Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains. |
| 2-haproxy_ssl_termination | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www. |
| 100-redirect_http_to_https | Configure HAproxy to automatically redirect HTTP traffic to HTTPS. |
### Author
Diego Castellanos
