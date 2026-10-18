# CENG413 HW-1:  Web App
Build: `docker build -t ceng413-hw1:1.0 .`
Run: `docker run -d -p 8080:8080 -e APP_MESSAGE="Hello CENG413" --name ceng413-app ceng413-hw1:1.0`
Verify: `curl http://localhost:8080/health` and `curl http://localhost:8080/`
Stop: `docker rm -f ceng413-app`
