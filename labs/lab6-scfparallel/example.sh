#!/bin/bash

# Set file name
fileName="testFile.txt"

# Create file
touch $fileName

# Intro message
echo "I'm your new test script!" >> $fileName
echo >> $fileName
echo >> $fileName

# Fill it with some things
for i in {1..10}
do
  echo "$i" >> $fileName
done

# Finish it out
echo >> $fileName
echo >> $fileName
echo "All Finished!" >> $fileName
