# Use the latest slim version of Debian
FROM --platform=$TARGETPLATFORM debian:bookworm-slim

# Set ARG for platform-specific commands
ARG TARGETPLATFORM

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set up SSH
RUN mkdir /var/run/sshd && \
    echo 'root:toor' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create and activate Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
WORKDIR /app
COPY . .

# Copy initial .bashrc with virtual environment activation to a temporary location
COPY .bashrc /etc/skel/.bashrc

# Copy the script to ensure .bashrc is in the root directory
COPY initialize.sh /usr/local/bin/initialize.sh
RUN chmod +x /usr/local/bin/initialize.sh

# Expose SSH port and FastAPI port
EXPOSE 22 8000

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Init .bashrc and start services
CMD ["/bin/bash", "-c", "/usr/local/bin/initialize.sh && /usr/sbin/sshd -D & uvicorn api.routes:app --host 0.0.0.0 --port 8000"]