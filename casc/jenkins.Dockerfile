FROM jenkins/jenkins:2.444-alpine

USER root

# Install plugins and setup jenkins instance with CASC
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /root/jenkins.yaml
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY jenkins.yaml /root/jenkins.yaml
COPY jobs /root/casc/jobs
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt