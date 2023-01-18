FROM gcc:11

RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.5.0.2216-linux.zip && \
    unzip sonar-scanner-cli-4.5.0.2216-linux.zip && \
    rm sonar-scanner-cli-4.5.0.2216-linux.zip && \
    mv sonar-scanner-4.5.0.2216-linux /usr/local/sonar-scanner && \
    ln -s /usr/local/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner

