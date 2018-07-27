Example of how to use a computer to read from an API and use the USB serial to send messages to a Circuit Playground Express.

The file to run on the computer is `main.py`.  The code file that should be saved on the CPX is `cpx/code.py`.

The computer script uses `pyserial` and `requests`.  Remember to either `pip install -r requirements.txt` on the computer or `pipenv install` if you have `pipenv`.