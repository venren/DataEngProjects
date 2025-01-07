resource "aws_subnet" "private_subnet_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a" # Update to your region's AZ
  map_public_ip_on_launch = false

  tags = {
    Name = "emr-private-subnet-1"
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b" # Update to your region's AZ
  map_public_ip_on_launch = false

  tags = {
    Name = "emr-private-subnet-2"
  }
}
