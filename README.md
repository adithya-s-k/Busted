# Busted

**Busted** - a easy way of using you laptop webcam as a security device. The program will detect when there is motion and send you a video if anything is stolen

This project was built for the [Tri NIT Hackthon](https://unstop.com/hackathon/tri-nit-hackathon-national-institute-of-technology-karnataka-nitk-surathkal-254063)

***[Project Video](https://youtu.be/fEzzeSZ28zQ)***

## Problem Statement
**ML03 Track** : CCTVs have been around for over 20 years. Traditionally security agents and operations managers have been tasked with real-time CCTV camera monitoring to detect abnormal behavior or situations in areas under surveillance or for post-event investigation. They have needed to review hours or days of footage to extract evidence and understand what occurred at the time of the incident. Due to time constraints, it is difficult to catch on all the relevant data required to solve the issue. Also, humans are prone to errors making it more difficult to efficiently process the data. The aim of this problem statement is to build a system for the CCTV industry that independently identify and classify objects and patterns to configure intelligent alerts or gather evidence of the incident Solution: Theft detection: Detecting changes in a room in real-time to check for stolen items and give feedback to the user in video and text format The product will identify the difference in frames immediately after the motion has ceased to exist. Once the difference has been identified it will give output, the output being the missing object (or objects). The feedback is sent to the user (or users) in the video(mp4) and text format via mail. Voice recognition will make sure the user is not alerted falsely when a family member or acquaintance enters the room and moves an object.
## Introduction
The task to achieve is using video metadata and machine learning to build a system for real-time alerts, triggering real-time calls to action when certain objects or behaviors are detected or when anomalous activity occurs,
## Proposed Method

 - Our product focuses on theft prevention and burglar identification using real-time video capture.
 - -It sends feedback, in video and text, to the user through mail and alerts them about the situation.
 - This video capturing will be done using cv2 ML library.
 - The difference in frames before and after motion is detected is done using skimages.
 - The datetime module is used to get the time at which motion was detected at the scenario and the time when the object(or multiple objects) went missing.

## Work done and Results
The product will identify the difference in frames immediately after the motion has ceased to exist. Once the difference has been identified it will give output , the output being the missing object (or objects). The feedback is sent to the user (or users) in video(mp4) and text format via mail. Voice recognition will make sure the user is not alerted falsely when a family member or acquintance enters the room and moves an object.

## Conclusion
Keeping in mind the busy schedules of people we have arrived at the conclusion that automation is the way to go. In our project we automate security, Keeping belongings safe when the owner is not around

## Installation

  

Download the zip file or clone the repository

  

```bash

git clone https://github.com/adithya-s-k/Busted.git

```

Go to the repository where you have cloned and run app.py

```bash

python main.py

```

## Tech Stack

  
**Language:** Python
**Libraries:** Tkinter , Python Image Library , Email.message
  
  

## Authors

  

- [@adithya-s-k](https://github.com/adithya-s-k)

- [@aayushsenapati](https://github.com/aayushsenapati)

- [@aaryanhb](https://github.com/aaryanhb)
  

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)]()

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-s-kolavi-127a561a8/)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/adithya_s_k)

  
  

## Contributing

  

Contributions are always welcome!

  

You can fork the repository and create a pullrequest for contributing.

  

Please adhere to this project's `code of conduct`.
