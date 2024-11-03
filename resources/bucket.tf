# terraform {
#   backend "s3" {
#     bucket = "project-1-aws-etl"
#     key    = "terraform/tfstate"
#     region = "us-west-1"  # Use the exact region value here
#   }
# }

resource "aws_s3_bucket" "example" {
  bucket = "project-1-aws-etl"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}