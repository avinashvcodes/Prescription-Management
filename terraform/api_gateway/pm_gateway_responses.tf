resource "aws_api_gateway_gateway_response" "test" {
  rest_api_id   = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  status_code   = "400"
  response_type = "BAD_REQUEST_BODY"

  response_templates = {
    "application/json" = "{\"error\": \"Invalid request\",\"message\":\"$context.error.validationErrorString\"}"
  }
}