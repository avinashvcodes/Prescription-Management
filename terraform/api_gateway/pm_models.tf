resource "aws_api_gateway_model" "prescription_model" {
  rest_api_id  = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  name         = "prescription"
  content_type = "application/json"

  schema = <<EOF
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "physiciansId": {
      "type": "string"
    },
    "customerId": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "paymentMethod": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "otherDetails": {
      "type": "object"
    },
    "date": {
      "type": "string"
    },
    "createdBy": {
      "type": "string"
    }
  },
  "required": [
    "physiciansId",
    "customerId",
    "status",
    "paymentMethod",
    "date",
    "createdBy"
  ]
}
EOF
}

resource "aws_api_gateway_model" "update_prescription_model" {
  rest_api_id  = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  name         = "updatePrescription"
  content_type = "application/json"

  schema = <<EOF
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "prescriptionId": {
      "type": "string"
    },
    "physiciansId": {
      "type": "string"
    },
    "customerId": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "paymentMethod": {
      "type": "object",
      "properties": {
        "code": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      },
      "required": [
        "code",
        "name"
      ]
    },
    "otherDetails": {
      "type": "object"
    },
    "date": {
      "type": "string"
    },
    "updatedBy": {
      "type": "string"
    }
  },
  "required": [
    "prescriptionId",
    "physiciansId",
    "customerId",
    "status",
    "paymentMethod",
    "date",
    "updatedBy"
  ]
}
EOF
}

resource "aws_api_gateway_model" "prescription_items_model" {
  rest_api_id  = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  name         = "prescriptionItems"
  content_type = "application/json"

  schema = <<EOF
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "drugId": {
      "type": "string"
    },
    "prescriptionId": {
      "type": "string"
    },
    "quantity": {
      "type": "integer"
    },
    "instructionToCustomer": {
      "type": "string"
    },
    "createdBy": {
      "type": "string"
    }
  },
  "required": [
    "drugId",
    "prescriptionId",
    "quantity",
    "createdBy"
  ]
}
EOF
}

resource "aws_api_gateway_model" "update_prescription_items_model" {
  rest_api_id  = aws_api_gateway_rest_api.rest_api_pharmacy_management_avinash.id
  name         = "updatePrescriptionItems"
  content_type = "application/json"

  schema = <<EOF
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "drugId": {
      "type": "string"
    },
    "prescriptionId": {
      "type": "string"
    },
    "quantity": {
      "type": "integer"
    },
    "instructionToCustomer": {
      "type": "string"
    },
    "updatedBy": {
      "type": "string"
    }
  },
  "required": [
    "drugId",
    "prescriptionId",
    "quantity",
    "updatedBy"
  ]
}
EOF
}


