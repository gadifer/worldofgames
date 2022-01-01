FROM python:3

WORKDIR /training/devops
#RUN python3 -m venv venv
#RUN . venv/bin/activate

# Install dependencies:
COPY requirements.txt ./
COPY MainScores.py ./
COPY Utils.py ./
COPY scores.txt ./
COPY oldscore.txt ./
ADD templates/Scores.html ./templates/Scores.html/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./MainScores.py", "runserver", "0.0.0.0:5000"]
