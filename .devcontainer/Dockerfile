FROM python:3.13.0rc1
# RUN apt-get update && apt-get install -y --no-install-recommends curl
RUN useradd -ms /bin/bash vscode
USER vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"

WORKDIR /workspace
RUN pip install --upgrade pip
RUN pip install pipenv
# RUN pip install --upgrade pip --root-user-action=ignore
# RUN pip install pipenv --root-user-action=ignore
COPY Pipfile Pipfile.lock /workspace/
RUN pipenv install --deploy --ignore-pipfile || (cat /workspace/Pipfile.lock && false)
CMD ["bash"]