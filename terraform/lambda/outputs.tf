output "get-prescription-lambda-invoke-arn" {
  value = aws_lambda_function.get_prescription_lambda_function.invoke_arn
}

output "prescription-lambda-invoke-arn" {
  value = aws_lambda_function.prescription_lambda_function.invoke_arn
}

output "authorizer-invoke-arn" {
  value = aws_lambda_function.authorizer_lambda_function.invoke_arn
}

output "update-prescription-lambda-invoke-arn" {
  value = aws_lambda_function.update_prescription_lambda_function.invoke_arn
}

output "prescription-items-lambda-invoke-arn" {
  value = aws_lambda_function.prescription_items_lambda_function.invoke_arn
}

output "get-prescription-items-lambda-invoke-arn" {
  value = aws_lambda_function.get_prescription_items_lambda_function.invoke_arn
}

output "update-prescription-items-lambda-invoke-arn" {
  value = aws_lambda_function.update_prescription_items_lambda_function.invoke_arn
}