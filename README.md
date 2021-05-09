# ZooZoos
Team Name: ZooZoos

Team Members: Avni Mittal, Khushi Baghel, Khushboo Thakur
First Year Btech, IIT Mandi

Social Problem: Healthcare and Medicine

Brief Description: One Stop for covid patients for finding covid resources through advanced search on Twitter. Many people don’t know how to search for relevant hashtags and words on Twitter, we do that for them with our web application ‘Cov-Track’. 

Tech Stack: We’ll be using HTML, CSS, flask, and Python. We are using the Twitter API of ‘Tweepy’ for live streaming tweets. We are taking input from the user about their location and their needs, and based on that we’ll show them the required tweets.

Use Cases and Future projects: India is experiencing a covid Tsunami at the moment, and in this time people have turned to social media for help. This application helps those people in need, linking people from various backgrounds on social media and helping them help each other. There is no restriction on the application's possible potential; it may be modified  to accommodate other conditions such as other illnesses or emergency circumstances. For example, anyone running out of insulin may search for and locate suitable persons who could have it at the moment. This may also be changed to show job vacancies to allow prospective applicants to apply for them.
# Working:
We are using HTML and CSS for our frontend and python and flask for our backend, for live streaming the tweets we are using Twitter API named Tweepy. We take input from the user of their City and the resources needed and then run a search using Tweepy, 50 most recent and relevant tweets are returned by the function ‘postweets()’ and stored as a list in tweets. Through different attributes of Tweepy, specifically text and time we store the major text of these tweets in the list ‘text’ and the time of creation in the list ‘time’, which are then returned to the frontend and run there using jinja.
