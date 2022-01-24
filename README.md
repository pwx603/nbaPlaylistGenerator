# Nba Reddit Stram Generator#

## About ##
Generates m3u playlist for nba games from https://reddit.rnbastreams.com/ and upload it to AWS s3.
Fully containerized, so it can be easily ran remotely on Cloud Services via interval scheduling or event-based triggers.

more on m3u: https://en.wikipedia.org/wiki/M3U

m3u files can be played with any media player that supports the format.

## Get Started ##

Pre-req: use aws cli to set your aws credentials.

1. Install docker and docker-compose - https://docs.docker.com/get-docker/
2. `$ cd nbaRedditStreamPlaylistGenerator`
3. `$ docker-compose build`
4. `$ docker-compose up --abort-on-container-exit`

