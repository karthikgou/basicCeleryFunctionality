# fastApiApplication

execute the below command to start the rabbitmq broker using community image ::::
docker run -d -p 5672:5672 rabbitmq

execute below command to start the celery instance ::::
python -m celery -A tasks worker --pool=eventlet -l INFO


