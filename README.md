# flask-locust

# create docker image - docker build -t perf_test/python-flask .  
# run docker container - docker container run -d -p 5000:5000 perf_test/python-flask:latest  
# launch performance tests - locust -f load.py  