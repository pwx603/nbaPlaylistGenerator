#!/bin/sh
# wait-for-selenium.sh

set -e

host="$1"
shift

while ! curl --silent --fail "$host":4444; do
    echo >&2 'selenium not up, retrying in 5s...'
    sleep 5
done
echo >&2 'selenium up, exiting'
exec "$@"