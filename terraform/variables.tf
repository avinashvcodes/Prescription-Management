variable "access_key" {
}

variable "secret_key" {
}

variable "region" {
}

variable "vpc_subnet_ids" {
}

variable "security_group_id" {
}

variable "db_username" {
}

variable "db_database" {
}

variable "db_schema" {
}

variable "db_host" {
}

variable "db_password" {
}

variable "db_port" {
}

locals {
  environment_variables = {
    username = var.db_username
    password = var.db_password
    host = var.db_host
    port = var.db_port
    database = var.db_database
    schema = var.db_schema
    timeout = 60
  }
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