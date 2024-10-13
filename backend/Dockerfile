FROM python:3.12-slim-bookworm

RUN useradd -u 8877 user
RUN mkdir /home/user
RUN chown -R user /home/user

WORKDIR /home/user/
RUN mkdir cgdtracker-backend
WORKDIR /home/user/cgdtracker-backend

COPY frontend/requirements.txt /home/user/cgdtracker-backend/requirements.txt

RUN pip install uv -q
RUN uv pip install -r /home/user/cgdtracker-backend/requirements.txt --system

COPY frontend/src /home/user/cgdtracker-backend/src
COPY frontend/pyproject.toml /home/user/cgdtracker-backend/pyproject.toml

RUN uv pip install -e . --no-deps --system

CMD ["streamlit", "run", "src/cdgtracker_frontend/app.py", "--server.port", "80"]