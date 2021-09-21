# Clickfait @ Hack The North 2021
## Inspiration
With the enormous prevalence of the internet in the modern world, clickbait runs rampant throughout social media and entertainment. Whether for sharing information or gaining a profit, sensationalizing and withholding information is common in media titles in order to attract views and attention. However, many consumers (us included) often find clickbait irritating, as the enticing title is often obnoxious and a gross exaggeration of the information actually presented. Thus, we decided to build **Clickfait**: a web app to help users avoid disappointment by detecting likely instances of clickbait beforehand.

## What it does
Clickfait is a web app which analyzes a media title and determines whether it can be considered clickbait or not. By inputting the title of a media piece, Clickfait analyzes the “clickbaitiness” of the title by considering two factors: “withhold”, which is the title’s tendency to obscure crucial information that may entice a user to click, and “sentiment”, which is a measure of how sensationalized the title is. Finally, Clickfait returns the data from this analysis to the user in a clear, visual manner.

## How we built it
We built Clickfait using a database of clickbait vs. non-clickbait titles, using Google’s Natural Language API and TensorFlow for training a model for clickbait recognition. Moreover, we decided to build a web app for Clickfait for increased accessibility to users.

## Challenges we ran into
- Running the application with the front end
- Initially low accuracy when training the Tensorflow model

## Accomplishments that we're proud of
- Developing a model in Tensorflow with 95.5% accuracy!

## What we learned
- Use and creation of TensorFlow models, Google Cloud (Natural Language AI, App Engine), Flask, Figma, and the nightmare that is TXT records (thanks Domain.com for clickfait.tech)

## What's next for Clickfait
- Expanding on Clickfait’s detection abilities. It would be awesome to implement thumbnail detection for media to detect traits common to clickbait (e.g. open mouths & eyes, red arrows and circles, etc.)
- Extending from a web app to a browser extension. The extension would function by automatically analyzing the titles on the user’s screen for greater convenience.

## Debrief/post-mortem
As an overall concept, Clickfait had finalist potential at this year's Hack the North. We had the right technology, the talent, and the willpower (or rather, enough to stay up until 5am). Unfortunately, several things didn't pan out the weeks before and especially the hours during the hackathon, for one reason or another. Perhaps it was a lack of oversight in planning, tech. preparations, and/or real-life circumstances. And that's perfectly fine — this is a learning process. All of us on the team have grown tremendously as a result of this massive effort, and no matter how presentable our project is (we have amazing data!), I am still very proud of what we have accomplished in such a short time, inside and outside of this repository. I hope you can appreciate that too. -Victor
