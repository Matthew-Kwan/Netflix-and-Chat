# HackTheNorth2021
 
# Introduction
Netflix and Chat is a Chrome Extension for Netflix which provides additional functionality to your Netflix viewing experience. With Netflix & Chat, we provide users the ability to share their thoughts and comments on their favorite movies/tv-shows and read what others had to say about a certain scene. We hope that our extension provides a greater sense of community as we find ourselves increasingly isolated through the current pandemic. 

## How We Built It. 
Lots and lots of JavaScript - also Python. We didn't use any of the category APIs (although we really wanted to, we just didn't end up needing them except for the app, which was not completed), and so everything was done from scratch!

The front end was managed in the usual Chrome extension framework, using HTML, CSS, and JS. We ran into difficulties adjusting and reading from Netflix's player, as they have preventative measures for some extensions (for example, if you share your screen on discord it will often be a black screen).

The JavaScript within the frontend was rather complicated, requiring us to use local sockets to communicate between multiple scripts. This was because we always had to keep the chat updated, even if they skipped or went back in time. Netflix did not make our job easy.

The Speech Recognition was done using inbuilt Chrome functions, as we trained the model to recognize advanced grammar.

To communicate with the backend, we used post and get requests from the clients.

The backend was done with Django (in Python) and hosted on Replit. Although we originally wanted to use Cockroach DB, we faced difficulties with the API as it seemed to stop working during the night, so we switched to Django's default, SQL.
