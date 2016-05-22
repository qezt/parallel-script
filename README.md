# README

## What

This is a tiny script that executes a list of commands in parallel.

It requires each command to be independent.

## Why

I do a lot of CPU intensive processing which doesn't use all my CPU cores. Such a waste.

## How

When you have a bunch of commands stored (on generated on the fly), you could pipe line into the script and the script will schedule executions for you.

For example, if you want to convert all PNG file into WEBP files, you could simply do this:


    find . -name '*.png' | sed 's/\(.*\).png/convert \1.png \1.webp/' | python parallel.py

Notice the speed difference yet?

If you encounter any problem, you are welcome to fork it and file pull requests.

## Licence

Nahhhhhhhhhhhhhhhhh.

You can use it freely.
