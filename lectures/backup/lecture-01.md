% Lecture 01 - Course Introduction
% None
% 11th January, 2017

Overview of This Lecture
------------------------

**Course Administration**

* Course details
* Course schedule
* Assessment Schemes
* Policies and Rules

**Course Content Overview**

* Computer networking and data communication
* Network programming (socket programming)
* Client-server architecture
* Applications
* Programming requirements (Python)

Course Instructors
------------------

**Albert Au Yeung – Lecturer**

* Email: cmauyeung@ie.cuhk.edu.hk
* For lecture content, materials, details of assignments, project arrangements, reference materials, etc.

**Marco Leung – Teaching Assistant**

* Email: mtleung@cuhk.edu.hk
* Contact Marco if you need specific help when working on your assignments and project

**Note**: Both of us do NOT have regular office hours on campus, email us first whenever you need help.

Lectures
--------

**Venue & Time**

* TBC
* 7:00pm – 9:30pm
* Lecture dates (12 lectures):
    + 11th, 18th, 25th January
    + 1st, 8th, 22nd February
    + 1st, 8th, 15th, 22nd, 29th March
    + 12th April
* Project Presentation:
    + 26th April


Course Schedule
---------------

Our 12 Lectures will following (roughly) the schedule below:

* 
* 
* 
* 

Assessment Scheme
-----------------

* **10%** - Attendance (From Lecture 2 to Lecture 12)
* **50%** - Programming Assignment
* **40%** - Course Project


Programming Assignments
-----------------------

* 

Course Project
--------------

* 


What should you expect?
-----------------------

Take this course if you:

* Have background in computer networks and related concepts
* Have basic understanding or willing to learn the Python Programming Language
* Would like to challenge yourself with interesting programming and system design problems


Some Rules
----------

What you should do in this course?

* Attend the lectures, and raise questions whenever you have any
* Seek help as **early** as possible (e.g. if you have difficulties in picking up Python programming, or if you cannot set up the development environment)
* Feel free to make **suggestions** to the course and/or lectures
* Do your own assignments, and do NOT make your work publicly available before the deadline
* All late submissions of assignments will receive **30%** penalty (up to **one week**)


Honesty in Academic Work
------------------------

* Zero tolerance on cheating and plagiarism
* Read: [http://www.cuhk.edu.hk/policy/academichonesty/](http://www.cuhk.edu.hk/policy/academichonesty/)
* Cite references whenever you use materials from any other sources
* It will be considered plagiarism no matter you copy other’s work or allow others to copy your work

Online Materials (1)
--------------------

* Assignments will be released and collected on the CUHK E-Learning System: [https://elearn.cuhk.edu.hk/](https://elearn.cuhk.edu.hk/)
* You will submit your assignments here


Online Materials (2)
--------------------

* Course Website: [https://course.ie.cuhk.edu.hk/~iems5703/](https://course.ie.cuhk.edu.hk/~iems5703/) or [http://iems5703.albertauyeung.com](http://iems5703.albertauyeung.com)
* Lecture slides, assignments, project details, references will be available here
* For more convenient communication among us and discussions among yourselves, we will use Slack in this course: [https://iems5703-1718t2.slack.com/](https://iems5703-1718t2.slack.com/)
* Sign up for an account on slack and join the above team
* NOTE: DO NOT post any solution of assignments on Slack or any other public channels


Computer Network
----------------

* A network that allows computers to perform data communication with one
another

<center>
<img src="img/computer_network.png" width="60%">
</center>

Data Communication
------------------

* Exchange of data between two devices using some form of transmission
medium
* A simplified communication model:

<center>
<img src="img/data_communication.png" width="90%">
</center>

* Protocols: rules that govern how data is transmitted in this system

Computer Network
----------------

When we have many computers that want to talk to one another, point-to-point links become not practical, especially when the distance is too far

<center>
<img src="img/computer_network_2.png" width="100%">
</center>


Problems and Challenges
-----------------------

Challenges in Networking:

* How can data be transmitted from one node to another through the network?<br/> **(e.g. routing/switching)**
* How can we address the computers?<br/>  **(e.g. IP Address)**
* How can we identify which applications on the computers the data should be delivered to? <br/> **(port and socket)**
* How to handle error or missing data?<br/>  **(e.g. the TCP protocol)**
* What if a large amount of data is transmitted at the same time?


Applications
------------

Common Applications on the Internet

* The World Wide Web (Web servers and browsers)
* File transfer (FTP servers and clients)
* Instant messaging & video conferencing (e.g. Skype, Whatsapp, Wechat)
* Peer-to-peer file sharing
* Cloud storage
* ...


Case Studies
--------------

* World Wide Web
* Instant Messaging & Video Conferencing
* Peer-to-peer file sharing


Client Server Architecture
--------------------------

* 

Common Three Tier Architecture
------------------------------

* Presentation Tier (e.g. Webpage, App)
* Logic Tier (Carry out commands, make logic decisions, perform calculations)
* Data Tier (A database or file system storing the data of the app)

References
----------

* 
* 
* 

Introduction to Python
----------------------

What is Python?

What do people use Python for?

Setting up Environment
- Linux / Mac / Windows
- IDE? (Try PyCharm, or Visual Studio Code)
- Install Jupyter and use a IPython Notebook

Basics
- assignment
- conditions
- loops

Data Types and Data structures
- Strings, integer, float
- immutable objects / mutable objects
- List, tuples
- Dictionary


Class and functions
- Classes
- Functions

Python Style Guide
- PEP8
- indentation (use space instead of tab)
- Comments, docstrings
- common practices
- ...

Virtualenv, iPython


Concurrency
------------

(Ref: https://www.slideshare.net/TausunAkhtary/concurrent-parallel-programming)
(Ref: https://www.slideshare.net/pvergain/multiprocessing-with-python-presentation)


Running more than one tasks at the same time
* In a time-shared manner on a single CPU core
* In a truly parallel manner on a multi-core CPU


Concurrency vs. Parallelism

Concurrency: two or more calculations happen within the same time frame, and there is usually some sort of dependency between them
(example: two queues with only one coffee machine)

Parallelism: two or more calculations happen simultaneously
(example: two queues on two coffee machines)


Level of Concurrency:
* process-based (multiple programs (processes) running concurrently)
* thread-based (parts of the same process running concurrently)


Challenges in Concurency
------------------------
* Shared resources
* Race condition
* Critical section
* Deadlock
* Starvation
* ...



Thread
------

Show thread life cycle diagram



Dining Philosophers Problem
---------------------------

[Dining Philosophers Problem - Wikipedia](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both forks so that the forks become available to others. A philosopher can take the fork on their right or the one on their left as they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.


Concurrency in Python
---------------------

https://wiki.python.org/moin/GlobalInterpreterLock
Does it mean that we cannot benefit from multi-threading in Python?
(consider applications with heavy I/O operations)

