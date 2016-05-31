#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_arhitektuurkolm.sock"

workers = 2
proc_name = "arhitektuurkolm"
#loglevel = 'debug'
