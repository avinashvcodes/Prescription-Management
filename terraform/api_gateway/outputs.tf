output "rest_api_execution_arn"{
  value = aws_api_gateway_rest_api.rest_api_pharmacy_management.execution_arn
}

output "authorizer_id" {
  value = aws_api_gateway_authorizer.pharmacy_management_authorizer.id
}