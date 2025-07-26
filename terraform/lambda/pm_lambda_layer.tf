module "lambda_layer" {
    source = "terraform-aws-modules/lambda/aws"
    create_layer = true
    create_function = false
    layer_name = "lambda_layer"
    compatible_runtimes = ["python3.9"]
    source_path = [{
        pip_requirements = "../requirements.txt"
        prefix_in_zip = "python"
    }]
    store_on_s3 = true
    s3_bucket = "academy-terraform-lambda-source-code-v2"
    artifacts_dir = "academy2022/lambda_layer"
    runtime = "python3.9"
    tags = {
      owner = "Avinash"
    }
    /* runtime is mandatory when using pip_requirements */
    /* runtime is used to pip install requirements.txt in specified python version*/
}
