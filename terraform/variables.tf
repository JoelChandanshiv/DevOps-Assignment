variable "aws_region" {
  default = "ap-south-1"
}
variable "backend_image_tag" {
  description = "Image tag (Git SHA) for backend"
  type        = string
}

variable "frontend_image_tag" {
  description = "Image tag (Git SHA) for frontend"
  type        = string
}
variable "ecr_backend_repo" {
  default     = "850995570360.dkr.ecr.ap-south-1.amazonaws.com/devops-backend"
  description = "ECR repository for backend"
}

variable "ecr_frontend_repo" {
  default     = "850995570360.dkr.ecr.ap-south-1.amazonaws.com/devops-frontend"
  description = "ECR repository for frontend"
}