Project Kruipertje 1.0
===============

Description
------------
The application Kruipertje is developed by  Yarince Martis, Mick Tuit, Robert Verkerk & Ugur Ekim, a project group at the University of Applied Sciences Arnhem and Nijmegen in 2017. <br>
It searches for URLs on web pages. The found URLs are added to a queue and crawled in the next iteration. The full HTML is saved in Redis.<br>

After crawling, the parser is started. It searches for valuable company information in the saved HTML. <br>
The found information is saved in Elasticsearch and read by Kibana to be showed in different statistics and diagrams. <br>
On the different dashboards, information about Kruipertje can be seen. Like how many URLs are crawled and what websites have what kind of information. 

The dashboard is accessible via the servers ip address and the port 5601. <br>
Example: 172.0.0.1:5601


Work environment
----------------
To run the application succesfully you need to install the next few software packages:
1. [Python 3.6.1](https://www.python.org/) with pip and setuptools
2. [MySQL Community Server 5.7.18](https://dev.mysql.com/downloads/mysql/)
3. [Redis 2.8.3](https://redis.io/)
4. [Elasticsearch 5.4.1](https://www.elastic.co/)
5. [Kibana 5.4.1](https://www.elastic.co/products/kibana)
6. [Filebeat 5.4.1](https://www.elastic.co/products/beats/filebeat)


Starting the application for the first time
-------------------------------------------
- Make a virtual environment and activate it.
- Run python setup.py --install <br>
- Run app/\_\_main\_\_.py


Possibilities for the future
----------------------------
- Fix the net number regex in the Phone number Module.
- Preload the blacklist at the start of the program. 
  - When running a high amount of threads the blacklist file is opened too many times. 
- Restart a thread if an error occurs
