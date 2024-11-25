# Lambda function deployment example

# IAM Role for Lambda
resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for the Lambda role
resource "aws_iam_role_policy" "lambda_policy" {
  name   = "lambda_policy"
  role   = aws_iam_role.lambda_execution_role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Effect   = "Allow",
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Action   = [
          "s3:GetObject",
          "s3:ListBucket"
        ],
        Effect   = "Allow",
        Resource = [
          "arn:aws:s3:::${aws_s3_bucket.etl_bucket.id}",
          "arn:aws:s3:::${aws_s3_bucket.etl_bucket.id}/*"
        ]
      }
    ]
  })
}

resource "null_resource" "zip_lambda_code" {
  provisioner "local-exec" {
    command = <<-EOT
      echo "Current directory: $(pwd)"
      echo "Compressing the Lambda function"
      powershell -Command "Compress-Archive -Path 'C:\\Learning\\DE Projects\\src\\lambda\\etl_upload_lambda.py' -DestinationPath 'C:\\Learning\\DE Projects\\src\\datasets\\lambda_function.zip'"
    EOT
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}



# Lambda function resource that uses the ZIP file created above
resource "aws_lambda_function" "etl_lambda" {
  function_name = "etl_upload_lambda"
  runtime       = "python3.9"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "etl_upload_lambda.helloLambda"
  filename      = "C:\\Learning\\DE Projects\\src\\datasets\\lambda_function.zip"  # This will refer to the zipped file created locally

  depends_on = [null_resource.zip_lambda_code]  # Ensure the ZIP file is created before Lambda deployment
}

# CloudWatch log group for Lambda logs (optional)
resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/${aws_lambda_function.etl_lambda.function_name}"
  retention_in_days = 7 # Retain logs for 7 days
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.etl_lambda.function_name
  principal     = "s3.amazonaws.com"

  source_arn = aws_s3_bucket.etl_bucket.arn
}