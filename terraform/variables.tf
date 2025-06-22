variable "aws_region" {
  default = "ap-south-1"
}

variable "backend_image" {
  description = "ECR image URI for backend"
  type        = string
}
