resource "aws_s3_bucket" "emr_bucket" {
  bucket = "emr-serverless-data-bucket" # Replace with a unique bucket name

  # Optional: Apply versioning or other configurations
  versioning {
    enabled = true
  }
}
