resource "aws_emrserverless_application" "example" {
  name     = "emr-serverless-app"
  release_label = "emr-6.8.0" # Update based on your required version
  type     = "SPARK"         # Options: SPARK, HIVE, etc.

  initial_capacity {
    worker_type = "Driver"
    worker_count = 1
  }

  maximum_capacity {
    worker_type = "Driver"
    worker_count = 1
  }

  network_configuration {
    security_group_ids = [aws_security_group.emr_sg.id]
    subnet_ids         = [
      aws_subnet.private_subnet_1.id,
      aws_subnet.private_subnet_2.id
    ]
  }
}
