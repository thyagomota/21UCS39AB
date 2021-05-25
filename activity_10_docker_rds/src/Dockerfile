# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 10 - Extract the dollar to real exchange rate, saving it into a database.

FROM python:latest 
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY dollar2real.py .
ENV DB_HOST=dollar2real.cvhpjdm21h9e.us-west-1.rds.amazonaws.com
ENV DB_NAME=dollar2real
ENV DB_USER=dollar2real 
ENV DB_PASSWORD=135791
CMD ["python", "dollar2real.py"]