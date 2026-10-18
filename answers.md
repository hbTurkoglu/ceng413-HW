# HW-1 Written Answers

1. Explain the order of the instructions in your Dockerfile. What would happen to build time if you changed the order of two of them?

First, I set the working folder with WORKDIR /app and copied requirements.txt to install the Python packages with pip install. After that, I copied my code with COPY , created appuser so the container does not run as root, and started the app on port 8000 with gunicorn. I put COPY requirements.txt . before COPY . . because Docker uses layer caching. When I change app.py, Docker does not need to install Flask and Gunicorn again because requirements.txt did not change. If I changed their order and copied the code first, every small edit in app.py would break the cache and make the build much slower.


2. What happens to data written inside a container when the container is removed? How would you keep the data, and where should an application keep important state?

When we remove a container with docker rm, all files created inside the container  are deleted . If we want to keep the files, we can  save them on the host computer. However, a web app should not keep important data inside the container. Important state like user information should be saved in an external database  so we do not lose data when containers are removed or updated.

3. Why is the latest tag a risk for reproducibility? What did you use instead?

Using the latest tag is risky because it always downloads the newest version, which can change at any time.Because of this, I did not use latest and used python:3.12


Because of an OBS issue, I couldn't attend the lab class. So, I'm using AI to understand the project, figure out what to do, and ask questions like 'What is Docker?'(all information like that) for myself. 