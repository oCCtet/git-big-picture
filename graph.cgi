#!/bin/sh

# git-big-picture CGI program to construct and return
# an SVG image for the specified git repository

# only the GET method is supported
if [ "$REQUEST_METHOD" != "GET" ]; then
    echo "Status: 501 Not Implemented"
    echo ""
    exit 0;
fi

# the 'r' option must be provided to tell what repo to access
r=`echo "$QUERY_STRING" | sed 's/&/\n/g' | awk 'BEGIN { FS="=" } /^r=[a-zA-Z0-9_-+\.\/]+$/ { print $2 }'`
if [ -z "$r" ] || [ ! -d "$r" ]; then
    echo "Status: 400 Bad Request"
    echo ""
    exit 0;
fi

# ------------------------------------------------------------------
echo "Status: 200 OK"
echo "Content-type : image/svg+xml"
echo ""

git-big-picture --format=svg -pVO "$r"
