FROM archlinux:latest

RUN pacman -Syyu --noconfirm \
    && pacman -S --noconfirm python python-pip zstd p7zip gcc \
    && python -m venv /venv \
    && /venv/bin/pip install --upgrade pip
    
RUN mkdir /app/
WORKDIR /app/
COPY . /app/

# Activate the virtual environment and install Python packages
RUN /venv/bin/pip install -U setuptools \
    && /venv/bin/pip install -U -r requirements.txt

# Use the virtual environment for the CMD
CMD ["/venv/bin/bash", "start.sh"]
