python3 database.py
export FLASK_APP=server.py
if [ -z $@ ]; then
  echo "please pass browser as argument."
  exit 0
fi

sleep 3& $@ 127.0.0.1:5000& flask run
