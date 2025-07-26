resource "aws_api_gateway_resource" "get_prescription_items" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  parent_id = aws_api_gateway_resource.pharmacy.id
  path_part = "get-prescription-items"
  depends_on = [
    aws_api_gateway_resource.pharmacy
  ]
}

resource "aws_api_gateway_method" "get_prescription_items" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = "GET"
  authorization = "CUSTOM"
  api_key_required = true
  authorizer_id = aws_api_gateway_authorizer.pharmacy_management_authorizer.id
  request_validator_id = aws_api_gateway_request_validator.get_validator.id
  request_parameters = {
    "method.request.querystring.prescriptionId" = true
    "method.request.querystring.drugId" = false
  }
  depends_on = [
    aws_api_gateway_resource.get_prescription_items
  ]
}

resource "aws_api_gateway_integration" "get_prescription_items_integration" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  integration_http_method = "POST"
  type = "AWS"
  uri = var.get-prescription-items-lambda-invoke-arn
  request_templates = {
    "application/json" = "${file("templates/default.template")}"
  }
  request_parameters = {
    "integration.request.querystring.prescriptionId" = "method.request.querystring.prescriptionId"
    "integration.request.querystring.drugId" = "method.request.querystring.drugId"
  }
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  depends_on = [
    aws_api_gateway_method.get_prescription_items
  ]
}

resource "aws_api_gateway_method_response" "get_prescription_items_response_200" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = "200"
  depends_on = [
    aws_api_gateway_integration.get_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "get_prescription_items_response_200i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = aws_api_gateway_method_response.get_prescription_items_response_200.status_code
  depends_on = [
    aws_api_gateway_method_response.get_prescription_items_response_200
  ]
}

resource "aws_api_gateway_method_response" "get_prescription_items_response_400" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = "400"
  
  depends_on = [
    aws_api_gateway_integration.get_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "get_prescription_items_response_400i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = aws_api_gateway_method_response.get_prescription_items_response_400.status_code
  selection_pattern = ".*No data.*"
  depends_on = [
    aws_api_gateway_method_response.get_prescription_items_response_400
  ]
  response_templates = {
    "application/json" = "${file("templates/no_data.template")}"
  }
}

resource "aws_api_gateway_method_response" "get_prescription_items_response_404" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = "404"
  
  depends_on = [
    aws_api_gateway_integration.get_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "get_prescription_items_response_404i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = aws_api_gateway_method_response.get_prescription_items_response_404.status_code
  selection_pattern = ".*Missing.*"
  depends_on = [
    aws_api_gateway_method_response.get_prescription_items_response_404
  ]
  response_templates = {
    "application/json" = "${file("templates/invalid_request.template")}"
  }
}

resource "aws_api_gateway_method_response" "get_prescription_items_response_500" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = "500"
  
  depends_on = [
    aws_api_gateway_integration.get_prescription_items_integration
  ]
}

resource "aws_api_gateway_integration_response" "get_prescription_items_response_500i" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  resource_id = aws_api_gateway_resource.get_prescription_items.id
  http_method = aws_api_gateway_method.get_prescription_items.http_method
  status_code = aws_api_gateway_method_response.get_prescription_items_response_500.status_code
  selection_pattern = ".*Error.*"
  depends_on = [
    aws_api_gateway_method_response.get_prescription_items_response_500
  ]
  response_templates = {
    "application/json" = "${file("templates/internal_server_error.template")}"
  }
}
