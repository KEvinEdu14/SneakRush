variable "aws_region" {
  description = "Región AWS"
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR de la VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "Rangos CIDR de subnets públicas"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  description = "Rangos CIDR de subnets privadas"
  type        = list(string)
  default     = ["10.0.11.0/24", "10.0.12.0/24"]
}

variable "instance_type" {
  description = "Tipo de instancia EC2 para auth-service"
  default     = "t3.micro"
}

variable "key_name" {
  description = "sneakrush-qa-key"
  type        = string
}
