# FROM python:3.13.0rc1
# # RUN apt-get update && apt-get install -y --no-install-recommends curl
# RUN useradd -ms /bin/bash vscode
# USER vscode
# ENV PATH="/home/vscode/.local/bin:${PATH}"

# WORKDIR /workspace
# RUN pip install --upgrade pip
# RUN pip install pipenv
# # RUN pip install --upgrade pip --root-user-action=ignore
# # RUN pip install pipenv --root-user-action=ignore
# COPY Pipfile Pipfile.lock /workspace/
# RUN pipenv install --deploy --ignore-pipfile || (cat /workspace/Pipfile.lock && false)
# CMD ["bash"]

FROM python:3.13.0rc1

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Railway uses $PORT env variable internally)
ENV PORT=8000
EXPOSE $PORT

# Start Gunicorn server with your Django app
CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]
