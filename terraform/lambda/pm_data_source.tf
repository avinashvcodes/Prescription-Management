data "aws_subnet_ids" "private" {
  vpc_id = var.vpc_id
  tags = {
    Tier = "private"
    Name = "private-subnet-a"
  }
}

data "aws_security_group" "selected" {
  name = "lambda-security-group"
}

data "aws_iam_role" "lambda_access_role" {
    name = "lambda_access_role"
}