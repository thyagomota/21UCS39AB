# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 08 - Extract the dollar to real exchange rate

FROM python:latest 
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY dollar2real.py .
CMD ["python", "dollar2real.py"]