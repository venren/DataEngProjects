# Big Data using Cloud

## Goals to acheive in this project
* Create a Big data processing project with AWS
* Tech stack to use - Apache Spark with pyspark library, AWS EMR Serverless
* Use Terraform for building infrastructure
* Come up with clear design diagram - research and come up with tool to build system diagram

## Track follow up from this project to avoid scope creep in this project
* AWS Glue - how to use it and why is it different from EMR serverless 

### Dataset used in the project
Spotify - https://www.kaggle.com/datasets/dhruvildave/spotify-charts 

### AWS Services used in this project with terraform script and usage


| **AWS Service Name** | **Terraform Script** | **Usage** |
|-----------------------|----------------------|-----------|
| **VPC**              |                      | Represents the overall network in which your AWS resources (e.g., EC2 instances, RDS databases, EMR clusters) are deployed. |
| **Subnet**           |                      | Segments of the VPC, typically used to group resources based on their networking requirements (e.g., internet access, security). |
| **Internet Gateway** |                      | Allows public subnets to communicate with the internet. Traffic from resources in the public subnet is routed through this gateway. |
| **NAT Gateway** | | Allows resources in private subnets to access the internet without exposing them directly. |
| **Route Tables** | | Subnets enforce security at the instance level (via security groups) and subnet level (via Network ACLs). |
