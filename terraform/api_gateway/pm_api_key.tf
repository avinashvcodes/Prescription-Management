resource "aws_api_gateway_api_key" "api_key" {
    name = "api_key_pharmacy_management"
    tags = {
      owner = "Avinash"
    }
}

resource "aws_api_gateway_usage_plan" "usage_plan" {
  name = "usage_plan_pharmacy_management"

  api_stages {
    api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
    stage  = aws_api_gateway_deployment.dev.stage_name
  }
  depends_on = [
    aws_api_gateway_deployment.dev
  ]
}

resource "aws_api_gateway_usage_plan_key" "usage_plan_key" {
  key_id        = aws_api_gateway_api_key.api_key.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.usage_plan.id
  depends_on = [
    aws_api_gateway_deployment.dev
  ]
}