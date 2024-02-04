FROM jenkins/jenkins:2.442-alpine

USER root

# Install plugins and setup jenkins instance with CASC
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /root/jenkins.yaml
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY jenkins.yaml /root/jenkins.yaml
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

# Install docker
# If jenkins is set up as dind those two lines can be removed
RUN apk add --update curl docker openrc docker-cli-compose
RUN rc-update add docker boot