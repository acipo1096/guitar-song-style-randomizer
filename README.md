# Guitar Song/Style Randomizer

## Description

A web application that calls a Python script, which returns a random artist and song (or a random guitarist and his "style" of playing) from a Google Sheet. To view a demo of this application, click [here](https://youtu.be/iqWX4EQsjdk). (I only showcase the song randomizer here - to learn more about randomizing styles, see below.)

## History/Motivation

As a guitarist who can now play over 500 songs, I would often get asked by people to play a song, only for me to stare blankly into space - I knew so many songs that it was hard for me to pick one. I started writing all the songs I learned in a Google Sheet, but while it gave me a visual of how many songs I could play, it didn't solve the problem as I would still spend minutes scrolling around.


In 2020, I was asked to learn Python and pandas for my job. The plan was to build a web application that could track student grades and data in a web interface, using data pulled from Google Sheets. Unfortunately, the project was put on hold due to COVID-19, and I was furloughed for 3 months. I decided to use that time off to improve my IT and programming skills. I developed two Python scripts that would connect to and return data from a Google Sheet. It worked well, but didn't look appealing and could only be run from a terminal.

2 years later, after having a better understanding of web development technologies, I wondered if I could create a web interface that could run my Python script without me having to reinvent the wheel. And, instead of me choosing a song, I figured, "Why not let the technology do it for me?"

## Usage

This app uses a blend of many different technologies:
- The front end was built with HTML, CSS, JavaScript, and Bootstrap 5
- The backend runs on NodeJS/Express
- The data is pulled from two separate Google Sheets

When I press "What's Next?" on the front end, it makes a GET request to the API hosting the respective Python script, which pulls the Google Sheet data, organizes and calls a specific song and artist with pandas, and randomly returns one artist and song to the front end. The process takes about 3 seconds to run.

## Note: What are Guitar "Styles"?

When many guitarists start playing guitar (myself included), they learn songs, guitar solos, and "licks" from their favorite players. A "lick" is a short passage of notes that sounds interesting. Many guitarists (including the greats) steal licks from their influences and use them in their playing, which eventually evolves into a unique style.
What can sometimes happen is that guitarists just play licks instead of understanding how notes and "phrases" work together differently to serve different songs.

After years of playing, I started to look at the way guitarists put their notes together instead of just blindly copying them. (For example, a guitarist might constantly play 4 notes together quickly, while another likes to play one note at a time.)

While on the *Guitar Styles* tab, a new guitarist and his style of playing is randomized every 60 seconds. During that time, I'll practice soloing in that guitarist's style, even if I wouldn't normally do that on a certain song. This forces me to play a certain way, breaking out of creative ruts and generating new ideas for my playing.
