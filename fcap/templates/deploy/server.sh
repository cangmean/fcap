#!/bin/sh
/root/v3/bin/gunicorn -c unicorn.py ../manage:app