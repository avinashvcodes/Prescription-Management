provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region = var.region
}


module "lambda" {
  source = "./lambda"
  rest_api_execution_arn = module.api_gateway.rest_api_execution_arn
  authorizer_id = module.api_gateway.authorizer_id
  environment_variables = local.environment_variables
  vpc_id = var.vpc_id
  security_group_id = var.security_group_id
  vpc_subnet_ids = var.vpc_subnet_ids
}

module "api_gateway" {
  source = "./api_gateway"
  get-prescription-lambda-invoke-arn = module.lambda.get-prescription-lambda-invoke-arn
  prescription-lambda-invoke-arn = module.lambda.prescription-lambda-invoke-arn
  authorizer-invoke-arn = module.lambda.authorizer-invoke-arn
  update-prescription-lambda-invoke-arn = module.lambda.update-prescription-lambda-invoke-arn
  prescription-items-lambda-invoke-arn = module.lambda.prescription-items-lambda-invoke-arn
  get-prescription-items-lambda-invoke-arn = module.lambda.get-prescription-items-lambda-invoke-arn
  update-prescription-items-lambda-invoke-arn = module.lambda.update-prescription-items-lambda-invoke-arn
}





