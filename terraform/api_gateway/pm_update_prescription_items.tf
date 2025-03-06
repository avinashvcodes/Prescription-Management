resource "aws_api_gateway_resource" "update_prescription_items" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  parent_id = aws_api_gateway_resource.pharmacy.id
  path_part = "update-prescription-items"
  depends_on = [
    aws_api_gateway_resource.pharmacy
  ]
}

resource "aws_api_gateway_method" "update_prescription_items" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = "PUT"
  authorization = "CUSTOM"
  api_key_required = true
  authorizer_id = aws_api_gateway_authorizer.pharmacy_management_authorizer.id
  request_validator_id = aws_api_gateway_request_validator.post_put_validator.id
  request_models = {
    "application/json" = aws_api_gateway_model.update_prescription_items_model.name
  }
  depends_on = [
    aws_api_gateway_resource.update_prescription_items
  ]
}

resource "aws_api_gateway_integration" "update_prescription_items_integration" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  integration_http_method = "POST"
  type = "AWS"
  uri = var.update-prescription-items-lambda-invoke-arn
  request_templates = {
    "application/json" = "${file("templates/default.template")}"
  }
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  depends_on = [
    aws_api_gateway_method.update_prescription_items
  ]
}

resource "aws_api_gateway_method_response" "update_prescription_items_response_200" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = "200"
  depends_on = [
    aws_api_gateway_integration.update_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "update_prescription_items_response_200i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = aws_api_gateway_method_response.update_prescription_items_response_200.status_code
  depends_on = [
    aws_api_gateway_method_response.update_prescription_items_response_200
  ]
}

resource "aws_api_gateway_method_response" "update_prescription_items_response_400" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = "400"
  depends_on = [
    aws_api_gateway_integration.update_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "update_prescription_items_response_400i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = aws_api_gateway_method_response.update_prescription_items_response_400.status_code
  selection_pattern = ".*Missing.*"
  depends_on = [
    aws_api_gateway_method_response.update_prescription_items_response_400
  ]
  response_templates = {
    "application/json" = "${file("templates/invalid_request.template")}"
  }
}

resource "aws_api_gateway_method_response" "update_prescription_items_response_500" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = "500"
  depends_on = [
    aws_api_gateway_integration.update_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "update_prescription_items_response_500i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  resource_id = aws_api_gateway_resource.update_prescription_items.id
  http_method = aws_api_gateway_method.update_prescription_items.http_method
  status_code = aws_api_gateway_method_response.update_prescription_items_response_500.status_code
  selection_pattern = ".*Error.*"
  depends_on = [
    aws_api_gateway_method_response.update_prescription_items_response_500
  ]
  response_templates = {
    "application/json" = "${file("templates/internal_server_error.template")}"
  }
}
