# Set up environment

We use pipenv to set up python environment.

pipenv: https://pipenv.pypa.io/en/latest/

Good point of pipenv
- You no longer need to use pip and virtualenv separately. They work together.
- Managing a requirements.txt file can be problematic, so Pipenv uses Pipfile and Pipfile.lock to separate abstract dependency declarations from the last tested combination.

So you need to install pipenv.(And I set python version 3.8)

After installing pipenv,

1. change directory to `src` (e.g. cd Tweet_Analyzing/src)
2. `pipenv install` in `src` directory (this command install library such as requests, pytest)
3. When command `pipenv run test`, you don't catch error , so you succeed to set up


