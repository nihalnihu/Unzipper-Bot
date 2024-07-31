# Start from the Arch Linux image
FROM archlinux:latest

# Update and install necessary packages including git
RUN pacman -Syyu --noconfirm \
    && pacman -S --noconfirm python python-pip zstd p7zip gcc git \
    && python -m venv /venv \
    && /venv/bin/pip install --upgrade pip

# Create and set the working directory
RUN mkdir /app/
WORKDIR /app/

# Copy application files
COPY . /app/

# Install Python dependencies
RUN /venv/bin/pip install -U setuptools \
    && /venv/bin/pip install -U -r requirements.txt
