variable "rest_api_execution_arn" {
    type = string
}

variable "authorizer_id" {
    type = string
}

variable "vpc_subnet_ids" {
}

variable "security_group_id" {
}

variable "environment_variables" {
}

variable "lambda_tags"{
    type = map
    default = {
    author = "Avinash"
    runtime = "python3.9"
    project = "Pharmacy Management"
  }
}

variable "vpc_id" {
}