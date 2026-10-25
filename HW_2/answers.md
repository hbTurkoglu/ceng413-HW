

 1. Your app calls the second service by name. How does that work, and why does the same name not work between two containers on the default `docker run` network?
When we start the project with `docker compose up`, Docker Compose automatically creates a custom bridge network and puts both `app` and `redis` on that network. Custom networks in Docker have a built-in DNS server that translates the service name `redis` into the Redis container's IP address. Because of this, my Flask app can connect using `REDIS_HOST=redis` without needing a hardcoded IP address. 

2. Which of your services is stateless and which is not? Show the evidence: what did you do, and what happened to your data (for example `docker compose rm -sf app` and then `docker compose down`, and `docker compose down -v`)?
In my project, the `app` service is stateless because I removed the local `/data` file logic so it never writes to its own disk, while the `redis` service is stateful because it saves the visit counter and notes inside the `redis_data` named volume. 

 3. Where should a database password come from, and why is it a problem to commit it to Git, even in a private repository?
A database or Redis password should come from environment variables 

