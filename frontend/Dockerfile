FROM python:3.12-slim-bookworm

RUN useradd -u 8877 user
RUN mkdir /home/user
RUN chown -R user /home/user

WORKDIR /home/user/
RUN mkdir cgdtracker-frontend
WORKDIR /home/user/cgdtracker-frontend

COPY frontend/requirements.txt /home/user/cgdtracker-frontend/requirements.txt

RUN pip install uv -q
RUN uv pip install -r /home/user/cgdtracker-frontend/requirements.txt --system

COPY frontend/src /home/user/cgdtracker-frontend/src
COPY frontend/pyproject.toml /home/user/cgdtracker-frontend/pyproject.toml

RUN uv pip install -e . --no-deps --system

CMD ["streamlit", "run", "src/cdgtracker_frontend/app.py", "--server.port", "80"]