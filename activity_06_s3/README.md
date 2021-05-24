# Activity 06

## Upload/Download/Delete to/from an S3 Bucket

## Goal
The goal of this activity is to illustrate how to create an S3 bucket and how to upload/download/delete files to/from the s3 bucket programmatically. 
 
## Steps

### Step 1 - Create an S3 Bucket

Remember, bucket names must be globally unique within AWS. 

```
aws s3api create-bucket \
    --bucket activity-06-ocean-breeze \
    --region us-west-1 \
    --create-bucket-configuration LocationConstraint=us-west-1
```

### Step 2 - Upload a File

```
aws s3 cp \
    files/eagle.jpeg s3://activity-06-ocean-breeze/eagle.jpeg
```

### Step 3 - List Contents of a Bucket

```
aws s3 ls s3://activity-06-ocean-breeze
```

### Step 4 - Download a File 

```
aws s3 cp \
    s3://activity-06-ocean-breeze/eagle.jpeg files/eagle2.jpeg
```

### Step 5 - Delete a File 

```
aws s3 rm s3://activity-06-ocean-breeze/eagle.jpeg
```

### Step 6 - Delete a Bucket 

```
aws s3 rb s3://activity-06-ocean-breeze --force  
```