# Build Stage
FROM lacion/alpine-golang-buildimage:1.13 AS build-stage

LABEL app="build-feedstar-api"
LABEL REPO="https://github.com/helithumper/feedstar-api"

ENV PROJPATH=/go/src/github.com/helithumper/feedstar-api

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

ADD . /go/src/github.com/helithumper/feedstar-api
WORKDIR /go/src/github.com/helithumper/feedstar-api

RUN make build-alpine

# Final Stage
FROM golang:1.13.5-alpine3.10

ARG GIT_COMMIT
ARG VERSION
LABEL REPO="https://github.com/helithumper/feedstar-api"
LABEL GIT_COMMIT=$GIT_COMMIT
LABEL VERSION=$VERSION

# Because of https://github.com/docker/docker/issues/14914
ENV PATH=$PATH:/opt/feedstar-api/bin

WORKDIR /opt/feedstar-api/bin

COPY --from=build-stage /go/src/github.com/helithumper/feedstar-api/bin/feedstar-api /opt/feedstar-api/bin/
RUN chmod +x /opt/feedstar-api/bin/feedstar-api

# Create appuser
RUN adduser -D -g '' feedstar-api
USER feedstar-api

# ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/opt/feedstar-api/bin/feedstar-api"]
