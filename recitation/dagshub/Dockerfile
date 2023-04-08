FROM jupyter/datascience-notebook:2023-02-28
WORKDIR /home/jovyan/work
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
