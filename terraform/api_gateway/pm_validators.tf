resource "aws_api_gateway_request_validator" "post_put_validator" {
  name = "validate request body and request parameters"
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  validate_request_body = true
  validate_request_parameters = true
}

resource "aws_api_gateway_request_validator" "get_validator" {
  name = "validate request parameters"
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  validate_request_parameters = true
}