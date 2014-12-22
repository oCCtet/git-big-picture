#!/bin/sh

# git-big-picture CGI program to construct and return
# an SVG image for the specified git repository

# only the GET method is supported
if [ "$REQUEST_METHOD" != "GET" ]; then
    printf "Status: 501 Not Implemented\r\n\r\n"
    printf "Invalid request method: $REQUEST_METHOD\r\n"
    printf "Only the GET method is supported."
    exit 0;
fi

# the 'r' option must be provided to tell what repo to access
r=`printf "$QUERY_STRING" \
    | sed 's/&/\n/g'      \
    | awk 'BEGIN { FS="=" } /^r=/ { printf $2 }'`
if [ -z "$r" ] || [ ! -d "$r" ]; then
    printf "Status: 400 Bad Request\r\n\r\n"
    printf "Invalid repository: '${r}'"
    exit 0;
fi

# ------------------------------------------------------------------
printf "Status: 200 OK\r\n"
printf "Content-type : image/svg+xml\r\n\r\n"

git-big-picture --format=svg -pVO "$r" || \
    printf 'digraph empty_repo {"(No commits)"}' | dot -Tsvg
