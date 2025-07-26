resource "aws_api_gateway_authorizer" "pharmacy_management_authorizer" {
  name = "authorizer_pharmacy_management"
  rest_api_id = aws_api_gateway_rest_api.rest_api_pharmacy_management.id
  type = "REQUEST"
  authorizer_uri = var.authorizer-invoke-arn
  identity_source = "method.request.header.email,method.request.header.Password"
  authorizer_result_ttl_in_seconds = 0
}
