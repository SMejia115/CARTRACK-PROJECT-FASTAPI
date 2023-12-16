* Developed: by Santiago Mejía Orejuela.
* E-mail: s.mejia6@utp.edu.co

# Back

Backend developed with python 3.11.6.

## To install python libraries (project dependencies):

- Step 1 - (Install python):
You must have python installed on your computer. You can download it from: [Python](https://www.python.org/downloads/)

- Step 2 - (Create the python virtual environment for the backend):
In the terminal, go to the Back folder and type the command `python -m venv vevn`.

- Step 3 - (Start the virtual environment): 
In the terminal, you type the following commands one by one:
`cd venv/Scripts`
`activate`
`cd ../..`

- Step 4 - (Install dependencies):
In the terminal, type the following command:
`pip install -r requirements.txt`

## To run the API:

In the terminal, you go to the Back folder and type the following command:
`uvicorn main:app --reload --port 5000`