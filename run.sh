echo -----------------------[Ich gönn Mal Flask auf $HOSTNAME]---------------------------------
sudo apt install python3-venv
pip install Flask
echo ----------------------[Ich mach mal Datenbank]-------------------------------
python3 database.py
export FLASK_APP=server.py
if [ -z $@ ]; then
  echo "please pass browser as argument, pass _, to get rid of this warning"
  exit 0
fi
echo ----------------------[Ich mach mal Server an]-------------------------------
$@ http://127.0.0.1:5000/; flask run