module "prescription-items" {
  source = "terraform-aws-modules/lambda/aws"
  create_function = false
  source_path = [
    {
      path = "../src/python/prescription_items"
      prefix_in_zip = "prescription_items"
    },
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
  artifacts_dir = "academy2022/lambda_function_prescription_items_avinash"
  store_on_s3 = true
  s3_bucket = "academy-terraform-lambda-source-code-v2"
  tags = {
      owner = "Avinash"
    }
}

resource "aws_lambda_function" "prescription_items_lambda_function" {
    function_name = "lambda_function_prescription_items_avinash"
    s3_bucket = module.prescription-items.s3_object.bucket
    s3_key = module.prescription-items.s3_object.key
    s3_object_version = module.prescription-items.s3_object.version_id
    role = data.aws_iam_role.academy_lambda_access.arn
    runtime = "python3.9"
    handler = "prescription_items.lambda_post_prescription_items_avinash.post_prescription_items"
    layers = [module.lambda_layer.this_lambda_layer_arn]
    depends_on = [
        module.prescription-items
    ]
    timeout = 60
    memory_size = 128
    environment {
      variables = var.environment_variables
    }
    vpc_config {
      subnet_ids         = var.vpc_subnet_ids
      security_group_ids = [var.security_group_id]
    }
    tags = var.lambda_tags
}

resource "aws_lambda_permission" "prescription_items_lambda_function_permission" {
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.prescription_items_lambda_function.function_name
    principal = "apigateway.amazonaws.com"
    statement_id = "AllowAPIInvoke"
    source_arn = "${var.rest_api_execution_arn}/*/POST/v1/pharmacy/prescription-items"
}