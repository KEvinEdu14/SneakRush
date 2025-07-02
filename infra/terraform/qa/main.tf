provider "aws" { region = var.aws_region }

# 1) VPC
module "vpc" {
  source         = "../modules/vpc"
  region         = var.aws_region
  vpc_cidr       = var.vpc_cidr
  public_subnets = var.public_subnets
  private_subnets= var.private_subnets
}

# 2) Security Groups for RDS & EC2
resource "aws_security_group" "rds_sg" {
  name        = "qa-postgres-sg"
  vpc_id      = module.vpc.vpc_id
  ingress { from_port=5432; to_port=5432; protocol="tcp"; cidr_blocks=[var.vpc_cidr] }
  egress  { from_port=0; to_port=0; protocol="-1"; cidr_blocks=["0.0.0.0/0"] }
}
resource "aws_security_group" "ec2_sg" {
  name        = "qa-ec2-sg"
  vpc_id      = module.vpc.vpc_id
  ingress {
    from_port   = 22; to_port = 22; protocol="tcp"; cidr_blocks=["0.0.0.0/0"]
  }
  ingress {
    from_port   = 8000; to_port = 8000; protocol="tcp"; cidr_blocks=["0.0.0.0/0"]
  }
  egress  { from_port=0; to_port=0; protocol="-1"; cidr_blocks=["0.0.0.0/0"] }
}

# 3) RDS
module "postgres" {
  source               = "../modules/rds"
  region               = var.aws_region
  db_name              = "sneakrush"
  username             = "postgres"
  password             = "postgres"
  instance_class       = var.instance_type
  allocated_storage    = 20
  engine_version       = "15"
  subnet_ids           = module.vpc.private_subnet_ids
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
}

# 4) Auth Service EC2
module "auth_service" {
  source               = "../modules/ec2"
  region               = var.aws_region
  name                 = "auth-service"
  instance_type        = var.instance_type
  ami_filter           = "amzn2-ami-hvm-*-x86_64-gp2"
  subnet_ids           = module.vpc.public_subnet_ids
  security_group_ids   = [aws_security_group.ec2_sg.id]
  key_name             = var.key_name
}
