resource "aws_api_gateway_rest_api" "rest_api_pharmacy_management_avinash" {
  name = "rest_api_pharmacy_management_avinash"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
  tags = {
    owner = "Avinash"
  }
}

resource "aws_api_gateway_resource" "v1" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  parent_id   = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.root_resource_id
  path_part   = "v1"
}

resource "aws_api_gateway_resource" "pharmacy" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  parent_id   = aws_api_gateway_resource.v1.id
  path_part   = "pharmacy"
}

resource "aws_api_gateway_deployment" "dev" {
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  stage_name = "dev"
}