
# This is an auto generated Dockerfile for ros:perception
# generated from docker_images/create_ros_image.Dockerfile.em
FROM wasteant/wasteant:12.5.1-cudnn-runtime-ubuntu22.04

LABEL maintainer="tannous.geagea@wasteant.com"
LABEL com.wasteant.version="1.1b1"

# [CHECK] Whether it is convenient to use the local user values or create ENV variables, or run everyhting with root
ARG user
ARG userid
ARG group
ARG groupid

# Set non-interactive mode for apt-get
# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# install mlfow
RUN pip3 install mlflow

# upgrade everything
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -q -y \
   && rm -rf /var/lib/apt/lists/*

# # Set up users and groups
RUN addgroup --gid $groupid $group && \
	adduser --uid $userid --gid $groupid --disabled-password --gecos '' --shell /bin/bash $user && \
	echo "$user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$user && \
	chmod 0440 /etc/sudoers.d/$user

RUN mkdir -p /home/$user/src
RUN mkdir -p /media/$user

RUN /bin/bash -c "chown -R $user:$user /home/$user/"
RUN /bin/bash -c "chown -R $user:$user /media/$user/"

# Create directory for Supervisor logs
RUN mkdir -p /var/log/supervisor && \
    chmod -R 755 /var/log/supervisor
    

COPY ./supervisord.conf /etc/supervisord.conf
COPY ./entrypoint.sh /home/.
RUN /bin/bash -c "chown $user:$user /home/entrypoint.sh"

ENTRYPOINT /bin/bash -c ". /home/entrypoint.sh"