module "prescription" {
  source = "terraform-aws-modules/lambda/aws"
  create_function = false
  source_path = [
    {path = "../src/python/prescription"
    prefix_in_zip = "prescription"},
    {
      path = "../src/python/models"
      prefix_in_zip = "models"
      patterns = ["!../src/python/models/__pycache__"] 
    },
    {
      path = "../src/python/service"
      prefix_in_zip = "service"
      patterns = ["!../src/python/service/__pycache__"] 
    },
    {
      path = "../src/python/common"
      prefix_in_zip = "common"
      patterns = ["!../src/python/service/__pycache__"]
    }
    ]
  artifacts_dir = "academy2022/lambda_function_prescription"
  store_on_s3 = true
  s3_bucket = "academy-terraform-lambda-source-code-v2"
  tags = {
      owner = "Avinash"
    }
}

resource "aws_lambda_function" "prescription_lambda_function" {
  function_name = "lambda_function_prescription"
  s3_bucket = module.prescription.s3_object.bucket
  s3_key = module.prescription.s3_object.key
  s3_object_version = module.prescription.s3_object.version_id
  handler = "prescription.lambda_post_prescription.post_prescription"
  runtime = "python3.9"
  timeout = 60
  memory_size = 128
  role = data.aws_iam_role.academy_lambda_access.arn
  depends_on = [
    module.prescription
  ]
  layers = [module.lambda_layer.this_lambda_layer_arn]
  vpc_config {
    subnet_ids         = var.vpc_subnet_ids
    security_group_ids = [var.security_group_id]
  }
  environment {
    variables = var.environment_variables
  }
  tags = var.lambda_tags
}

/* output "so" {
  value = aws_lambda_function.prescription_lambda_function.vpc_config[0]
} */

resource "aws_lambda_permission" "prescription_lambda_function_permission" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.prescription_lambda_function.function_name
  principal = "apigateway.amazonaws.com"
  statement_id = "AllowAPIInvoke"
  source_arn = "${var.rest_api_execution_arn}/*/POST/v1/pharmacy/prescription"
}