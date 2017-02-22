This App is simple format backend.

1. Create database
   $ python migrate.py db init
   $ python migrate.py db migrate
   $ python migrate.py db upgrade

2. Run app on :5555
   $ python run.py

3. Open other terminal
   curl -i http://localhost:5555/
   curl -i http://localhost:5555/main/
   curl -i http://localhost:5555/role/
   curl -i http://localhost:5555/user/

4. Check log
   $ tail -f log/debug
