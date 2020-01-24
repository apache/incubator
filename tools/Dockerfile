# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#############################################################################
# Dockerfile with many of the tools necessary for diagram generation
#
# A comprehensive list of asciidoctor diagramming tools and their
# requirements can be found at:
# - https://github.com/asciidoctor/asciidoctor-diagram
#
# You can find examples in the tools/maven-revealjs-asciidocter-template/
# presentation. A typical presentation will not use ALL of these tools.
#
# To build this image:
#
# docker image build --build-arg USER_ID=$(id -u ${USER}) --build-arg GROUP_ID=$(id -g ${USER}) -t training-build .
#
# (Passing the `USER_ID` and `GROUP_ID` is useful to build presentations with
# the same user and permissions inside the docker container.)
#
# To build a presentation using this image:
#
# cd incubator-training/tools/maven-revealjs-asciidoctor-template/
# docker run -it --rm --volume $PWD:/opt/workdir training-build:latest -c "mvn clean package"
#
# Alternatively, you can include a reference to your local .m2 to speed up the build:
#
# docker run -it --rm --volume $HOME/.m2:/home/docker-user/.m2 --volume $PWD:/opt/workdir training-build:latest
#
# To run the presentation using jetty:
#
# docker run -it --rm --publish 58080:8080/tcp --volume $HOME/.m2:/home/docker-user/.m2 --volume $PWD:/opt/workdir training-build:latest -c "mvn jetty:run-exploded"
#
# Alternatively, you can serve the pages in the target/generated-slides/
# directory using any web server:
#
# docker run -d --name my-tmp-httpd -p 58080:80 -v $PWD/target/generated-slides/:/usr/local/apache2/htdocs/:ro httpd:2.4
#

# Start bt building some tools using a multistage docker.
# ===========================================================================

FROM haskell:8 as tool-haskell-builder
RUN cabal update && cabal install --allow-newer erd

FROM rust:1.38.0 as tool-rust-builder
RUN cargo install svgbob_cli

# Build a docker image containing every tool necessary to build the template
# ===========================================================================

FROM centos:8

# System tools --------------------------------------------------------------

RUN dnf install -y git wget bzip2

# Maven build tool ----------------------------------------------------------

# asciidocter, revealjs, c3 and d3 javascript libraries are installed
# during the maven build.

# automatically included: meme generator, plantuml

RUN dnf install -y maven

# http://www.graphviz.org/ graph visualisation tools ------------------------

RUN dnf install -y graphviz

# http://blockdiag.com/en/ family of diagramming tools ----------------------
# Requires: python

RUN dnf install -y python36
RUN python3 -m pip install --upgrade pip setuptools seqdiag blockdiag \
    actdiag nwdiag

# Meme generator ------------------------------------------------------------
# Requires: ImageMagick (for convert and
RUN dnf install -y epel-release
RUN dnf install -y ImageMagick

# https://github.com/BurntSushi/erd entity-relationship diagrams ------------
# Requires: graphviz

COPY --from=tool-haskell-builder /root/.cabal/bin/erd /usr/local/bin/erd

# https://kevinpt.github.io/syntrax/ railroad diagrams ----------------------

RUN dnf install -y gcc cairo-devel redhat-rpm-config python3-devel pango-devel python3-gobject gtk3
RUN python3 -m pip install --upgrade syntrax

# https://github.com/ivanceras/svgbob ascii diagrams to SVG -----------------

COPY --from=tool-rust-builder /usr/local/cargo/bin/svgbob /usr/local/bin/svgbob

# https://vega.github.io/vega/ Vega visualisation tools ---------------------

RUN dnf install -y nodejs
RUN dnf install -y python2
RUN PYTHON=/usr/bin/python2 npm install --unsafe-perm --global vega-cli pango

# https://mermaidjs.github.io/#/ Mermaid markdownish charts -----------------
# Requires: npm

# This provides the mmdc command, but it looks like asciidoctor still
# requires the mermaid command.  Version issue?

RUN npm install --unsafe-perm --global mermaid.cli

## Run as current user, inspired by:
## https://jtreminio.com/blog/running-docker-containers-as-current-host-user/#ok-so-what-actually-works
ARG USER_ID
ARG GROUP_ID

RUN if [ ${USER_ID:-0} -ne 0 ] && [ ${GROUP_ID:-0} -ne 0 ]; then \
    if getent passwd docker-user ; then userdel -f docker-user; fi && \
    if getent group docker-user ; then groupdel docker-user; fi &&\
    groupadd -g ${GROUP_ID} docker-user &&\
    useradd -l -u ${USER_ID} -g docker-user docker-user &&\
    install -d -m 0755 -o docker-user -g docker-user /home/docker-user\
    && chown --changes --silent --no-dereference --recursive \
            ${USER_ID}:${GROUP_ID} \
       /usr/local/ \
;fi

USER docker-user
WORKDIR /opt/workdir

ENTRYPOINT [ "bash" ]
