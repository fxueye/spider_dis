rm *.log* -f

#!/bin/bash
# shutdown server
./stop.sh


# run app server
./run-app.sh
sleep 2

