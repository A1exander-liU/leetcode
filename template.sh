#!/bin/bash

pythonContents="
class Solution:
  def function(self) -> None:
    return
"
readmeContents="
# Problem


### Example 1


### Solution
"

arg1=$1
mkdir $arg1
cd $arg1
echo $readmeContents >README.md
echo $pythonContents >solution.py
