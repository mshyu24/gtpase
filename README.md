# Data Processing for GTPase Assay

a quick little script to convert data. written for phosphate assay, but any linear relationship run at large plate scale will do, just trade values in the process.py script

## Repository Contents:
1. This README
2. A copy of the MIT License
3. requirements.txt, for quick install
4. process.py, the python script that will turn the input into the output

## Setup tl;dr:
Download the repository
Make a new virtual environment
Install requirements
Add your files to the folder the script is in (input and output)
Run the script

## Setup (click by click, for Mac users):
All things in curly brackets can be replaced with the relevant file name etc.

1. Download the repository (green button on main page)
2. Put the folder somewhere convenient, probably in a folder that doesn't have spaces in its name or your desktop
3. Open Terminal, navigate to that folder (use "cd {directory name}" to go to a particular folder, use "ls" to list what is in the folder you are currently in, use "pwd" to get the path to the folder you're currently in)
4. Navigate into the folder you downloaded
5. Make a new virtual environment (type "python3 -m venv {virtual environment name}")
6. Activate your new virtual environment (type "source {virtual environment name}/bin/activate")
7. Make sure you can run the python script (type "chmod +x process.py")
8. Use pip to install the requirements file (type "pip install -r requirements.txt")
9. At this point you should be set! To test your setup, you can use the sample file and the run instructions (move sample file to the same folder as the python script and make a new output folder)

To run:
python3 process.py {input file name} {output file name}

You will see file read and file written messages print to the command line as the script runs

## Formatting files:
Recommendation: name the files without spaces to avoid issues

Input should be a single Excel sheet with plate data as columns, in order you want it, with well number as the header row (e.g. a1, a2, a3...). Each cell should contain the reading.
There should be no column with row labels.

## Processing details


This will just apply an affine transformation (see comments to fill in your coefficients from your standard).

Name your outfile, it will be generated automatically

Put your in file in the same folder as the python script and you're good to run!
