resource "aws_api_gateway_resource" "prescription" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  parent_id = aws_api_gateway_resource.pharmacy.id
  path_part = "prescription"
  depends_on = [
    aws_api_gateway_resource.pharmacy
  ]
}

resource "aws_api_gateway_method" "post_prescription" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = "POST"
  authorization = "CUSTOM"
  api_key_required = true
  authorizer_id = aws_api_gateway_authorizer.pharmacy_management_authorizer.id
  request_models = {
    "application/json" = aws_api_gateway_model.prescription_model.name
  }
  request_validator_id = aws_api_gateway_request_validator.post_put_validator.id
  request_parameters = {
    "method.request.header.email" = true
    "method.request.header.Password" = true
  }
}

resource "aws_api_gateway_integration" "post-prescription-request-integration" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  integration_http_method = "POST"
  type = "AWS"
  uri = var.prescription-lambda-invoke-arn
  request_parameters = {
    "integration.request.header.email" = "method.request.header.email"
    "integration.request.header.Password" = "method.request.header.Password"
  }
  request_templates = {
    "application/json" = "${file("templates/default.template")}"
  }
  passthrough_behavior = "WHEN_NO_TEMPLATES"
}

resource "aws_api_gateway_method_response" "post_prescription_response_200" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = "200"
}

resource "aws_api_gateway_integration_response" "post_prescription_response_200i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = aws_api_gateway_method_response.post_prescription_response_200.status_code
}

resource "aws_api_gateway_method_response" "post_prescription_response_400" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = "400"
}

resource "aws_api_gateway_integration_response" "post_prescription_response_400i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = aws_api_gateway_method_response.post_prescription_response_400.status_code
  selection_pattern = ".*Missing.*"
  response_templates = {
    "application/json" = "${file("templates/invalid_request.template")}"
  }
}

resource "aws_api_gateway_method_response" "post_prescription_response_500" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = "500"
}

resource "aws_api_gateway_integration_response" "post_prescription_response_500i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.prescription.id
  http_method = aws_api_gateway_method.post_prescription.http_method
  status_code = aws_api_gateway_method_response.post_prescription_response_500.status_code
  selection_pattern = ".*Error.*"
  response_templates = {
    "application/json" = "${file("templates/internal_server_error.template")}"
  }
}

